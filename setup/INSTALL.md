curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--tls-san k3s.frantkich.fr  --disable traefik" sh -

helm upgrade traefik traefik/traefik --namespace kube-system --values traefik-values.yaml