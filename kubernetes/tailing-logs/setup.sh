#!/bin/bash

# Start cluster
minikube start -p sre101 --nodes 4

kubectl create namespace production
kubectl config set-context --current --namespace production

# Deploy app
kubectl apply -f ./deployment.yaml

# Deploy daemonset
kubectl apply -f ./daemonset.yaml