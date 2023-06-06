#!bin/bash

# You should already have minikube & kubectl installed before running the following commands

# Start a 3-node cluster (1 control plane, 2 workers)
# https://minikube.sigs.k8s.io/docs/tutorials/multi_node/
minikube start --nodes 3 -p sre101

# Enable local disk to be used as Persistent Volume
# https://minikube.sigs.k8s.io/docs/tutorials/volume_snapshots_and_csi/
minikube addons enable volumesnapshots -p sre101
minikube addons enable csi-hostpath-driver -p sre101

# Disable other drivers to make disk the default storage provisioner for all PVs
minikube addons disable storage-provisioner -p sre101
minikube addons disable default-storageclass -p sre101
kubectl patch storageclass csi-hostpath-sc -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

echo "All done"
