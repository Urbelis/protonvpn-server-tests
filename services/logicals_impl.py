import json
import requests
import re
from utils.helpers import Helpers
from endpoints.vpn import VpnEndpoints


class LogicalServers():

    def __init__(self, base_url=None):
        self.base_url = base_url
        self.logicals_endpoint = VpnEndpoints().VPN_LOGICALS
        self.logical_servers = self.get_server_list()
        Helpers().evaluate_schema(self.logical_servers,
                        'schemas/logical_servers.json')

    def get_server_list(self):
        server_list = requests.get(self.base_url + self.logicals_endpoint)
        logical_servers = server_list.json()
        return logical_servers['LogicalServers']

    def free_servers(self):
        return [s for s in self.logical_servers if re.search(r'-free', s['Domain'])]

    def find_online_basic_server(self):
        for server in self.logical_servers:
            if server['Features'] == 0 and self.check_if_logical_online(server):
                return server
                
    def find_online_secure_server(self):
        for server in self.logical_servers:
            if server['Features'] == 1 and self.check_if_logical_online(server):
                return server

    def check_if_logical_online(self, logical_server):
        return logical_server['Status'] == 1

    def check_if_physical_online(self, logical_server):
        for server in logical_server['Servers']:
            return server['Status'] == 1

    def verify_logical_server_load(self, logical_server):
        load = logical_server['Load']
        if load <= 50:
            return "LOW"
        if 50 <= load < 90:
            return "MEDIUM"
        if load >= 90:
            return "HIGH"
