from grpc_template.protos import template_pb2_grpc, template_pb2


class Template(template_pb2_grpc.TemplateServicer):
    def __init__(self):
        pass

    def HelloWorld(self, request, context):
        return template_pb2.HelloWorldReply(result='hello world')

    def Hello(self, request, context):
        return template_pb2.HelloReply(greeting=f'hello, {request.name}')
