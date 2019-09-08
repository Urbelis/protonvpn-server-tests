import time 
from config import base_url
from services.logicals_impl import VPNServers

VPN_servers = VPNServers(base_url=base_url)
timestr = time.strftime("%Y%m%d-%H%M%S")
f = open("logs/"+timestr, "a")

f.write("Servers with high load: \n")
for server in VPN_servers.logical_servers:
    if VPN_servers.verify_logical_server_load(server) == "HIGH":
        f.write(str(server) +"\n")

f.write("Logical Servers that are offline: \n")
for server in VPN_servers.logical_servers:
    if VPN_servers.check_if_logical_online(server) != True:
        f.write(str(server)+ "\n")
