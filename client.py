import time
import grpc

import datastream_pb2_grpc
import datastream_pb2

from grpc._cython.cygrpc import CompressionAlgorithm
from grpc._cython.cygrpc import CompressionLevel

SERVER_ADDRESS = "localhost:23333"


def client_streaming(stub):
    print("--------------Call ClientStreaming Method Begin--------------")

    def request_messages():
        for i in range(100000):
            request = datastream_pb2.Request(
                request_data=("called by Python client, message:%d" % i))
            yield request

    response = stub.ClientStreaming(request_messages(), metadata=[('network-international', '643524tr^#sXT')])
    print("resp from server with status=%s" % (response.result))
    print("--------------Call ClientStreamingMethod Over---------------")


def main():
    chan_ops = [('grpc.default_compression_algorithm', CompressionAlgorithm.gzip),
            ('grpc.grpc.default_compression_level', CompressionLevel.high)]
    with grpc.insecure_channel(SERVER_ADDRESS,chan_ops) as channel:
        stub = datastream_pb2_grpc.GRPCDataStreamStub(channel)
        client_streaming(stub)


if __name__ == '__main__':
    main()