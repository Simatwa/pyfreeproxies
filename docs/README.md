<h1 align="center"> pyfreeproxies </h1>
<p align="center">
<!--
<a href="https://github.com/Simatwa/pyfreeproxies/actions/workflows/python-test.yml"><img src="https://github.com/Simatwa/pyfreeproxies/actions/workflows/python-test.yml/badge.svg" alt="Python Test"/></a>
-->
<a href="https://github.com/Simatwa/pyfreeproxies/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/static/v1?logo=GPL&color=Blue&message=GPLv3&label=License"/></a>
<a href=""><img alt="Python version" src="https://img.shields.io/pypi/pyversions/pyfreeproxies"/></a>
<a href="https://pypi.org/project/pyfreeproxies"><img alt="PyPi" src="https://img.shields.io/pypi/v/pyfreeproxies?color=green"/></a>
<a href="https://github.com/psf/black"><img alt="Black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/></a>
<a href="https://github.com/Simatwa/pyfreeproxies/actions/workflows/python-package.yml"><img alt="Python Package flow" src="https://github.com/Simatwa/pyfreeproxies/actions/workflows/python-package.yml/badge.svg?branch=master"/></a>
<a href="https://pepy.tech/project/pyfreeproxies"><img src="https://static.pepy.tech/personalized-badge/pyfreeproxies?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" alt="Downloads"></a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com/Simatwa/pyfreeproxies"/></a>      
<a href="https://wakatime.com/badge/github/Simatwa/pyfreeproxies"><img src="https://wakatime.com/badge/github/Simatwa/pyfreeproxies.svg" alt="wakatime"></a>
</p>

> Free to use http, socks4 and socks5 proxies based on [free-proxies](https://github.com/Simatwa/free-proxies).

## Installation

```
pip install -U pyfreeproxies
```

## Usage 

1. FreeProxies

   ```python
   from pyfreeproxies import FreeProxies
   proxy = FreeProxies()
   proxy.get_http_proxies() # http proxies
   proxy.get_socks4_proxies() # socks4 proxies 
   proxy.get_socks5_proxies() # socks 5 proxies
   proxy.get_combined_proxies() # http, socks4, socks5 combined.
   proxy.get_random_proxies() # Select from the lists randomly. 
   proxy.get_confirmed_working_proxies() # list of functional tested proxies. Support filters.
   proxy.get_proxies_metadata({"country": "United States",}) # filter with proxy metadata keys.
   proxy.proxies_update_available # check if there's an update to proxies.
   ```

---

2. Update Aware FreeProxies

   ```python
   from pyfreeproxies import UpdateAwareFreeProxies
   proxy = UpdateAwareFreeProxies()
   proxy.get_http_proxies() # http proxies
   proxy.get_socks4_proxies() # socks4 proxies 
   proxy.get_socks5_proxies() # socks 5 proxies
   proxy.get_combined_proxies() # http, socks4, socks5 combined.
   proxy.get_random_proxies() # Select from the lists randomly. 
   proxy.get_confirmed_working_proxies() # list of functional tested proxies. Support filters.
   proxy.get_proxies_metadata({"country": "United States",}) # filter with proxy metadata keys.
   proxy.is_update_available # check if there's an update to proxies.
   ```

---

3. IP Metadata

   ```python
   from pyfreeproxies import FreeProxies
   import pyfreeproxies.utils as proxies_util
   http_proxies = FreeProxies().get_http_proxies()
   proxy_metadata = proxies_util.trace_ip(http_proxies[0])
   print(proxy_metadata) # <class 'pyfreeproxies.models.ProxyMetadataModel'>
   """
   status='success' country='Vietnam' countryCode='VN' region='CT' regionName='Can Tho' city='Can Tho' zip='' lat=10.0359 lon=105.7808 timezone='Asia/Ho_Chi_Minh' isp='Viettel Corporation' org='VIETEL' as_='AS7552 Viettel Group' query='171.248.211.25' response_time=None continent=None continentCode=None district=None offset=None currency=None asname=None reverse=None mobile=None proxy=None hosting=None
   """
   ```

---

4. Your IP Metadata

   ```python
   import pyfreeproxies.utils as proxies_util
   proxy_metadata = proxies_util.trace_me()
   print(proxy_metadata) # <class 'pyfreeproxies.models.ProxyMetadataModel'>
   """
   status='success' country='Kenya' countryCode='KE' region='30' regionName='Nairobi County' city='Nairobi' zip='09831' lat=-1.28642 lon=*6.8198 timezone='Africa/Nairobi' isp='Jambonet Autonomous System' org='Telephone House' as_='AS12455 Kenyan Post & Telecommunications Company / Telkom Kenya Ltd' query='*1*.167.250.187' response_time=None continent=None continentCode=None district=None offset=None currency=None asname=None reverse=None mobile=None proxy=None hosting=None
   """
   ```

---

### [ProxyScrape](https://proxyscrape.com)

```python
from pyfreeproxies import ProxyScrape

scrape = ProxyScrape()

scrape.limit = 1

proxies = scrape.from_model()

print(proxies.total_records) 
print(proxies.shown_records)
print(proxies.limit)
print(proxies.skip)
print(proxies.nextpage)
print(proxies.proxies)
```

---

# Credits

- [x] [https://proxyscrape.com](proxyscrape.com)

---

<h3 align="center">Disclaimer</h3>

Please note that this project may involve the use of proxies for various purposes, including but not limited to, web scraping, data collection, or bypassing internet restrictions. It is the user's responsibility to ensure that their use of the project complies with all applicable laws and regulations, including but not limited to, copyright laws, privacy laws, and terms of service of the websites or services being accessed through the proxies.

The authors and contributors of **'freeproxies'** are not responsible for any misuse of the project, including but not limited to, any legal consequences that may arise from its use.

---