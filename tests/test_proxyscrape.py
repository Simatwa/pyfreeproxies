from pyfreeproxies.models import ProxyScrapeModel
from pyfreeproxies import ProxyScrape
import unittest


class TestProxyScrape(unittest.TestCase):

    def setUp(self):
        self.proxy = ProxyScrape()

    def test_format_specific_proxies(self):
        self.assertIsInstance(self.proxy.in_format("text"), str)

    def test_jsonified_proxies(self):
        self.assertIsInstance(self.proxy.get_jsonified_proxies(), dict)

    def test_proxies_from_model(self):
        self.assertIsInstance(self.proxy.proxies, ProxyScrapeModel)


if __name__ == "__main__":
    unittest.main()
