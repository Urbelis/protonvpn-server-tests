import time
from config import base_url
from services.logicals_impl import LogicalServers

servers = LogicalServers(base_url=base_url)
high_load_servers = []
offline_servers = []
timestr = time.strftime("%Y%m%d-%H%M%S")
f = open("logs/"+timestr, "a")

for server in servers.logical_servers:
    if servers.verify_logical_server_load(server) == "HIGH":
        high_load_servers.append(server)
    if servers.check_if_logical_online(server) != True:
        offline_servers.append(server)

f.write("Servers with high load: \n")
for server in high_load_servers:
    f.write(str(server) + "\n")

f.write("Servers which are offline: \n")
for server in offline_servers:
    f.write(str(server) + "\n")
