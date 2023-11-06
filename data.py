from dataclasses import dataclass


@dataclass
class DatasetItem:
    name: str
    full_name: str
    width: int
    height: int
    death: int
    sale_price: int
    country: str = ""
    style: str = ""  #
    subject: str = ""  #
    genre: str = ""  #
    medium: str = ""  #
    exhibition: bool = False
    for_sale: bool = False
    restored: bool = False
