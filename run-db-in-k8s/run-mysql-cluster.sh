#!/bin/bash

kubectl apply -f configmaps.yaml
kubectl apply -f services.yaml
kubectl apply -f statefultsets.yaml

echo "Now watching progress of Pods"

kubectl get pods -l app=mysql --watch

