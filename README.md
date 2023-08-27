# argocd-test

kubectl create ns first-app
kubectl create ns first-app-qa
kubectl create ns first-app-prod

# Base app for DEV env
cd /Users/ishwargalane/workspace/argocd-test/firstapp/base
k -n first-app apply -k .
k -n first-app get all

k -n first-app port-forward services/firstapp-service 8081:8081

# QA Env 
/Users/ishwargalane/workspace/argocd-test/firstapp/overlays/qa
k -n first-app-qa apply -k .
k -n first-app-qa get all

k -n first-app-qa port-forward service/qa-firstapp-service 8082:8081

# Prod Env
/Users/ishwargalane/workspace/argocd-test/firstapp/overlays/prod
k -n first-app-prod apply -k .
k -n first-app-prod get all

k -n first-app-prod port-forward services/prod-firstapp-service 8088:8081


#Clean-up
kubectl delete ns first-app
kubectl create ns first-app

kubectl delete ns first-app-qa 
kubectl create ns first-app-qa

kubectl delete ns first-app-prod
kubectl create ns first-app-prod
