import time
import json
from config import BASE_URL
from services.logicals_impl import LogicalServers

servers = LogicalServers(base_url=BASE_URL)
timestr = time.strftime("%Y%m%d-%H%M%S")
high_load_file= open("logs/highload."+timestr+".json", "a")
offline_servers_file = open("logs/servers"+timestr+".json", "a")

high_load_servers = [s for s in servers.logical_servers if servers.verify_logical_server_load(s) == "HIGH"]
offline_servers = [s for s in servers.logical_servers if not servers.check_if_logical_online(s)]

json.dump(high_load_servers, high_load_file, indent=4, sort_keys=True)
json.dump(offline_servers, offline_servers_file, indent=4, sort_keys=True)