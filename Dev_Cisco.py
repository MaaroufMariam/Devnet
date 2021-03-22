from netmiko import ConnectHandler
#from getpass import getpass

XR = {
                'host':'sbx-iosxr-mgmt.cisco.com',
                'username':'admin',
                'password':'C1sco12345',
                'port':8181,
                'device_type':'cisco_ios',
     }

NX = {
                'host':'sbx-nxos-mgmt.cisco.com',
                'username':'admin',
                'password':'Admin_1234!',
                'port':8181,
                'device_type':'cisco_ios',
     }

XE = {
                'host':'ios-xe-mgmt.cisco.com',
                'username':'developer',
                'password':'C1sco12345',
                'port':8181,
                'device_type':'cisco_ios',

     }
list = [NX,XE,XR]
for i in list:

        dev_device =  ConnectHandler(**i)
        dev_device.enable()
        add = input('enter the loopback address')
        print(add.split())
        for j in add:
                commands =["conf t" , "int loopback 0",j+" 255.255.255.255","no shut","router ospf 1","network "+j+"0.0.0.0 area 0","do show ip int brief","do show ip route"]
                for k in commands:
                        dev_device.send_command_timing(k)
        dev_device.find_prompt()
        dev_device.disconnect()
