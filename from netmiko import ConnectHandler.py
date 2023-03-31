from netmiko import ConnectHandler

 

iosv_l2 = {

    'device_type': 'cisco_ios',

    'ip': '192.168.122.72',

    'username': 'david',

    'password': 'cisco',

}

 

net_connect = ConnectHandler(**iosv_l2)

output = net_connect.send_command('show ip int brief')

print (output)

 

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']

output = net_connect.send_config_set(config_commands)

print (output)

 

for n in range (2,21):

    print "Creating VLAN " + str(n)

    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]

    output = net_connect.send_config_set(config_commands)

    print (output)

 

##################################### Enable mode #####################################

 

#!/usr/bin/env python

 

from netmiko import ConnectHandler

 

iosv_l2 = {

    'device_type': 'cisco_ios',

    'ip': '10.1.1.4',

    'username': 'netadmin',

    'password': 'password',

}

 

net_connect = ConnectHandler(**iosv_l2)

net_connect.enable()

output = net_connect.send_command('show ip int brief')

print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']

output = net_connect.send_config_set(config_commands)

print (output)

 

 

##################################### SSH to multiple switches #####################################

 

 

 

#!/usr/bin/env python

 

from netmiko import ConnectHandler

 

iosv_l2_s1 = {

    'device_type': 'cisco_ios',

    'ip': '10.1.1.3',

    'username': 'netadmin',

    'password': 'password',

}

 

iosv_l2_s2 = {

    'device_type': 'cisco_ios',

    'ip': '10.1.1.4',

    'username': 'netadmin',

    'password': 'password',

}

all_devices = [iosv_l2_s1, iosv_l2_s2]

 

for devices in all_devices:

    net_connect = ConnectHandler(**devices)

    net_connect.enable()

    output = net_connect.send_command('show ip int brief')

    print (output)

    config_commands = ['int loop 1', 'ip address 2.2.2.2 255.255.255.0']

    output = net_connect.send_config_set(config_commands)

    print (output)

 

 

##################################### apply configs from a file #####################################

 

#!/usr/bin/env python

 

from netmiko import ConnectHandler

 

iosv_l2_s1 = {

    'device_type': 'cisco_ios',

    'ip': '10.1.1.3',

    'username': 'netadmin',

    'password': 'password',

}

 

iosv_l2_s2 = {

    'device_type': 'cisco_ios',

    'ip': '10.1.1.4',

    'username': 'netadmin',

    'password': 'password',

}

with open('configs') as f:

     lines = f.read().splitlines()

print (lines)

all_devices = [iosv_l2_s1, iosv_l2_s2]

 

for devices in all_devices:

    net_connect = ConnectHandler(**devices)

    net_connect.enable()

    output = net_connect.send_config_set(lines)

    print (output)

 

 

##################################### configure vlan on interface #####################################

 

#!/usr/bin/env python

 

from netmiko import ConnectHandler

 

iosv_l2 = {

    'device_type': 'cisco_ios',

    'ip': '10.1.1.4',

    'username': 'netadmin',

    'password': 'password',

}

 

net_connect = ConnectHandler(**iosv_l2)

net_connect.enable()

interface = input('Pls enter the interface numer:')

vlan = input('Pls enter the VLAN number:')

config_commands = ['interface ethernet' + interface , 'switchport' , 'switchport mode access' , 'switchport access vlan ' + vlan , 'exit']

net_connect.send_config_set(config_commands)

output = net_connect.send_command('show interfaces status | inc ' + interface)

 

print (output)

 