FROM python:2.7

WORKDIR /StreamClient

ENV PATH "$PATH:/StreamClient"


COPY client.py /StreamClient
COPY datastream_pb2_grpc.py /StreamClient
COPY datastream_pb2.py /StreamClient
COPY datastream.proto /StreamClient
COPY server.crt /StreamClient


RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools googleapis-common-protos

CMD ["python", "./client.py"]