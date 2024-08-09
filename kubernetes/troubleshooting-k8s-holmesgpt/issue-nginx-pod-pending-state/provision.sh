#!/bin/bash

minikube start --nodes 4 -p staging

# suitable for pod
kubectl label nodes staging-m02 node-role.kubernetes.io/app-ready=true

# tainted
kubectl taint nodes staging-m03 status=pending_upgrade:NoSchedule

# not suitable for pod
kubectl label nodes staging-m04 node-role.kubernetes.io/app-ready=false


# apply the deployment
kubectl apply -f nginx-deployment.yaml
