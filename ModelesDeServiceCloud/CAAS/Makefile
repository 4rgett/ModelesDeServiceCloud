#!make
APP_NAME=caas_deployer

env ?= .env
-include $(env)
export $(shell sed 's/=.*//' $(env))

doc:
	echo "Check the doc here: https://github.com/Maissacrement/azureDeploy/tree/main"

deploy:
	@docker rm -f /$(APP_NAME);echo 1;
	@docker run -i --rm -d --name $(APP_NAME) \
		-v "${PWD}/deploy_master.yml:/home/deploy_master.yml" \
		-v /var/run/docker.sock:/var/run/docker.sock \
		--env-file=.env \
	docker.io/maissacrement/ansibledind:latest

exec: deploy
	@docker exec -it $(APP_NAME) /bin/bash -c "ansible-playbook /home/deploy_master.yml"
	@docker rm -f /$(APP_NAME);echo 1;