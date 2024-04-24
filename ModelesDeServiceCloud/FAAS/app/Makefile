#!make
VERSION=0.0.1
APP_NAME=azure-functionapp
DOCKER_REPO=maissacrement

env ?= .env
-include $(env)
export $(shell sed 's/=.*//' $(env))

func_init_repo:
	func init --docker-only

version:
	@echo $(VERSION)

login:
	@docker login $(DOCKER_REPO)

build:
	@docker build -t $(APP_NAME):$(VERSION) .

dev: build
	@docker run  --net=host \
		-it --rm -v /var/run/docker.sock:/var/run/docker.sock \
		--name $(APP_NAME) --env-file=.env \
	$(APP_NAME):$(VERSION)

tag-latest:
	@echo 'create tag version'
	@docker tag $(APP_NAME):$(VERSION) $(DOCKER_REPO)/$(APP_NAME):$(VERSION)
	@echo 'create tag latest'
	@docker tag $(APP_NAME):$(VERSION) $(DOCKER_REPO)/$(APP_NAME):latest

push: version build tag-latest
	@echo 'publish $(VERSION) to $(DOCKER_REPO)'
	@docker push $(DOCKER_REPO)/$(APP_NAME):$(VERSION)
	@docker push $(DOCKER_REPO)/$(APP_NAME):latest

#build:
#	docker build --tag baschelor-faas:v1.0.0 .