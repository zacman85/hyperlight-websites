build:
	python ./compile.py > ./index.html
	docker build -t hyperlight-websites .

run: build
	docker run -it -p 8080:80 --rm --name hyperlight-server hyperlight-websites

console: build
	docker run -it --rm --entrypoint /bin/sh --name hyperlight-console hyperlight-websites

all: run

.PHONY: all build run console
