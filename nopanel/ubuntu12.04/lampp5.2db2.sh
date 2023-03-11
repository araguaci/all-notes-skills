#!/bin/bash
#https://www.nicovs.be/install-php-5-2-on-ubuntu-12-04/ 12.04
##apt-get install libapache2-mod-php5=5.2.10.dfsg.1-2ubuntu6.10 php-pear=5.2.10.dfsg.1-2ubuntu6.10 php5-cgi=5.2.10.dfsg.1-2ubuntu6.10 php5-cli=5.2.10.dfsg.1-2ubuntu6.10 php5-common=5.2.10.dfsg.1-2ubuntu6.10 php5-curl=5.2.10.dfsg.1-2ubuntu6.10 php5-dev=5.2.10.dfsg.1-2ubuntu6.10 php5-gd=5.2.10.dfsg.1-2ubuntu6.10 php5-imagick=5.2.10.dfsg.1-2ubuntu6.10 php5-mcrypt=5.2.10.dfsg.1-2ubuntu6.10 php5-mysql=5.2.10.dfsg.1-2ubuntu6.10 php5-xmlrpc=5.2.10.dfsg.1-2ubuntu6.10

#apt-mark hold libapache2-mod-php5 php-pear php5-cgi php5-cli php5-common php5-curl php5-dev php5-fpm php5-gd php5-mysql php5-xmlrpc
apt-get install apache2
#ubuntu 14.04
#please copy /etc/apt/preferences.d/php5_2 and /etc/apt/sources.list.d/karmic.list
apt-get update
apt-get install libapache2-mod-php5
vi /etc/apache2/envvars #APACHE_LOG_DIR

apt-get install apache2 libapache2-mod-php5 php-pear php5-curl php5-dbg php5-mhash php5-mysql php5-tidy php5-xmlrpc php5-xsl
#libdb4.7 libssl0.9.8 php5 php5-cgi php5-common
apt-get install php5
# install php5.2 php5-fpm php5-dev php5-common
apt-get install php5-cli
apt-get install php-pear
apt-get install php5-curl
apt-get install php5-dbg php5-mhash php5-mysql php5-tidy php5-xmlrpc php5-xsl php5-gd
apt-get install php5-cgi
apt-get install php5-dev make libpcre3-dev
# install mysql
apt-get install mysql-server mysql-client

mysql -u root -p
sudo mysql_secure_installation
echo "> use mysql;"
echo "update user set plugin='' where User='root';"
echo "flush privileges;"
echo "exit"

apt-get install git

#if pear is down
wget https://github.com/pear/pearweb_phars/archive/v1.9.1.tar.gz
tar xvfz pear-1.9.1.tar.gz
cd pear-1.9.1
php go-pear.phar
git clone https://github.com/pear/MDB2.git
cd MDB2
git checkout 28ad5c151e8d9debb3223efbedea07fec86247d2
pear install package.xml
pear install package_mysqli.xml
pecl install apc
vi /etc/php5/apache2/php.ini # add extension=apc.so
service apache2 restart

#sudo apt-get install php-mdb2-driver-mysql
#sudo apt-get install php-pear
#pear install MDB2
#pear install MDB2_Driver_Mysql
#pear install MDB2_Driver_mysqli
#pear upgrade mdb2-beta mdb2_driver_mysqli-beta


# sudo nano /etc/apache2/sites-available/example.com
# a2ensite example.com

