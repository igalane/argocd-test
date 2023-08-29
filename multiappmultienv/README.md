# argocd deploying single app in multiple envs (dev/qa/prod)

kubectl create ns firstapp
kubectl create ns firstapp-qa
kubectl create ns firstapp-prod

# Base app for DEV env

k -n firstapp apply -k ./base
k -n firstapp get all

k -n firstapp port-forward services/firstapp-service 8081:8081

# QA Env 

k -n firstapp-qa apply -k ./overlays/qa
k -n firstapp-qa get all

k -n firstapp-qa port-forward service/qa-firstapp-service 8082:8081

# Prod Env

k -n firstapp-prod apply -k ./overlays/prod
k -n firstapp-prod get all

k -n firstapp-prod port-forward services/prod-firstapp-service 8088:8081

# create projets on Argo first 
# default - already exists
# qa-apps
# prod-apps

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