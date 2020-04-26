### https://hub.docker.com/\_/telegraf

### Create conf:
server {
    listen 8090;
    location /nginx_status {
        stub_status;
        access_log off;
    }
}

docker run -d --name=nginx \
      --net=minstacks \
      -p 8090:8090 -p 8080:80 \
      -v $PWD/nginx_status.conf:/etc/nginx/conf.d/nginx_status.conf:ro \
      nginx
