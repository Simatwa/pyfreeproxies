import logging
import requests
import typing
from functools import wraps
from pyfreeproxies.models import ProxyMetadataModel

contents_url: str = (
    "https://raw.githubusercontent.com/AlphaBei254/free-proxies/master/files"
)

requests_timeout: int = 10

session = requests.Session()

session.headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "*/*",
}

url_map = {
    "http_proxies": contents_url + "/http.json",
    "socks4_proxies": contents_url + "/socks4.json",
    "socks5_proxies": contents_url + "/socks5.json",
    "combined_proxies": contents_url + "/proxies.json",
    "random_proxies": contents_url + "/random.json",
    "proxies_metadata": contents_url + "/metadata.json",
    "last_proxies_updated_time": contents_url + "/timestamp.json",
    "proxies_generation_logs": contents_url + "/proxies.log",
    "config_file": contents_url + "/config.json",
}

proxies_hunter_config = session.get(url_map["config_file"]).json()

proxies_update_frequency_in_seconds: int = (
    proxies_hunter_config["update_frequency_in_minutes"] * 60
)


def exception_handler(func):
    """Handle execptions accordingly"""

    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(e)

    return decorator


def fetch(*args, **kwargs) -> dict[str, typing.Any]:
    """fetch json resource from internet"""
    kwargs["timeout"] = requests_timeout
    resp = session.get(*args, **kwargs)
    resp.raise_for_status()
    return resp.json()


def trace_ip(ip: str) -> ProxyMetadataModel:
    """Trace particular IP

    Args:
        ip (str): IP address.

    Returns:
        ProxyMetadataModel: Ip metadata
    """
    query = ip.replace("https://", "").replace("http://", "").split(":")[0]
    return ProxyMetadataModel(**fetch(f"http://ip-api.com/json/{query}"))


def trace_me() -> ProxyMetadataModel:
    """Get your ip metadata"""
    return ProxyMetadataModel(**fetch("http://ip-api.com/json"))


def filter_proxies_metadata(
    proxies: dict[str, dict[str, typing.Any]], filters: dict[str, typing.Any] = {}
) -> dict[str, ProxyMetadataModel]:
    """Filter proxies metadata

    Args:
        proxies (dict[str, dict[str, typing.Any]]): Proxies.
        filters (dict[str, typing.Any]): Proxy metadata key and it's corresponding value. Defaults to `{}`.
        - Case type of filter is `int|float`, comparator will be `<=` else `==`

    Returns:
        dict[str, ProxyMetadataModel]: Proxies, Metadata
    """
    response: dict[str, ProxyMetadataModel] = {}

    for proxy, metadata in proxies.items():

        if not metadata.get("status", "") == "success":
            continue
        try:
            for filter_key, filter_value in filters.items():
                metadata_value: typing.Any = metadata.get(filter_key)
                if isinstance(metadata_value, (float, int)):
                    assert metadata_value <= filter_value
                else:
                    assert metadata_value == filter_value
            response[proxy] = ProxyMetadataModel(**metadata)
        except:
            pass

    return response


def filter_confirmed_working_proxies(
    proxies: dict[str, dict[str, typing.Any]], filters: dict[str, typing.Any] = {}
) -> list[str]:
    """Filter tested working proxies.

    Args:
        proxies (dict[str, dict[str, typing.Any]]): Proxies.
        filters (dict[str, typing.Any]): Proxy `metadata key` and it's corresponding `value`. Defaults to `{}`.
         - Case type of filter is `int|float`, comparator will be `<=` else `==`.

    Returns:
        list[str]: Proxies.
    """
    response: list[str] = []
    for proxy, metadata in proxies.items():
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
