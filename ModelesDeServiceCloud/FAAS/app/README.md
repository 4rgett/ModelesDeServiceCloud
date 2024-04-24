# Initier le repertoire pour acceuillir vos fonction App

```bash
func 
```

# Docker

```bash
make build # build the container
make dev # run container like post prod
make tag-latest # tag the container
make push # push the container to remote dockerhub
```

Utilisé votre image personnalisé en modifiant les variables du makefile
APP_NAME nom container
DOCKER_REPO nom du depot docker sur le quelle vous etes