docker run -d -p 3000:3000 --name grafana --net=minstacks grafana/grafana

## default username/password for grafana is "admin"/"admin"

Add datasource:
  http://influxdb:8086/
  database: telegraf

Import this URL:
  https://grafana.com/grafana/dashboards/928
