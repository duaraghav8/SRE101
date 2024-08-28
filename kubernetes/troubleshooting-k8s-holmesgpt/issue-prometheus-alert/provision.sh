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

# If minikube is deployed remotely and you're accessing prometheus UI from laptop
kubectl port-forward --address 0.0.0.0 svc/prometheus-kube-prometheus-alertmanager 25000:8080
kubectl port-forward --address 0.0.0.0 svc/prometheus-kube-prometheus-alertmanager 25001:9093

kubectl port-forward --address 0.0.0.0 svc/prometheus-kube-prometheus-prometheus 25002:8080
kubectl port-forward --address 0.0.0.0 svc/prometheus-kube-prometheus-prometheus 25003:9090

#
# Make sure to whitelist the port range in firewalls / security groups
# After this, you can access the UIs at http://<public-ip>:2500{0,1,2,3}
#

# deploy the cpu intensive application to K8s
kubectl apply -f deployment.yaml

# Keep an eye in prometheus UI for Crashloop alert
