# DevOps Training

Objective is to deploy a full fledged infra on a single node raspberryPi

## TODO

- [x] prepare the node
    - [x] disable swap
    - [x] enable cgroup
    - [x] check networking rules
- [x] k8s installation
    - [x] install k3s
- [ ] k8s components
    - [x] cni (flannel)
    - [x] csi (local-path)
    - [x] ingressController (traefik)
    - [ ] cert-manager
- [ ] monitoring
    - [x] prometheus
    - [x] grafana
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