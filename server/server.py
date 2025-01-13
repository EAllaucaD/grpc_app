from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc


# Implementing the Greeter service
class Greeter(service_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return service_pb2.HelloResponse(message=f'Hello, {request.name}!')

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add the Greeter service to the server
    service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    
    # Server starts listening on port 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    
    # Keep the server running
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
