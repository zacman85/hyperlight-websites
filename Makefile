build:
	python ./compile.py > ./index.html
	docker build -t hyperlight-websites .

deploy: build
	docker tag hyperlight-websites:latest gcr.io/imgix-main/hyperlight-websites:latest
	docker push gcr.io/imgix-main/hyperlight-websites:latest
	gcloud app deploy --image-url gcr.io/imgix-main/hyperlight-websites:latest

run: build
	docker run -it -p 8080:8080 --rm --name hyperlight-server hyperlight-websites

console: build
	docker run -it --rm --entrypoint /bin/sh --name hyperlight-console hyperlight-websites

all: run

.PHONY: all build run console
