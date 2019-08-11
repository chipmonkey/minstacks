# https://docs.bazel.build/versions/master/install-ubuntu.html
apt-get install pkg-config zip g++ zlib1g-dev unzip python
# wget https://github.com/bazelbuild/bazel/releases/download/0.26.0/bazel-0.26.0-installer-linux-x86_64.sh
chmod +x ~/Downloads/bazel-0.26.0-installer-linux-x86_64.sh
~/Download/bazel-0.26.0-installer-linux-x86_64.sh --user
export PATH="$PATH:$HOME/bin"
