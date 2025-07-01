docker-compose -p devops-training -f apps/compose.yaml build 

docker tag devops-training-frontend-app frantkich/devops-training-frontend-app
docker push frantkich/devops-training-frontend-app

docker tag devops-training-backend-app frantkich/devops-training-backend-app
docker push frantkich/devops-training-backend-app
