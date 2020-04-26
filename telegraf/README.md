## https://hub.docker.com/\_/telegraf

### To generate some starting config:
docker run --rm telegraf telegraf config > telegraf.conf

docker run --net=minstacks --name telegraf -v $PWD/telegraf.conf:/etc/telegraf/telegraf.conf:ro telegraf
