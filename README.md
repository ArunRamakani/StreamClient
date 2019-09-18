# Stream Client

This is the stream client that can connect to gRPC stream server to transmit data in a stream after authentication through gRPC metadata. This client also compresses the data over the stream to optimize the transfer

## Build 

checkout the repository and run the below command to build the docker image in your local  

```docker build -t arunramakani/stream-client```

Alternatively we can pull the docker image from the Docker Hub directly using the below command

```docker pull arunramakani/stream-server```

## Run 

Once you have the image you can run the image using the command

```docker run -e server=34.69.90.135:80 arunramakani/stream-client```

Please not that I have hosted the Stream Server in GCE Kubernetes at "34.69.90.135:80". To host Stream Server yourself, go to repo https://github.com/ArunRamakani/StreamServer
