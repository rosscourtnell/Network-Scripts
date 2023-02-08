#Python script using netmiko to run commands on IOS Router

import netmiko

connection =netmiko.ConnectHandler(ip="10.2.224.3", device_type="cisco_nxos", username="RossC", password=input("Password: "))
print(connection.send_command("sh ip int brief"))
connection.disconnect()
