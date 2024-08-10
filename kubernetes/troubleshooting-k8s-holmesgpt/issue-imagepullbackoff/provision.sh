#!/bin/bash

# Create a private image in dockerhub - duaraghav8/payments-app

minikube start

kubectl run foobar --image duaraghav8/payments-app

# Shows that the pod is stuck in ImagePullBackoff
kubectl get pods


holmes ask --model "gpt-4o-2024-08-06" "Why is my payments pod not running? Explain the problem and suggest some solutions."
