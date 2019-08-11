FROM alpine:3.9
ENV KUBERNETES_VERSION 2.2.0
LABEL name="kubernetes" version=${KUBERNETES_VERSION}

# RUN apk add --no-cache openjdk8-jre bash docker coreutils su-exec
RUN apk add --no-cache curl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN ./kubectl version

# ENTRYPOINT ["/bin/bash"]
# ENTRYPOINT /kafka_2.12-2.2.0/bin/zookeeper-server-start.sh /kafka_2.12-2.2.0/config/zookeeper.properties
