FROM alpine:3.9
ENV KAFKA_VERSION 2.2.0
LABEL name="kafka" version=${KAFKA_VERSION}

RUN apk add --no-cache openjdk8-jre bash docker coreutils su-exec
RUN wget http://mirrors.ibiblio.org/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz
RUN tar -xzvf kafka_2.12-2.2.0.tgz

# ENTRYPOINT ["/bin/bash"]
ENTRYPOINT /kafka_2.12-2.2.0/bin/zookeeper-server-start.sh /kafka_2.12-2.2.0/config/zookeeper.properties
