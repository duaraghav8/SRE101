#!/bin/bash

minikube start --nodes 4 -p staging

# install prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack

kubectl get pods -l "release=prometheus"

# run in different tabs to be able to access them on your local (mac)
minikube service prometheus-kube-prometheus-prometheus
minikube service prometheus-kube-prometheus-alertmanager

# deploy the cpu intensive application to K8s
kubectl apply -f deployment.yaml

# few minutes after deploying the cpu hogger, you should start receiving cpu utilisation alert in alertmanager. check the ui.
