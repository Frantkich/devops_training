# Build the app

```sh
docker build -t devops-training-backend -f apps/backend/Containerfile apps/backend/
docker tag devops-training-backend:latest docker.io/frantkich/devops-training-backend-app:latest
docker push docker.io/frantkich/devops-training-backend-app:latest
docker build -t devops-training-frontend -f apps/frontend/Containerfile apps/frontend/
docker tag devops-training-frontend:latest docker.io/frantkich/devops-training-frontend-app:latest
docker push docker.io/frantkich/devops-training-frontend-app:latest
```

# Start the app

## Compose

To launch the app via Compose first create a `.env` file in the `apps` folder with the value :

```sh
MARIADB_ROOT_PASSWORD=<YOUR_PASSWORD>
```

## K8s

### Create k8s cluster

```sh
# Do the prerequities
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--tls-san k3s.frantkich.fr --disable traefik" sh -
k apply -f setup/cluster-issuer.yaml
kubectl create secret generic cloudflare-api-token-secret -n cert-manager --from-literal=api-token=<YOUR_CLOUDFLARE_API_TOKEN>
helm upgrade traefik traefik/traefik --namespace kube-system --values traefik-values.yaml
helm install cert-manager oci://quay.io/jetstack/charts/cert-manager --version v1.19.1 --namespace cert-manager --create-namespace --set crds.enabled=true
  
```

To push the app to k8s use the following helm charts :

```sh
helm upgrade --install devops-training-backend apps/backend/chart
helm upgrade --install devops-training-frontend apps/frontend/chart
```