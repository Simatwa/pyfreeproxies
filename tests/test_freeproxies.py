import unittest
from pyfreeproxies import FreeProxies
from pyfreeproxies.models import ProxyMetadataModel
from pyfreeproxies.utils import trace_ip


class TestFreeProxies(unittest.TestCase):

    def setUp(self):
        self.proxy = FreeProxies()

    def test_timestamp_check(self):
        "Timestamp check"
        self.assertIsInstance(self.proxy.proxies_update_available, bool)

    def test_http_proxies(self):
        "Http proxies fetch"
        self.assertIsInstance(self.proxy.get_http_proxies(), list)

    def test_socks4_proxies(self):
        """Socks4 proxies fetch"""
        self.assertIsInstance(self.proxy.get_socks4_proxies(), list)

    def test_socks5_proxies(self):
        """Scoks5 proxies fetch"""
        self.assertIsInstance(self.proxy.get_socks5_proxies(), list)

    def test_random_proxies(self):
        """Random proxies fetch"""
        self.assertIsInstance(self.proxy.get_random_proxies(), list)

    def test_combined_proxies(self):
        """Combined proxies fetch"""
        self.assertIsInstance(self.proxy.get_combined_proxies(), dict)

    def test_proxy_metadata(self):
        """Proxies' metadata fetch"""
        metadata = self.proxy.get_proxies_metadata()
        self.assertTrue(type(metadata) is dict)
        self.assertIsInstance(list(metadata.values())[0], ProxyMetadataModel)

    def test_confirmed_working_proxies(self):
        """Confirmed working proxies"""
        filter = {"country": "Singapore"}
        working_proxies = self.proxy.get_confirmed_working_proxies(filter)
        self.assertIsInstance(working_proxies, list)
        if working_proxies:
            ip_metadata = trace_ip(working_proxies[0])
            assert ip_metadata.country == filter["country"]

    def test_proxies_logs_availability(self):
        """Proxies generation logs availability"""
        self.assertIsInstance(self.proxy.get_proxies_generation_logs(), str)

    def test_update(self):
        """Update FreeProxies"""
        new_FreeProxies = self.proxy.update()
        assert hasattr(new_FreeProxies, "update")


if __name__ == "__main__":
    unittest.main()
