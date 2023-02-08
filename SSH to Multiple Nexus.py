# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler

tacacs=input("Password: ")
with open("TT_Nexus_Devices.txt") as nexusswitches:
    for HOST in nexusswitches:
        Switch = {
            "device_type": "cisco_nxos",
            "host": HOST,
            "username": "RossC",
            "password": tacacs
        }
        
        net_connect = ConnectHandler(**Switch)

        print ('Connecting to ' + HOST)
        print('-'*79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)

# Finally close the connection
net_connect.disconnect()
