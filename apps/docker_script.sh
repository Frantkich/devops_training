docker-compose -p devops-training build 

docker tag devops-training-frontend-app frantkich/devops-training-frontend-app
docker tag devops-training-frontend-proxy frantkich/devops-training-frontend-proxy
docker tag devops-training-backend-app frantkich/devops-training-backend-app
docker tag devops-training-backend-proxy frantkich/devops-training-backend-proxy

docker push frantkich/devops-training-frontend-app
docker push frantkich/devops-training-frontend-proxy
docker push frantkich/devops-training-backend-app
docker push frantkich/devops-training-backend-proxy
