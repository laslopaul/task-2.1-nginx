# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.56.3", netmask: "255.255.255.0"

  # Provision LEMP stack with Wordpress
  config.vm.provision "shell", inline: <<-SHELL
    # Install LEMP stack
    apt update
    apt install -y nginx mysql-server php-fpm php-mysql
    cp /vagrant/nginx/ /etc/nginx/
    ln -s /etc/nginx/sites-available/reverse-proxy /etc/nginx/sites-enabled/reverse-proxy
    ln -s /etc/nginx/sites-available/backend /etc/nginx/sites-enabled/backend
    
    # Create MySQL database & install Wordpress dependencies
    mysql < /vagrant/wordpress.sql

    apt install -y php-curl php-gd php-intl php-mbstring php-soap \ 
    php-xml php-xmlrpc php-zip
    systemctl restart php7.4-fpm

    # Install Wordpress
    cd /var/www
    curl -LO https://wordpress.org/latest.tar.gz
    tar xzvf latest.tar.gz && rm latest.tar.gz
    mv ./wordpress/wp-config-sample.php ./wordpress/wp-config.php
    chown -R www-data:www-data /var/www/wordpress
    /vagrant/edit-wp-config.py
    systemctl reload nginx
  SHELL
end