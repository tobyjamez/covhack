"""
Server interface functions for http verbs.
"""

import requests
import json

API_URL = ""


def search(search_string: str) -> dict:
    """
    @param search_string (str): string to search for

    Send a GET request with the search string.
    """
    params = dict(action="search",
                  word="search_string")
    response = requests.get(url=API_URL, params=params)
    return response.json()


def add(item_id: str) -> int:
    """
    @param item_id (str): ID for item to add to shopping list

    Send a POST request with an item id to add to shopping list.
    """
    item_dict = dict(action="add",
                     word=item_id)
    data = json.dumps(item_dict)
    response = requests.post(url=API_URL, data=item_id)
    return response.json()['status']


def show() -> dict:
    """
    Send a GET request to show current list.
    """
    params = dict(action="show")
    response = request.get(url=API_URL, params=params)
    return response.json()
