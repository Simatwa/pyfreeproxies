from pyfreeproxies.models import ProxyMetadataModel
import pyfreeproxies.utils as proxies_util
from datetime import datetime, timezone, timedelta
import typing


class FreeProxies:
    """Contains free `http`, `socks4` and `socks5` proxies."""

    def __init__(self):
        """Constructor"""
        self.last_proxies_updated_time_str_in_utc: str = proxies_util.fetch(
            url=proxies_util.url_map["last_proxies_updated_time"]
        ).get("utc")
        self.available_proxies_category: list[str] = [
            "http",
            "socks4",
            "socks5",
            "random",
        ]

    @property
    def proxies_update_available(self) -> bool:
        """Check if there's an update to proxies"""
        last_update_time_in_utc = datetime.fromisoformat(
            self.last_proxies_updated_time_str_in_utc
        ).replace(tzinfo=timezone.utc)
        current_time_in_utc = datetime.now(timezone.utc)
        return current_time_in_utc > (
            last_update_time_in_utc
            + timedelta(seconds=proxies_util.proxies_update_frequency_in_seconds)
        )

    def get_proxies(
        self, proxy_type: typing.Literal["http", "socks4", "socks5", "random"]
    ) -> list[str]:
        """Get proxies"""
        assert (
            proxy_type in self.available_proxies_category
        ), f"Invalid proxy category {proxy_type}, should be one of {', '.join(self.available_proxies_type)}."
        return proxies_util.fetch(proxies_util.url_map[f"{proxy_type}_proxies"]).get(
            "proxies"
        )

    def get_http_proxies(self) -> list[str]:
        """Http proxies"""
        return self.get_proxies("http")

    def get_socks4_proxies(self) -> list[str]:
        """Socks4 proxies"""
        return self.get_proxies("socks4")

    def get_socks5_proxies(self) -> list[str]:
        """Socks5 proxies"""
        return self.get_proxies("socks5")

    def get_random_proxies(self) -> list[str]:
        """Random proxies"""
        return self.get_proxies("random")

    def get_combined_proxies(self) -> dict[str, list[str]]:
        """http, socks4 and socks5 proxies"""
        return proxies_util.fetch(proxies_util.url_map["combined_proxies"])

    def get_proxies_metadata(self) -> dict[str, ProxyMetadataModel]:
        """Proxies with their info"""
        response: dict[str, ProxyMetadataModel] = {}
        for proxy, metadata in proxies_util.fetch(
            proxies_util.url_map["proxies_metadata"]
        ).items():

            if not metadata.get("status", "") == "success":
                continue

            response[proxy] = ProxyMetadataModel(**metadata)
        return response

    def get_confirmed_working_proxies(self, **filters) -> list[str]:
        """List of tested working proxies. **Filters are supported.**
        - Case type of filter is `int|float`, comparator will be `<=` else `==`
        """
        response: list[str] = []
        for proxy, metadata in proxies_util.fetch(
            proxies_util.url_map["proxies_metadata"]
        ).items():
            try:
                for filter_key, filter_value in filters.items():
                    metadata_value: typing.Any = metadata.get(filter_key)
                    if isinstance(metadata_value, (float, int)):
                        assert metadata_value <= filter_value
                    else:
                        assert metadata_value == filter_value
                response.append(proxy)
            except:
                pass

        return response

    def get_proxies_generation_logs(self) -> str:
        "Last proxies generation logs"
        return proxies_util.session.get(
            proxies_util.url_map["proxies_generation_logs"],
            timeout=proxies_util.requests_timeout,
        ).text

    def update(self) -> "FreeProxies":
        """Create new class instance and update timestamp"""
        return FreeProxies()
