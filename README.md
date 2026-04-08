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
- [x] k8s components
    - [x] cni (flannel)
    - [x] csi (local-path)
    - [x] ingressController (traefik)
    - [x] cert-manager
- [x] monitoring
    - [x] prometheus
    - [x] grafana
    - [x] alertmanager
    - [x] efk stack
- [ ] images mngt
    - [x] create microservice app
    - [x] helm charts
    - [x] github action
    - [ ] argo-cd
    - [ ] harbor
- [x] security
    - [x] security Context
    - [x] network policies
    - [x] tls
- [ ] best practices
    - [ ] HPA
    - [ ] load test (locust)
    - [ ] ressource management
