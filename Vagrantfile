# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure(2) do |config|
    # using a Centos machine
    config.vm.box = "boxcutter/centos72"
    config.vm.network "private_network", ip: "10.0.30.10"

    # creating a single node (it's a proof of concept so
    # I don't need to create a real cluster)
    config.vm.provision :ansible do |ansible|
        ansible.playbook = "provisioning/kafka.yml"
    end
end
