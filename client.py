import time
import grpc

import datastream_pb2_grpc
import datastream_pb2

from grpc._cython.cygrpc import CompressionAlgorithm
from grpc._cython.cygrpc import CompressionLevel

SERVER_ADDRESS = "34.67.155.227:80"


def client_streaming(stub):
    print("--------------Call ClientStreaming Method Begin--------------")

    def request_messages():
        for i in range(100):
            request = datastream_pb2.Request(user=(datastream_pb2.User(id=i, name=("name-%d" % i), message=("Welcome-%d" % i))))
            yield request

    response = stub.ClientStreaming(request_messages(), metadata=[('network-international', '643524tr^#sX')])
    print("resp from server with status=%s" % (response.result))
    
    if response.result == 0:
        print("--------------Call ClientStreamingMethod Over With Success---------------")
    else:
        print("--------------Call ClientStreamingMethod Over With Failure---------------")


def main():
    chan_ops = [('grpc.default_compression_algorithm', CompressionAlgorithm.gzip),
            ('grpc.grpc.default_compression_level', CompressionLevel.high)]
 
    with grpc.insecure_channel(SERVER_ADDRESS, chan_ops) as channel:
        stub = datastream_pb2_grpc.GRPCDataStreamStub(channel)
        client_streaming(stub)


if __name__ == '__main__':
    main()
