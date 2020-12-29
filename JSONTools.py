import requests
from requests.exceptions import HTTPError
from collections import namedtuple
from json import JSONEncoder


class Json:
    url = "https://reqres.in/api/products"

    def __int__(self):
        self.responseJson = None

    def getJson(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.responseJson = response.json()
        except HTTPError as http_error:
            print(f"http error: {http_error}")
        except Exception as err:
            print(f"other error: {err}")

    def getDataFromJson(self):
        return self.responseJson["data"]


class Product:

    def __init__(self, id, name, year, color, pantone_value):
        self.id = id
        self.name = name
        self.year = year
        self.color = color
        self.pantone_value = pantone_value

    def add(self, product):
        self.products.append(product)


def productJsonDecod(productDict):
    return namedtuple('X', productDict.keys())(*productDict.values())
