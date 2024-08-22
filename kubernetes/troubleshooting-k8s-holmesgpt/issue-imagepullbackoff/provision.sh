#!/bin/bash

# Create a private image in dockerhub - duaraghav8/payments-app

minikube start

kubectl run payments-service --image duaraghav8/payments-app

# Shows that the pod is stuck in ImagePullBackoff
kubectl get pods


holmes ask --model "gpt-4o-2024-08-06" "Why is my payments pod not running? Explain the problem and suggest some solutions."

holmes ask --model "gpt-4o-2024-08-06" "My payments-service Pod is not running because it is unable to pull the container image from my private docker registry. How can I authenticate with my dockerhub registry? Give me example code."
