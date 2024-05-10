import pydantic
from typing import Union


class ProxyMetadataModel(pydantic.BaseModel):
    status: str
    country: str
    countryCode: str
    region: str
    regionName: str
    city: str
    zip: str
    lat: float
    lon: float
    timezone: str
    isp: str
    org: str
    as_: str = pydantic.Field(..., alias="as")
    query: str
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
