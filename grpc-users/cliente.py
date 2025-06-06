import grpc
import users_pb2
import users_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = users_pb2_grpc.UserServiceStub(channel)

    response = stub.GetUser(users_pb2.UserRequest(id=1))
    print(f"ID: {response.id}, Nombre: {response.name}, Edad: {response.age}")

if __name__ == '__main__':
    run()
