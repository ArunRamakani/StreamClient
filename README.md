[![](https://images.microbadger.com/badges/version/arunramakani/stream-client.svg)](https://microbadger.com/images/arunramakani/stream-client "Get your own version badge on microbadger.com") [![](https://img.shields.io/docker/pulls/arunramakani/stream-client.svg)](https://img.shields.io/docker/pulls/arunramakani/stream-client.svg) [![](https://img.shields.io/docker/stars/arunramakani/stream-client.svg)](https://img.shields.io/docker/stars/arunramakani/stream-client.svg)


# Stream Client

This is the stream client that can connect to gRPC stream server to transmit data as streams after authentication through gRPC metadata. This client also compresses the data over the stream to optimize the transfer

## Build 

checkout the repository and run the below command to build the docker image in your local  

```docker build -t arunramakani/stream-client```

Alternatively we can pull the docker image from the Docker Hub directly using the below command

```docker pull arunramakani/stream-client```

## Run 

Once you have the image you can run the image using the command

```docker run -e server=34.69.90.135:80 arunramakani/stream-client```

Please not that I have hosted the Stream Server in GCE Kubernetes at "34.69.90.135:80". To host Stream Server yourself, go to repo https://github.com/ArunRamakani/StreamServer
