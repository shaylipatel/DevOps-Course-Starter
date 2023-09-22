import requests
import os


# board_id = os.getenv(TRELLO_BOARD_ID)
# trello_token = os.getenv(TRELLO_TOKEN)
# trello_key = os.getenv(TRELLO_KEY)

class Trello:
    def __init__(self):
        self.board_id = os.getenv('TRELLO_BOARD_ID')
        self.trello_token = os.getenv('TRELLO_TOKEN')
        self.trello_key = os.getenv('TRELLO_KEY')
        self.lists = self.get_lists()

    def get_lists(self):
        """
        Gets the list names and list ids

        Returns:
            dict: The dictionary with list ids and their retrospective names

        """
        trello_lists_api = requests.get(
            f"https://api.trello.com/1/boards/{self.board_id}/lists?key={self.trello_key}&token={self.trello_token}").json()
        list_names = {}
        for list_name in trello_lists_api:
            list_names[list_name['id']] = list_name['name']
        return list_names


class Item(Trello):
    def __init__(self, item_id, name, status):
        super().__init__()
        self.id = item_id
        self.name = name
        self.status = status


def get_items():
    """
    Fetches all items on Trello board via API

    Returns:
        list: The list of Trello items.
    """
    trello_details = Trello()
    trello_get_cards_api = requests.get(
        f"https://api.trello.com/1/boards/{trello_details.board_id}/cards/open?key={trello_details.trello_key}&token={trello_details.trello_token}").json()
    items = _select_fields(trello_get_cards_api, trello_details.lists)
    return items


def _select_fields(data, list_names):
    """
    Iterates through the Trello api data and puts the item's name. status and id into a new class object
    Args:
        data: Trello api data in json format.
        list_names: Dictionary of the list names and list ids.

    Returns:
        list: List of Trello items.

    """
    items = []
    for record in data:
        list_id = record["idList"]
        status = list_names[list_id]
        item = Item(record['id'], record['name'], status)
        items.append(item)
    return items


def change_status(item_id, list_id):
    """
    Makes an api request to Trello to change the status of the selected item

    Args:
        item_id: The id of item that is being changed
        list_id: The id of the list that the item should be moved to
    """
    trello_details = Trello()
    requests.request("PUT",
                     f"https://api.trello.com/1/cards/{item_id}?key={trello_details.trello_key}&token={trello_details.trello_token}&idList={list_id}")


def add_item(list_id, title):
    """
    Adds a new item with the specified title and status.

    Args:
        list_id: The id of the list that the item is in.
        title: The title of the item.

    """
    trello_details = Trello()
    requests.post(
        f"https://api.trello.com/1/cards?idList={list_id}&key={trello_details.trello_key}&token={trello_details.trello_token}&name={title}")


def get_list_id(status):
    """
    Retrieves the list id for a list with a given status
    Args:
        status: The status of the item in a string

    Returns:
        str: the list id for the given status

    """
    trello_details = Trello()
    for key, value in trello_details.lists.items():
        if value == status:
            return key
