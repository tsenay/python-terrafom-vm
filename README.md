# terraform-vm

## Requirements

 - python3
 - terraform

## Installation

pip install terraform-vm

## Develop

```bash
git clone https://github.com/tsenay/python-terraform-vm.git
cd python-terraform-vm
python -m venv venv
source ./venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

### Password Management
They must be passed as an environment variables.

Required password variable

- ESXPASS

### Command line

Usage

```bash
$ python-terraform-vm --help
usage: python-terraform-vm [-h] --action {create,destroy} --datacenter DATACENTER
                  --datastore DATASTORE --pool POOL --folder FOLDER --template
                  TEMPLATE --guestid GUESTID --name NAME [--nic NIC] [--ip IP]
                  [--cidr CIDR] [--gateway GATEWAY] --cpu CPU --ram RAM
                  [--disk DISK] [--dns DNS] --esxhost ESXHOST --esxuser
                  ESXUSER [-debug]

Manage vSphere Virtual Machines

optional arguments:
  -h, --help            show this help message and exit
  --action {create,destroy}
                        Action to Execute against vSphere
  --datacenter DATACENTER
                        ESXi Datacenter
  --datastore DATASTORE
                        ESXi Datastore
  --pool POOL           ESXi Resource Pool
  --folder FOLDER       ESXi VM Folder
  --template TEMPLATE   Template Name
  --guestid GUESTID     Guest ID
  --name NAME           Virtual Machine Name
  --nic NIC             Network Interface. Repeat option for several NICs
  --ip IP               NIC IP address. Repeat option for several NICs
  --cidr CIDR           NIC CIDR. Repeat option for several NICs
  --gateway GATEWAY     Default gateway
  --cpu CPU             CPUs
  --ram RAM             Memory
  --disk DISK           Additionnal disk in GB. Repeat option for several
                        disks
  --dns DNS             DNS server
  --esxhost ESXHOST     ESXi host
  --esxuser ESXUSER     ESXi Username
  -debug                Verbose Output

Environment variable ESXPASS is required to connect to vSphere /!\ When you
want to destroy a VM, tfstate file is not required
```

### Examples 

Create a VM
```bash
python-terraform-vm --name terrascript-test --datacenter "DC" --datastore "MyDatastore" --pool "ressource_pool" --template "rhel-7.5-vmw6.0" --guestid "rhel7_64Guest" --nic DvP_Nmae --ip 10.0.123.123 --cidr 24 --gateway 10.0.123.1 --cpu 1 --ram 1024 --disk 10 --dns 10.0.123.50 --dns 10.0.123.100 --esxhost esxhost.domain.com --esxuser "esxusername" --folder "terraformed" --action create
```

Destroy a VM
```bash
python-terraform-vm --name terrascript-test --datacenter "DC" --datastore "MyDatastore" --pool "ressource_pool" --template "rhel-7.5-vmw6.0" --guestid "rhel7_64Guest" --cpu 1 --ram 1024 --esxhost esxhost.domain.com --esxuser "esxusername" --folder "terraformed" --action destroy
```
