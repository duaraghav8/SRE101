#!/bin/bash

# Start cluster
minikube start -p sre101 --nodes 4

# Deploy app
kubectl apply -f ./deployment.yaml

# Deploy daemonset
kubectl apply -f https://k8s.io/examples/controllers/daemonset.yaml