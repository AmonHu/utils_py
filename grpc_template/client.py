from __future__ import print_function
import logging
import time
import uuid
from random import uniform

import grpc

from grpc_template.protos import template_pb2
from protos import template_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = template_pb2_grpc.TemplateStub(channel)
        req = template_pb2.HelloRequest(name='grpc')
        tax_reply = stub.Hello(req)
        print(tax_reply.greeting)


if __name__ == '__main__':
    logging.basicConfig()
    run()
