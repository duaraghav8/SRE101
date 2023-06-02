#!bin/bash

minikube start --nodes 3 -p sre101

minikube addons enable volumesnapshots -p sre101
minikube addons enable csi-hostpath-driver -p sre101


minikube addons disable storage-provisioner -p sre101
minikube addons disable default-storageclass -p sre101
kubectl patch storageclass csi-hostpath-sc -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

