from pydantic import BaseModel, Field, IPvAnyAddress
from typing import Union
from datetime import datetime


class ProxyMetadataModel(BaseModel):
    status: str
    country: str
    countryCode: str
    region: Union[str, None] = None
    regionName: str
    city: str
    zip: str
    lat: float
    lon: float
    timezone: str
    isp: str
    org: str
    as_: str = Field(..., alias="as")
    query: Union[IPvAnyAddress, None] = None
    response_time: Union[float, None] = None
    continent: Union[str, None] = None
    continentCode: Union[str, None] = None
    district: Union[str, None] = None
    offset: Union[float, None] = None
    currency: Union[str, None] = None
    asname: Union[str, None] = None
    reverse: Union[str, None] = None
    mobile: Union[bool, None] = None
    proxy: Union[bool, None] = None
    hosting: Union[bool, None] = None


class ProxyScrapeProxiesModel(BaseModel):
    alive: bool
    alive_since: datetime
    anonymity: str
    average_timeout: float
    first_seen: datetime
    ip_data: ProxyMetadataModel
    ip_data_last_update: datetime
    last_seen: datetime
    port: int
    protocol: str
    proxy: str
    ssl: bool
    timeout: float
    times_alive: int
    times_dead: int
    uptime: float
    ip: IPvAnyAddress


class ProxyScrapeModel(BaseModel):
    shown_records: int
    total_records: int
    limit: int
    skip: int
    nextpage: bool
    proxies: list[ProxyScrapeProxiesModel]
