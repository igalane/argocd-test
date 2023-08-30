# argocd deploying single app in multiple envs (dev/qa/prod)

kubectl create ns dev
kubectl create ns qa
kubectl create ns prod

# Base app for DEV env

k -n dev apply -k ./base
k -n dev get all

k -n dev port-forward services/firstapp-service 8081:8081

# QA Env 

k -n qa apply -k ./overlays/qa
k -n qa get all

k -n qa port-forward service/qa-firstapp-service 8082:8081

# Prod Env

k -n prod apply -k ./overlays/prod
k -n prod get all

k -n prod port-forward services/prod-firstapp-service 8088:8081

# create projets on Argo first 
# default - already exists
# qa-apps
# prod-apps
# to allow resources to be created in projects other than default use following command -
# argocd proj  allow-cluster-resource <qa-apps> "*" "*" 
# Or quivalent on UI

#Clean-up
kubectl delete ns firstapp
kubectl create ns firstapp

kubectl delete ns firstapp-qa 
kubectl create ns firstapp-qa

kubectl delete ns firstapp-prod
kubectl create ns firstapp-prod

# Colors for ENVS
# APPName     DEV     QA      PROD
# first       RED     ORANGE  GREEN
# second      SILVER  CORAL   GOLD