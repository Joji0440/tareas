import grpc
import users_pb2
import users_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = users_pb2_grpc.UserServiceStub(channel)

    # 1. Agregar un usuario nuevo
    print("Agregando usuario...")
    add_response = stub.AddUser(users_pb2.AddUserRequest(name="Juan", age=22))
    print(f"Usuario agregado: ID={add_response.id}, Nombre={add_response.name}, Edad={add_response.age}")

    # 2. Obtener usuario por ID
    print("\nObteniendo usuario...")
    get_response = stub.GetUser(users_pb2.UserRequest(id=add_response.id))
    print(f"Usuario obtenido: ID={get_response.id}, Nombre={get_response.name}, Edad={get_response.age}")

    # 3. Modificar usuario
    print("\nModificando usuario...")
    update_response = stub.UpdateUser(users_pb2.UpdateUserRequest(id=add_response.id, name="Juan Modificado", age=30))
    print(f"Usuario modificado: ID={update_response.id}, Nombre={update_response.name}, Edad={update_response.age}")

    # 4. Eliminar usuario
    print("\nEliminando usuario...")
    delete_response = stub.DeleteUser(users_pb2.UserRequest(id=add_response.id))
    print(f"Eliminado: {delete_response.success}, Mensaje: {delete_response.message}")

if __name__ == '__main__':
    run()
