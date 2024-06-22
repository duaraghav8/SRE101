#!/bin/bash

# Commands to run everything as discussed in the video

# Create a multi-node minikube cluster, ensure kubectl points to it.
# This is just to test things locally.
# If your cluster is running remotely, just ensure that
# kubectl points to it.
# TODO: rename k8s cluster to "staging" for more clarity
minikube start --nodes 4 -p sre101

# Run mysql, expose it to localhost and try connecting to & querying it.
# It should already be initialized with the data.
kubectl apply -f mysql/k8s-deployment.yaml
minikube -p sre101 service mysql
mysql -h localhost -P <MINIKUBE SERVICE PORT> --protocol=tcp -D sre101 -u root -ppassword

# Run redis
kubectl apply -f redis/k8s-deployment.yaml

# Run Service B
kubectl apply -f service_b/k8s-deployment.yaml

# Run Service A
kubectl apply -f service_a/k8s-deployment.yaml


# After making some changes to Service A code locally,
# Run mirrord to test it.
# mirrord will run the service in the context of the
# specified K8s Pod.
# Before running, if required, you can create and start
# a python virtualenv and install all dependencies of
# service A.
cd service_a
mirrord exec --target pod/<POD NAME> python3 app.py

# Now the app is mirrored. Run curl in a different terminal
# to test the original functionality & the new changes.
curl http://localhost:5000/complex_request
curl http://localhost:5000/health

# At this point you can also make a request to the staging
# service A and see the request handled by local app.
# The response returned by local app is discarded.
# Change the response in your local app to prove this.

# Run mirrord with specific configurtion (traffic stealing)
mirrord exec -f mirrord-configs/steal-all-traffic.json --target pod/<POD NAME> python3 app.py
mirrord exec -f mirrord-configs/steal-traffic-header-based.json --target pod/<POD NAME> python3 app.py

# With traffic stealing enabled, response will look
# different when handled by staging app or local app. Show this.