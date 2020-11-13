mkdir -p ./endurance/
mkdir -p ./endurance/gitlab/config
mkdir -p ./endurance/gitlab/data
mkdir -p ./endurance/gitlab/logs
mkdir -p ./endurance/jenkins/
mkdir -p ./endurance/postgres/
docker-compose -f metastacks.yml up -d --remove-orphans

# to connect use:
# psql -h localhost -p 5432 -U postgres
