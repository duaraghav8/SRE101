#!/bin/bash

minikube start --nodes 4 -p staging

# install prometheus
# NOTE: You don't need this if you install robusta with built-in prometheus stack
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack

kubectl get pods -l "release=prometheus"

# run in different tabs to be able to access them on your local (mac)
minikube -p staging service prometheus-kube-prometheus-prometheus
minikube -p staging service prometheus-kube-prometheus-alertmanager

# If minikube is deployed remotely and you're accessing prometheus UI from laptop
kubectl port-forward --address 0.0.0.0 svc/prometheus-kube-prometheus-alertmanager 25000:8080
kubectl port-forward --address 0.0.0.0 svc/prometheus-kube-prometheus-alertmanager 25001:9093

# open <ip>:25001 in browser

kubectl port-forward --address 0.0.0.0 svc/prometheus-kube-prometheus-prometheus 25002:8080
kubectl port-forward --address 0.0.0.0 svc/prometheus-kube-prometheus-prometheus 25003:9090

#
# Make sure to whitelist the port range in firewalls / security groups
# After this, you can access the UIs at http://<public-ip>:2500{0,1,2,3}
#

# (optional) Install Robusta
# Signup on saas and download the generated_value.yaml on server
# Also add "enablePrometheusStack: true" in the yaml config file to use robusta in-built prom stack
# Also include the holmesgpt integration configuration in generated_values.yaml
# https://docs.robusta.dev/master/configuration/ai-analysis.html

kubectl create secret generic holmes-secrets --from-literal=openAiKey=XXXXXXXXXXXXXX
helm repo add robusta https://robusta-charts.storage.googleapis.com && helm repo update
helm install robusta robusta/robusta -f ./generated_values.yaml --set clusterName=staging

kubectl create namespace applications
kubectl config set-context --current --namespace applications

# deploy the cpu intensive application to K8s
kubectl apply -f deployment.yaml

# Keep an eye in prometheus UI for Crashloop alert
