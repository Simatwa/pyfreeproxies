from pyfreeproxies.models import ProxyScrapeModel
from pyfreeproxies.utils import fetch, session
from typing import Literal


class ProxyScrape:

    url_format = (
        "https://api.proxyscrape.com/v3/free-proxy-list/get"
        "?request=displayproxies&proxy_format=protocolipport"
        "&format=%(format)s"
    )

    def __init__(self, limit: int = 343):
        """Constructor

        Args:
            limit (int, optional): Total proxies to be processed. Defaults to 343.
        """
        self._proxies_metadata_cache = {}
        self.limit = limit

    def get_jsonified_proxies(self) -> dict:
        """Fetch proxies metadata in json format

        Returns:
            dict: Proxies metadata
        """
        resp = (
            self._proxies_metadata_cache
            if self._proxies_metadata_cache
            else fetch(self.url_format % dict(format="json"))
        )
        if self.limit:
            resp["proxies"] = resp.get("proxies")[: self.limit]

        return resp

    def update_proxies(self):
        """Update proxies cache"""
        self._proxies_metadata_cache = None
        new_proxies = self.get_jsonified_proxies()
        self._proxies_metadata_cache = new_proxies

    def from_model(self) -> ProxyScrapeModel:
        """Get proxies and make model.

        Returns:
            ProxyScrapeModel: Modelled proxies.
        """
        return ProxyScrapeModel(**self.get_jsonified_proxies())

    def in_format(self, format: Literal["json", "csv", "text"]) -> str:
        """Get proxies metadata in specific format.

        Args:
            format (Literal[json, csv, text]): Desired format.

        Returns:
            str: Proxies metadata
        """
        resp = session.get(
            self.url_format % {"format": format},
        )
        resp.raise_for_status()
        return resp.text

    @property
    def proxies(self) -> ProxyScrapeModel:
        return self.from_model()
