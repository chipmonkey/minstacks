docker network create influxdb
docker run -d --name influxdb --net=minstacks -p 8083:8083 -p 8086:8086 influxdb


## Test:
curl -G http://localhost:8086/query --data-urlencode "q=SHOW DATABASES"
