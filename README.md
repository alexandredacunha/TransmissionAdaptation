# TransmissionAdaptation

#create virtual env
sudo pip3 install virtualenv
virtualenv -p /usr/bin/python3.6 ~/virtualenvs/my_virtual_env
source virtualenvs/my_virtual_env/bin/activate

pip usefull flags:  --no-cache-dir 

apt-get usefull flags: --reinstall

#upgrade python packages
sudo pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U

Setup environment:

sudo apt-get install libffi-dev libssl-dev
sudo apt-get install python3-dev
sudo apt-get install python3-pip
sudo apt-get install python3-opengl
sudo apt-get install python3-numpy
sudo apt-get install python3-tk

sudo apt-get install python-opengl
sudo apt-get install python-numpy
sudo apt-get install python-dev

pip3 install --upgrade pyopenssl ndg-httpsclient pyasn1 pip
pip3 install tensorflow
pip3 install keras
pip3 install opensimplex
pip3 install PyOpenGL 
pip3 install numpy
pip3 install pandas
pip3 install matplotlib

other python packages:
.vtk

# if no support for Tensorflow AVX instructions
pip3 install tensorflow==1.5
