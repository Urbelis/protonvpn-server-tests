from config import base_url
from utils.helpers import Helpers
from services.logicals_impl import LogicalServers

helpers = Helpers()
servers = LogicalServers(base_url=base_url)


def test_validate_server_schema():
    helpers.evaluate_schema(servers.logical_servers,
                            'schemas/logical_servers.json')


def test_vpn_applications_are_operational():
    assert servers.find_online_basic_server(
        servers.logical_servers) != None
    assert servers.find_online_secure_server(
        servers.logical_servers) != None


def test_at_least_one_free_server_is_accessible():
    free_servers = servers.find_free_servers(
        servers.logical_servers)
    assert any(servers.check_if_logical_online(
        server) != False and servers.check_if_physical_online(server) != False for server in free_servers)
