"""
Server interface functions for http verbs.
"""

import requests

API_URL = "https://phrijj.herokuapp.com/server/"


def search(search_string: str) -> dict:
    """
    @param search_string (str): string to search for

    Send a GET request with the search string.
    """
    params = dict(action="search",
                  name=search_string)
    response = requests.get(API_URL+"lowestprice/"+search_string)
    return response.json()


def add(item_id: str) -> int:
    """
    @param item_id (str): ID for item to add to shopping list

    Send a POST request with an item id to add to shopping list.
    """
    headers = {"content-type": "application/json"}
    data = dict(name=item_id)
    response = requests.post(url=API_URL+"add/", data=data)
    return response.json()['status']


def show() -> dict:
    """
    Send a GET request to show current list.
    """
    params = dict(action="show")
    response = requests.get(API_URL+"show/")
    return response
