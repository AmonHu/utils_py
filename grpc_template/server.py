from concurrent import futures
import grpc

from protos import template_pb2_grpc
from grpc_core.template import Template


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    template_pb2_grpc.add_TemplateServicer_to_server(Template(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
