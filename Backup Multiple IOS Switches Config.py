# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler

tacacs=input("Password: ")
with open('LW__Device_Backup.txt') as switches:
    for HOST in switches:
        Switch = {
            "device_type": "cisco_ios",
            "host": HOST,
            "username": "RossC",
            "password": tacacs
        }

        net_connect = ConnectHandler(**Switch)

        hostname = net_connect.send_command('sh run | i hostname | excl logging')
        hostname.split(" ")
        hostname,device = hostname.split(" ")
        print ("Backing up " + device)

        filename = "C:\TEMP\LW Backups/" + device + ".txt"
        # to save backup to same folder as script use below line and comment out above line 
        #filename = device + '.txt' 

        showrun = net_connect.send_command('show run')
        showvlan = net_connect.send_command('show vlan')
        showintstatus = net_connect.send_command('show int status')
        showipintbri = net_connect.send_command('show ip int brief')
        showiproute = net_connect.send_command('show ip route')
        log_file = open(filename, "a")   # in append mode
        log_file.write(showrun)
        log_file.write("\n")
        log_file.write(showvlan)
        log_file.write("\n")
        log_file.write(showintstatus)
        log_file.write("\n")
        log_file.write(showipintbri)
        log_file.write("\n")
        log_file.write(showiproute)
        log_file.write("\n")

# Finally close the connection
net_connect.disconnect()