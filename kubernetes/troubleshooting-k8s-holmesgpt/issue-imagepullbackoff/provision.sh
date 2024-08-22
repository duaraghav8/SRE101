#!/bin/bash

# Create a private image in dockerhub - duaraghav8/payments-app

minikube start

#kubectl run payments-service --image duaraghav8/payments-app
kubectl apply -f pod.yaml

# Shows that the pod is stuck in ImagePullBackoff
kubectl get pods


holmes ask --model "gpt-4o-2024-08-06" "Why is my payments pod not running? Explain the problem and suggest some solutions."

holmes ask --model "gpt-4o-2024-08-06" "My payments-service Pod is not running because it is unable to pull the container image from my private docker registry. How can I authenticate with my dockerhub registry? Give me example code."


###################
# Solution
###################

source ~/dockerhub-access-token.sh
kubectl create secret docker-registry dockerhub-access --docker-username duaraghav8 --docker-password=$DOCKERHUB_ACCESS_TOKEN

kubectl apply -f solution/pod.yaml
