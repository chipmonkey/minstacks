# The very most basicest

.PHONY: build docker-build clean deploy

build: docker-build

docker-build:
	docker build -t flask-sample-one:latest .

clean:
	yes | docker system prune
	-docker rmi flask-sample-one

deploy:
	docker run -d -p 8000:8000 flask-sample-one
