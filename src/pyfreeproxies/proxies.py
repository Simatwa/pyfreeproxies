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

    def get_proxies_metadata(
        self, filters: dict[str, typing.Any] = {}
    ) -> dict[str, ProxyMetadataModel]:
        """Proxies with their info

        Args:
            filters (dict[str, typing.Any]): Proxy metadata key and it's corresponding value. Defaults to `{}`.
            - Case type of filter is `int|float`, comparator will be `<=` else `==`

        Returns:
            dict[str, ProxyMetadataModel]: Proxy and ProxyMetadata object.
        """

        return proxies_util.filter_proxies_metadata(
            proxies_util.fetch(proxies_util.url_map["proxies_metadata"]), filters
        )

    def get_confirmed_working_proxies(
        self, filters: dict[str, typing.Any] = {}
    ) -> list[str]:
        """List of tested working proxies. Filters are supported.

        Args:
            filters (dict[str, typing.Any]): Proxy `metadata key` and it's corresponding `value`. Defaults to `{}`.
             - Case type of filter is `int|float`, comparator will be `<=` else `==`.

        Returns:
            list[str]: Proxies.
        """
        return proxies_util.filter_confirmed_working_proxies(
            proxies_util.fetch(proxies_util.url_map["proxies_metadata"]), filters
        )

    def get_proxies_generation_logs(self) -> str:
        "Last proxies generation logs"
        return proxies_util.session.get(
            proxies_util.url_map["proxies_generation_logs"],
            timeout=proxies_util.requests_timeout,
        ).text

    def update(self) -> "FreeProxies":
        """Create new class instance and update timestamp"""
        return FreeProxies()


class UpdateAwareFreeProxies:
    """Considers `update` in fetching proxies"""

    def __init__(self):
        self.freeProxies = FreeProxies()
        self._http_proxies = self.freeProxies.get_http_proxies()
        self._socks4_proxies = self.freeProxies.get_socks4_proxies()
        self._socks5_proxies = self.freeProxies.get_socks5_proxies()
        self._random_proxies = self.freeProxies.get_random_proxies()
        self._combined_proxies = self.freeProxies.get_combined_proxies()
        self._proxies_metadata = proxies_util.fetch(
            proxies_util.url_map["proxies_metadata"]
        )
        self._confirmed_working_proxies = self._proxies_metadata.copy()
        self._proxies_generation_logs = self.freeProxies.get_proxies_generation_logs()

    @property
    def is_update_available(self) -> bool:
        """Update freeproxies if there's an update"""
        if self.freeProxies.proxies_update_available:
            self.freeProxies = FreeProxies()
            return True
        else:
            return False

    def get_http_proxies(self) -> list[str]:
        """http proxies"""
        if self.is_update_available:
            self._http_proxies = self.freeProxies.get_http_proxies()

        return self._http_proxies

    def get_socks4_proxies(self) -> list[str]:
        """Socks4 proxies"""
        if self.is_update_available:
            self._socks4_proxies = self.freeProxies.get_socks4_proxies()

        return self._socks4_proxies

    def get_socks5_proxies(self) -> list[str]:
        """Socks5 proxies"""
        if self.is_update_available:
            self._socks5_proxies = self.freeProxies.get_socks5_proxies()

        return self._socks5_proxies

    def get_random_proxies(self) -> list[str]:
        """Random proxies"""
        if self.is_update_available:
            self._random_proxies = self.freeProxies.get_random_proxies()

        return self._random_proxies

    def get_combined_proxies(self) -> dict[str, list[str]]:
        """Combined proxies"""
        if self.is_update_available:
            self._combined_proxies = self.freeProxies.get_combined_proxies()

        return self._combined_proxies

    def get_proxies_metadata(
        self, filters: dict[str, typing.Any] = {}
    ) -> dict[str, ProxyMetadataModel]:
        """Proxies with their info. `Filters are supported.`

        Args:
            filters (dict[str, typing.Any]): Proxy metadata key and it's corresponding value. Defaults to `{}`.
            - Case type of filter is `int|float`, comparator will be `<=` else `==`

        Returns:
            dict[str, ProxyMetadataModel]: Proxy and ProxyMetadata object.
        """
        if self.is_update_available:
            self._proxies_metadata = proxies_util.fetch(
                proxies_util.url_map["proxies_metadata"]
            )

        return proxies_util.filter_proxies_metadata(self._proxies_metadata, filters)

    def get_confirmed_working_proxies(
        self, filters: dict[str, typing.Any]
    ) -> list[str]:
        """List of tested working proxies. `Filters are supported.`

        Args:
            filters (dict[str, typing.Any]): Proxy `metadata key` and it's corresponding `value`. Defaults to `{}`.
             - Case type of filter is `int|float`, comparator will be `<=` else `==`.

        Returns:
            list[str]: Proxies.
        """
        if self.is_update_available:
            self._confirmed_working_proxies = proxies_util.fetch(
                proxies_util.url_map["proxies_metadata"]
            )

        return proxies_util.filter_confirmed_working_proxies(
            self._confirmed_working_proxies, filters
        )

    def get_proxies_generation_logs(self) -> str:
        """Proxies generation logs"""
        if self.is_update_available:
            self._proxies_generation_logs = (
                self.freeProxies.get_proxies_generation_logs()
            )

        return self._proxies_generation_logs
