#!/bin/bash

docker network ls

docker run -it --rm --name ctrA alpine

# Look for "Networks" JSON object in the metadata
docker inspect $CONTAINER_A_ID | vim -

# Look for "Containers" JSON object in the metadata
docker inspect bridge | vim -

docker network create sre101
docker network ls

docker run -it --rm --name ctrB --net sre101 alpine
docker inspect $CONTAINER_B_ID | vim -

# Show both the running containers
docker ps -a

docker run -it --rm --name ctrC --net sre101 alpine

# Inside ctrC
nc -l -p 80

# Expose container to host
docker run -it --rm --name ctrD --net sre101 -p 8000:80 alpine

# Inside ctrD
nc -l -p 80

# On host machine
curl localhost:8000

# Close all containers, then run this to delete network
docker network rm sre101
