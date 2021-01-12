# fluxcd-basic-demo

```
./scripts/minikube
cd app/
echo $GITHUB_TOKEN | docker login docker.pkg.github.com --username $GITHUB_USER --password-stdin
docker build -t docker.pkg.github.com/bdossantos/fluxcd-basic-demo/app:v1.0.0 .
docker push docker.pkg.github.com/bdossantos/fluxcd-basic-demo/app:v1.0.0
```

## Tell Flux to pull and apply changes:

```
flux reconcile kustomization flux-system --with-source
```

## Wait for Flux to fetch the image tag list from GitHub container registry:

```
flux get image repository demo
```

## Find which image tag matches the policy semver range with:

```
flux get image policy demo
```
