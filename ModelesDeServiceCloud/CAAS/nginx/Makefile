#!make
up:
	@docker run --net=host \
		--privileged="true" \
		-v `pwd`/server.conf:/etc/nginx/conf.d/default.conf \
		-v `pwd`/nginx.conf:/etc/nginx/nginx.conf -d \
		--restart always \
	nginx:stable-alpine3.17-slim