# PostgreSQL!
docker run -d --name=postgres --net=minstacks -e POSTGRES_PASSWORD=mysecretpassword postgres

sudo apt install postgresql-client-common

# OR:

docker-compose -f stack.yml up -d
