#!/bin/bash

# Prerequisites:
# Build and publish the docker images defined in app, sidecar and daemon

# Start cluster
minikube start -p sre101 --nodes 4

kubectl create namespace production
kubectl config set-context --current --namespace production

# Deploy app
kubectl apply -f ./deployment.yaml

# Deploy daemonset
kubectl apply -f ./daemonset.yaml