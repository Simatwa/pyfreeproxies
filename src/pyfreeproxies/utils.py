import logging
import requests
import typing
from functools import wraps
from pyfreeproxies.models import ProxyMetadataModel

contents_url: str = (
    "https://raw.githubusercontent.com/Simatwa/free-proxies/master/files"
)

proxies_update_frequency_in_seconds: int = 30 * 60

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
}


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
    """fetch resource from internet"""
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
    return ProxyMetadataModel(**fetch("http://ip-api.com/"))
