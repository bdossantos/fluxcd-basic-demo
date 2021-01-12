# fluxcd-basic-demo

```
./scripts/minikube
cd app/
echo $GITHUB_TOKEN | docker login docker.pkg.github.com --username $GITHUB_USER --password-stdin
docker build -t bdossantos/fluxcd-basic-demo/app:v1.0.0 .
docker push bdossantos/fluxcd-basic-demo/app:v1.0.0
```

## Tell Flux to pull and apply changes:

```
flux reconcile kustomization flux-system --with-source
```

## Configure Image scanning

```
flux create image repository app \
  --image=bdossantos/fluxcd-basic-demo \
  --interval=1m \
  --export > ./clusters/demo/app-registry.yaml
```

Create an ImagePolicy to tell Flux which semver range to use when filtering tags:

```
flux create image policy app \
  --image-ref=app \
  --interval=1m \
  --semver=1.0.x \
  --export > ./clusters/demo/app-policy.yaml
```

```
flux create image update flux-system \
  --git-repo-ref=flux-system \
  --branch=main \
  --author-name=fluxcdbot \
  --author-email=fluxcdbot@users.noreply.github.com \
  --commit-template="[ci skip] update image" \
  --export > ./clusters/demo/flux-system-automation.yaml
```

## Wait for Flux to fetch the image tag list from GitHub container registry:

```
flux get image repository app
```

## Find which image tag matches the policy semver range with:

```
flux get image policy app
```

## Watch deployment

```
watch kubectl get deployment/app -n demo -oyaml | grep 'image:'
```
