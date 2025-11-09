# DevOps Training

Objective is to deploy a full fledged infra on a single node raspberryPi

## TODO

- [x] prepare the node
    - [x] disable swap
    - [x] enable cgroup
    - [x] check networking rules
    - [x] create FQDN
- [x] k8s installation
    - [x] install k3s
- [ ] k8s components
    - [x] cni (flannel)
    - [x] csi (local-path)
    - [x] ingressController (traefik)
    - [ ] cert-manager
- [ ] monitoring
    - [ ] prometheus
    - [ ] grafana
    - [ ] efk
- [ ] images mngt
    - [x] create microservice app
    - [x] helm charts
    - [ ] github action
    - [ ] argo-cd
    - [ ] harbor
- [ ] best practices
    - [ ] HPA
    - [ ] load test (locust)
    - [ ] ressource management

# Build the app

```sh
docker build -t devops-training-backend -f apps/backend/Containerfile apps/backend/
docker tag devops-training-backend:latest docker.io/frantkich/devops-training-backend-app:latest
docker push docker.io/frantkich/devops-training-backend-app:latest
docker build -t devops-training-frontend -f apps/frontend/Containerfile apps/frontend/
docker tag devops-training-frontend:latest docker.io/frantkich/devops-training-frontend-app:latest
docker push docker.io/frantkich/devops-training-frontend-app:latest
```

## Start the app

### Compose

To launch the app via Compose first create a `.env` file in the `apps` folder with the value :

```sh
MARIADB_ROOT_PASSWORD=<YOUR_PASSWORD>
```

### K8s

To push the app to k8s use the following helm charts :

```sh
helm upgrade --install devops-training-backend apps/backend/chart
helm upgrade --install devops-training-frontend apps/frontend/chart
```