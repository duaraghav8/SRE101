#!/bin/zsh

# Build Image
docker build -t voltest:latest .

# Run container without volume mounting
docker run -it --rm voltest

# Create Volume
docker volume ls
docker volume create voltest
docker volume ls

# Run container with pre-created volume
docker run -it --rm --volume 'voltest:/data' voltest

# Volume operations
docker inspect voltest
docker rm voltest

# Use --mount for more customization
docker run \
    -it \
    --mount 'type=volume,src=voltest2,dst=/data,volume-driver=local' \
    voltest

# Cleanup
docker rmi voltest
docker volume rm voltest
