import json
import requests
import re
from endpoints.vpn import VpnEndpoints


class LogicalServers():

    def __init__(self, base_url=None):
        self.base_url = base_url
        self.logicals_endpoint = VpnEndpoints().VPN_LOGICALS
        self.server_list = self.get_server_list()
        self.logical_servers = self.server_list['LogicalServers']

    def get_server_list(self):
        server_list = requests.get(self.base_url + self.logicals_endpoint)
        logical_servers = server_list.json()
        return logical_servers

    def find_free_servers(self, server_list):
        free_servers = []
        for server in server_list:
            if re.search(r'-free', server['Domain']):
                free_servers.append(server)
            else:
                continue
        return free_servers

    def find_online_basic_server(self, server_list):
        for server in server_list:
            if server['Features'] == 0 and self.check_if_logical_online(server) == True:
                return server
            else:
                continue

    def find_online_secure_server(self, server_list):
        for server in server_list:
            if server['Features'] == 1 and self.check_if_logical_online(server) == True:
                return server
            else:
                continue

    def check_if_logical_online(self, logical_server):
        if logical_server['Status'] == 1:
            return True

    def check_if_physical_online(self, logical_server):
        for server in logical_server['Servers']:
            if server['Status'] == 1:
                return True

    def verify_logical_server_load(self, logical_server):
        load = logical_server['Load']
        if load <= 50:
            logical_server_load_status = "LOW"
        if 50 <= load < 90:
            logical_server_load_status = "MEDIUM"
        if load >= 90:
            logical_server_load_status = "HIGH"
        return logical_server_load_status
