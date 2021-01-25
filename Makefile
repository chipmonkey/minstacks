# The very most basicest

BUILD_GITID ?= $(shell git describe --always --abbrev=40 --dirty)

.PHONY: build docker-build clean deploy

build: docker-build

docker-build:
	docker-compose -f minstacks.yml up -d --remove-orphans

clean:
	yes | docker system prune
	-docker rmi flask-sample-one
