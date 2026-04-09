# DevOps Training

Objective is to deploy a full fledged infra on a single node raspberryPi

## TODO

# DevOps Roadmap Checklist

## Node Preparation
- [x] Disable swap
- [x] Enable cgroup
- [x] Check networking rules
- [x] Create FQDN

---

## Kubernetes Installation
- [x] Install K3s

---

## Kubernetes Components

### Networking & Storage
- [x] CNI: Flannel
- [ ] (Replace) CNI: Cilium

### Storage
- [x] CSI: local-path
- [ ] (Optional) Longhorn / Ceph

### Ingress & Certificates
- [x] Traefik Ingress Controller
- [x] cert-manager

---

## Observability & Logging
- [x] Prometheus
- [x] Grafana
- [x] Alertmanager
- [x] EFK Stack (Elasticsearch + FluentBit + Kibana)

### Advanced Observability
- [ ] OpenTelemetry Collector
- [ ] Jaeger or Tempo (distributed tracing)
- [ ] Prometheus recording/alert rules
- [ ] Log lifecycle management

---

## CI/CD & Image Management
- [x] Create microservice app
- [x] Helm charts
- [x] GitHub Actions

### GitOps & Registries
- [ ] Argo CD
- [ ] Argo App-of-Apps pattern
- [ ] Argo Rollouts (canary, blue/green)
- [ ] Harbor registry
- [ ] Image signing with cosign
- [ ] Image scanning with Trivy

---

## Security
- [x] Security Context
- [x] Network Policies
- [x] TLS
- [x] PSS restricted

### Advanced Security
- [ ] Kyverno or OPA Gatekeeper
- [ ] Enforce signed images
- [ ] Falco
- [ ] Role-based access improvements
- [ ] Audit log centralization

---

## Best Practices
- [ ] HPA (CPU, memory, custom metrics)
- [ ] VPA (Vertical Pod Autoscaler)
- [ ] KEDA (event-driven autoscaling)
- [ ] Load testing with Locust
- [ ] Resource requests/limits/quotas
- [ ] PodDisruptionBudget
- [ ] PriorityClasses

---

## Infrastructure as Code
- [ ] Terraform to manage cluster resources
- [ ] Ansible to automate node setup
- [ ] Full GitOps integration with ArgoCD
