from config import base_url
from utils.helpers import Helpers
from services.logicals_impl import VPNServers

# Move BASEURL To Pytest CFG

helpers = Helpers()
VPN_servers = VPNServers(base_url=base_url)


def test_validate_server_schema():
    helpers.evaluate_schema(VPN_servers.logical_servers,
                            'schemas/logical_servers.json')


def test_vpn_applications_are_operational():
    assert VPN_servers.find_online_basic_server(
        VPN_servers.logical_servers) != None
    assert VPN_servers.find_online_secure_server(
        VPN_servers.logical_servers) != None


def test_at_least_one_free_server_is_accessible():
    free_servers = VPN_servers.find_free_servers(
        VPN_servers.logical_servers)
    assert any(VPN_servers.check_if_logical_online(
        server) != False and VPN_servers.check_if_physical_online(server) != False for server in free_servers)
