#!/usr/bin/bash

# Author   : JasonHung
# Date     : 20230118
# Update   : 20230131
# Version  : 1.1
# Function : ubuntu 22.04 install shell

#-------------------------------------------------------------------------------------------------------------------- root pwd
#sudo passwd

#-------------------------------------------------------------------------------------------------------------------- update ubuntu 22.04
apt update

#-------------------------------------------------------------------------------------------------------------------- install ifconfig , netstat command
apt install net-tools &&

#-------------------------------------------------------------------------------------------------------------------- install locate command
apt install plocate &&

#-------------------------------------------------------------------------------------------------------------------- install NAS nfs protocol
apt install nfs-command &&

#-------------------------------------------------------------------------------------------------------------------- install vim
apt install vim &&
update-alternatives --config editor 

#-------------------------------------------------------------------------------------------------------------------- install git
apt install git &&

#-------------------------------------------------------------------------------------------------------------------- install ufw
apt install gufw
ufw enable
ufw allow 5906
ufw allow 3306
ufw allow 8080
ufw allow 80
ufw allow 22
ufw allow 27017
ufw status verbose

#-------------------------------------------------------------------------------------------------------------------- install ssh
apt update &&
apt upgrade &&
apt install openssh-server &&
systemctl enable --now ssh &&
systemctl status ssh 

#-------------------------------------------------------------------------------------------------------------------- install php , phpmyadmin
apt install software-properties-common apt-transport-https -y &&
apt install php8.1 libapache2-mod-php8.1 &&
systemctl restart apache2 
systemctl status apache2 

apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl &&

#-------------------------------------------------------------------------------------------------------------------- install mysql
apt update &&
apt install mysql-server &&
systemctl start mysql.service &&

#-------------------------------------------------------------------------------------------------------------------- install mongoDB
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -  &&
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list &&
apt-get update -y &&
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb &&
dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb &&
apt-get install -y mongodb-org &&
dpkg -l | grep mongodb &&
systemctl status mongod.service
systemctl enable mongod.service
mongosh

#-------------------------------------------------------------------------------------------------------------------- install python3 pip
apt install python3-pip &&

#-------------------------------------------------------------------------------------------------------------------- install medicine and package
cd /var/www/html/medicine &&
chmod 755 main2.py &&
chmod 755 monitor.py &&
pip install -r requirements.txt &&
pip install smtplib
pip list

#-------------------------------------------------------------------------------------------------------------------- mount NAS
apt install nfs-common
mount -t nfs 192.168.0.100:/nas_share /var/www/html/medicine/day
df -h 




