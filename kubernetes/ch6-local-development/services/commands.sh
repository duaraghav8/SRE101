#!/bin/bash

# Create a multi-node minikube cluster, ensure kubectl points to it
minikube start --nodes 4 -p sre101

# Run mysql, expose it to localhost and try connecting.
# It should already be initialized with the data.
kubectl apply -f mysql/k8s-deployment.yaml
minikube -p sre101 service mysql
mysql -h localhost -P <MINIKUBE SERVICE PORT> --protocol=tcp -D sre101 -u root -ppassword

kubectl apply -f redis/k8s-deployment.yaml

kubectl apply -f service_a/k8s-deployment.yaml

kubectl apply -f service_b/k8s-deployment.yaml
