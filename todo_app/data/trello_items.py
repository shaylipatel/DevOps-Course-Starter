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
        trello_lists_api = requests.get(
            f"https://api.trello.com/1/boards/{self.board_id}/lists?key={self.trello_key}&token={self.trello_token}").json()
        list_names = {}
        for list_name in trello_lists_api:
            list_names[list_name['id']] = list_name['name']
        return list_names


class Item(Trello):
    def __init__(self, id, name, status):
        super().__init__()
        self.id = id
        self.name = name
        self.status = status


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    trello_details = Trello()
    trello_get_cards_api = requests.get(
        f"https://api.trello.com/1/boards/{trello_details.board_id}/cards/open?key={trello_details.trello_key}&token={trello_details.trello_token}").json()
    items = _select_fields(trello_get_cards_api, trello_details.lists)
    return items


def _select_fields(data, list_names):
    items = []
    for record in data:
        list_id = record["idList"]
        status = list_names[list_id]
        item = Item(record['id'],record['name'], status)
        items.append(item)
    return items


def change_status(item_id, list_id):
    trello_details = Trello()
    requests.request("PUT",
                     f"https://api.trello.com/1/cards/{item_id}?key={trello_details.trello_key}&token={trello_details.trello_token}&idList={list_id}")


def add_item(list_id, title):
    """
    Adds a new item with the specified title to the session.

    Args:
        list_id: The id of the list that the item is in.
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    trello_details = Trello()
    requests.post(f"https://api.trello.com/1/cards?idList={list_id}&key={trello_details.trello_key}&token={trello_details.trello_token}&name={title}")


def get_list_id(status):
    trello_details = Trello()
    for key, value in trello_details.lists.items():
        if value == status:
            return key
