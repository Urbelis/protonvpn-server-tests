from config import base_url
from utils.helpers import Helpers
from services.logicals_impl import LogicalServers

servers = LogicalServers(base_url=base_url)


def test_vpn_applications_are_operational():
    assert servers.find_online_basic_server() != None
    assert servers.find_online_secure_server() != None


def test_at_least_one_free_server_is_accessible():
    free_servers = servers.free_servers()
    assert any(servers.check_if_logical_online(
        server) and servers.check_if_physical_online(server) for server in free_servers)
