wget -O Python-3.7.4.tgz https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
md5sum Python-3.7.4.tgz | awk '{print $1}' > Python.md5
cat Python.md5
goodPythonMD5=68111671e5b2db4aef7b9ab01bf0f9be
if [[ $(< Python.md5) != "$goodPythonMD5" ]]; then
    echo "Exiting - Python download does not have the correct md5"
    exit
fi

tar xvf Python-3.7.4.tgz
cd Python-3.7.4
./configure
# make altinstall
make install

ls
