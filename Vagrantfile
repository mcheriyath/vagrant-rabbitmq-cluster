# -*- mode: ruby -*-
# vi: set ft=ruby :

#!! REQUIRES !! vagrant-hostmanager

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

BOXES = [
  { name: :mq1, ip: '10.10.1.101', },
  { name: :mq2, ip: '10.10.1.102', },
  { name: :mq3, ip: '10.10.1.103', },
  { name: :mq3, ip: '10.10.1.104', },
]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  #config.proxy.http     = "http://username:password@url:port"
  #config.proxy.https    = "http://username:password@url:port"
  #config.proxy.no_proxy = "localhost,127.0.0.1"
  config.ssh.insert_key = false
  config.vm.box = 'ubuntu/xenial64'
  config.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
  config.ssh.forward_agent = true

  # Hostmanager config
  #config.vm.provision :hostmanager
  #config.hostmanager.enabled = true
  #config.hostmanager.manage_host = true
  #config.hostmanager.ignore_private_ip = false
  #config.hostmanager.include_offline = true

  config.vm.provider :virtualbox do |vb|
    vb.customize ['modifyvm', :id, '--cpus', '1']
    vb.customize ['modifyvm', :id, '--memory', '1024']
    vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
  end

  BOXES.each do |opts|
    config.vm.define opts[:name] do |config|
      config.vm.hostname = opts[:name].to_s

      config.vm.network :private_network, ip: opts[:ip], netmask: '255.255.255.0'

    end
  end
end

