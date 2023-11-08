#!/bin/bash

# Run python app locally
pip3 install flask # In case you don't already have flask
python3 app.py

# Build
docker build -t hello-app:latest .
docker images

# Push to repository
docker login
docker tag hello-app:latest duaraghav8/hello-app:latest
docker push duaraghav8/hello-app:latest

# Pull from repository
docker pull duaraghav8/hello-app
docker images

# Run container
docker run --rm -d -p 5000:5000 duaraghav8/hello-app:latest
docker ps

# Analyse container
docker inspect <ID> | vim -
docker logs -f <ID>
docker exec -it <ID> /bin/ls -al
docker exec -it <ID> /bin/bash

# Remove image, Build again, with versioning
docker rmi <ID>
docker build -t duaraghav8/hello-app:0.1.0 .

# Stop & destroy
docker stop <ID>
docker rm <ID>
