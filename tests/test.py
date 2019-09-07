import requests
import json
import unittest
from utils.helpers import Helpers
from services.logicals_impl import VPNServers


class ServerTests(unittest.TestCase):
    VPN_servers = VPNServers(base_url='https://api.protonmail.ch/')
    helpers = Helpers()
    servers = VPN_servers.get_server_list()
    logical_server_list = servers['LogicalServers']

    def test_validate_server_schema(self):
        self.helpers.evaluate_schema(
            self.logical_server_list, 'schemas/logical_servers.json')

    def test_vpn_applications_are_operational(self):
        self.VPN_servers.find_online_basic_server(self.logical_server_list)
        self.VPN_servers.find_online_secure_server(self.logical_server_list)

    def test_free_servers_are_accessible(self):
        free_servers = self.VPN_servers.find_free_servers(
            self.logical_server_list)
        for server in free_servers:
            self.assertEqual(self.VPN_servers.check_if_online(server), True)
