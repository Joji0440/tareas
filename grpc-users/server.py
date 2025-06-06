import grpc
from concurrent import futures
import psycopg2
import users_pb2
import users_pb2_grpc

class UserService(users_pb2_grpc.UserServiceServicer):
    def __init__(self):
        # Conexión a la base de datos PostgreSQL
        self.conn = psycopg2.connect(
            dbname="suariosdb",
            user="lizzardi",      
            password="",          
            host="localhost"
        )

    def GetUser(self, request, context):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, name, age FROM usuarios WHERE id = %s", (request.id,))
            row = cur.fetchone()
            if row:
                return users_pb2.UserResponse(id=row[0], name=row[1], age=row[2])
            else:
                return users_pb2.UserResponse(id=request.id, name="Desconocido", age=0)

    def AddUser(self, request, context):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO usuarios (name, age) VALUES (%s, %s) RETURNING id", (request.name, request.age))
            user_id = cur.fetchone()[0]
            self.conn.commit()
            return users_pb2.UserResponse(id=user_id, name=request.name, age=request.age)

    def UpdateUser(self, request, context):
        with self.conn.cursor() as cur:
            cur.execute("UPDATE usuarios SET name = %s, age = %s WHERE id = %s RETURNING id", (request.name, request.age, request.id))
            updated = cur.fetchone()
            self.conn.commit()
            if updated:
                return users_pb2.UserResponse(id=request.id, name=request.name, age=request.age)
            else:
                return users_pb2.UserResponse(id=request.id, name="No encontrado", age=0)

    def DeleteUser(self, request, context):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM usuarios WHERE id = %s RETURNING id", (request.id,))
            deleted = cur.fetchone()
            self.conn.commit()
            if deleted:
                return users_pb2.DeleteUserResponse(success=True, message="Usuario eliminado")
            else:
                return users_pb2.DeleteUserResponse(success=False, message="Usuario no encontrado")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC en ejecución en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
