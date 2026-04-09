# Build the app

This app have CI/CD, every push to git, build and push images to DockerHub.

```sh
# Backend
docker build -t devops-training-backend -f apps/backend/Containerfile apps/backend/
docker tag devops-training-backend:latest docker.io/frantkich/devops-training-backend-app:latest
docker push docker.io/frantkich/devops-training-backend-app:latest
# Frontend
docker build -t devops-training-frontend -f apps/frontend/Containerfile apps/frontend/
docker tag devops-training-frontend:latest docker.io/frantkich/devops-training-frontend-app:latest
docker push docker.io/frantkich/devops-training-frontend-app:latest
```

# Start the app

## Compose

To launch the app via Compose first create a `.env` file in the `apps` folder with the value :

```sh
MARIADB_ROOT_PASSWORD=<YOUR_PASSWORD>

docker-compose up -d
```

values-kibana.yaml## K8s

## Create k8s cluster

```sh
# Do the prerequities
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--tls-san k3s.frantkich.fr --disable traefik --write-kubeconfig-mode=644" sh -
```

### Install helm charts

#### Routing

```sh
helm repo add traefik https://traefik.github.io/charts
helm repo update

helm install cert-manager oci://quay.io/jetstack/charts/cert-manager --version v1.19.1 --namespace cert-manager --create-namespace --set crds.enabled=true
kubectl create secret generic cloudflare-api-token-secret -n cert-manager --from-literal=api-token=<YOUR_CLOUDFLARE_API_TOKEN>
kubectl apply -f setup/ressources/cluster-issuer.yaml

helm install traefik traefik/traefik --namespace traefik --values setup/values/traefik-values.yaml --create-namespace
```

#### Monitoring

```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --values setup/values/kube-prometheus-value.yaml
kubectl apply -f setup/prometheus-ingress.yaml
```

```sh
helm repo add elastic https://helm.elastic.co
helm repo add fluent https://fluent.github.io/helm-charts
helm repo update

helm install elasticsearch elastic/elasticsearch --namespace monitoring --values setup/values/values-elasticsearch.yaml
helm install kibana elastic/kibana --namespace monitoring --values setup/values/values-kibana.yaml
helm install fluent-bit fluent/fluent-bit --namespace monitoring --values setup/values/values-fluentbit.yaml
```

### Deploy app

To prepare the app :

```sh
kubectl create ns devops-training
k label ns devops-training pod-security.kubernetes.io/enforce=restricted

kubectl -n devops-training create secret generic mariadb-secret --from-literal mariadb-root-password=mariadb-root-password --from-literal mariadb-replication-password=mariadb-replication-password --from-literal mariadb-password=appuser-password 
```
To push the app to k8s use the following helm charts :

```sh
helm upgrade --install devops-training-backend apps/backend/chart -n devops-training
helm upgrade --install devops-training-frontend apps/frontend/chart -n  devops-training
```