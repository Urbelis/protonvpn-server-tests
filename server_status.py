import time
from config import base_url
from services.logicals_impl import LogicalServers

servers = LogicalServers(base_url=base_url)
timestr = time.strftime("%Y%m%d-%H%M%S")
f = open("logs/"+timestr, "a")

high_load_servers = [s for s in servers.logical_servers if servers.verify_logical_server_load(s) == "HIGH"]
offline_servers = [s for s in servers.logical_servers if not servers.check_if_logical_online(s)]

f.write("Servers with high load: \n")
for server in high_load_servers:
    f.write(str(server) + "\n")

f.write("Servers which are offline: \n")
for server in offline_servers:
    f.write(str(server) + "\n")
