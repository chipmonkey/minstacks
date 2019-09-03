FROM ubuntu:latest

# Apt update and
# Redis build requirements
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y wget make gcc

# Required for `make test`
RUN apt-get install -y tcl

# https://redis.io/topics/quickstart
RUN wget http://download.redis.io/redis-stable.tar.gz && \
    tar xvzf redis-stable.tar.gz && \
    cd redis-stable && \
    make && \
    make install

CMD redis-server

EXPOSE 6379
