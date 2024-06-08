from pyfreeproxies.proxies import FreeProxies
from pyfreeproxies.proxies import UpdateAwareFreeProxies
from pyfreeproxies.proxyscrape import ProxyScrape

from importlib import metadata

try:
    __version__ = metadata.version("pyfreeproxies")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0"
