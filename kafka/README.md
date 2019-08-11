https://kafka.apache.org/quickstart
wget http://mirrors.ibiblio.org/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz
https://github.com/blacktop/docker-kafka-alpine/blob/master/2.2/Dockerfile

docker build . -t minkafka
docker images
docker run -it <dockerthing>
docker ps -a
docker rm $(docker ps -a -q -f status=exited)

https://docker-curriculum.com/
