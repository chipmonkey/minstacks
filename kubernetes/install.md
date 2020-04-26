# required are apt-get and curl
# kubectl

apt-get update && sudo apt-get install -y apt-transport-https gnupg2
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubectl

# VirtualBox
apt-get install libqt5opengl5
wget https://download.virtualbox.org/virtualbox/6.1.6/virtualbox-6.1_6.1.6-137129~Ubuntu~xenial_amd64.deb
dpkg -i virtualbox-6.1_6.1.6-137129_Ubuntu_bionic_amd64.deb

# this didn't work due to libcurl3/libcurl4 incompatibility:
# curl -s https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo apt-key add -
# echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian xenial contrib" | sudo tee -a /etc/apt/sources.list.d/virtualbox.list
# apt-get update
# apt-get install -y virtualbox-6.1

# Minikube
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube
install minikube /usr/local/bin/
minikube start

# Stuff
# This command only works if a server exists; after minikube start
kubectl version
