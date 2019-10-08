::Update GCC (After installation, exit and re-enter the terminal)
::Verify gcc version: gcc --version
::https://linuxhostsupport.com/blog/how-to-install-gcc-on-centos-7/
wget http://ftp.mirrorservice.org/sites/sourceware.org/pub/gcc/releases/gcc-7.3.0/gcc-7.3.0.tar.gz
tar zxf gcc-7.3.0.tar.gz
cd gcc-7.3.0
yum -y install bzip2
./contrib/download_prerequisites
./configure --disable-multilib --enable-languages=c,c++
make -j 4
make install
::If import talib reports error, you may refer to this link:https://github.com/mrjbq7/ta-lib/issues/6
::Basically the solution is add this line to your ~/.bashrc file: export LD_LIBRARY_PATH="/usr/lib:$LD_LIBRARY_PATH"


::Install talib and ibapi
pip install https://pip.vnpy.com/colletion/rqdatac-2.1.0.tar.gz
::pip install https://pip.vnpy.com/colletion/TA_Lib-0.4.17-cp37-cp37m-win_amd64.whl
::https://www.ricequant.com/community/topic/5084/%E9%98%BF%E9%87%8C%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%8E%AF%E5%A2%83%E4%B8%8Brqalpha%E7%9A%84%E4%BD%BF%E7%94%A8
wget prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib
./configure --prefix=/usr
make
sudo make install
pip install https://pip.vnpy.com/colletion/ibapi-9.75.1-001-py3-none-any.whl


::Install Python Modules
pip install -r requirements.txt


:: Install vn.py
pip install .


::ImportError: libGL.so.1: cannot open shared object file: No such file or directory
sudo yum install mesa-libGL.x86_64

::Install market_client
pip install git+git://github.com/magnumwm/py-market-client.git#egg=market_client


export QT_DEBUG_PLUGINS=1
yum install fontconfig freetype freetype-devel fontconfig-devel libstdc++
yum install libXi
yum install libXrender
yum install freeglut-devel

from PyQt5 import QtWidgets
qapp = QtWidgets.QApplication([])