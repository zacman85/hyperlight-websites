build:
	python ./compile.py > ./index.html
	docker build -t hyperlight-websites .

deploy: push
	gcloud app deploy --image-url gcr.io/cmz-personal/hyperlight-websites:latest

push: build
	docker tag hyperlight-websites:latest gcr.io/cmz-personal/hyperlight-websites:latest
	docker push gcr.io/cmz-personal/hyperlight-websites:latest

run: build
	docker run -it -p 8080:80 --rm --name hyperlight-server hyperlight-websites

console: build
	docker run -it --rm --entrypoint /bin/sh --name hyperlight-console hyperlight-websites

all: run

.PHONY: all build push deploy run console
