# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.56.3", netmask: "255.255.255.0"

  # Share an additional folder to the guest VM
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Install nginx, php-fpm & mysql with a shell script
  config.vm.provision "shell", inline: <<-SHELL
    apt update
    apt install -y nginx mysql-server php-fpm php-mysql
  SHELL
end
