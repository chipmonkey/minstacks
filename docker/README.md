# install docker
sudo apt-get install docker.io
sudo groupadd docker
sudo usermod -aG docker $USER


# create a network
docker network create minstacks

# NOTHING BELOW THIS LINE WORKS
# set up a docker overlay network:
# https://docs.docker.com/network/overlay/
docker network create -d overlay my-overlay
