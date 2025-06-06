import grpc
from concurrent import futures
import time
import users_pb2
import users_pb2_grpc

class UserService(users_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        users = {
            1: {"name": "Carlos", "age": 25},
            2: {"name": "Ana", "age": 30}
        }
        user = users.get(request.id, {"name": "Desconocido", "age": 0})
        return users_pb2.UserResponse(id=request.id, name=user["name"], age=user["age"])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC en ejecución en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
