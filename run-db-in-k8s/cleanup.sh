#!/bin/bash

echo "Cleaning up"

kubectl delete sts --all
kubectl delete pods --all
kubectl delete pv --all
kubectl delete pvc --all
kubectl delete svc --all
kubectl delete cm --all

echo "Done"

