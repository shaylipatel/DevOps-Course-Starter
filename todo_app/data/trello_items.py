import requests


# board_id = os.getenv(TRELLO_BOARD_ID)
# trello_token = os.getenv(TRELLO_TOKEN)
# trello_key = os.getenv(TRELLO_KEY)


def get_items(board_id, trello_token, trello_key, list_names):
    """
    Fetches all saved items from the session.

    Args:
        board_id:
        trello_token:
        trello_key:
        list_names:

    Returns:
        list: The list of saved items.
    """

    trello_get_cards_api = requests.get(
        f"https://api.trello.com/1/boards/{board_id}/cards/open?key={trello_key}&token={trello_token}").json()
    items = _select_fields(trello_get_cards_api, list_names)
    return items


def _select_fields(data, list_names):
    items = []
    for record in data:
        id = record['id']
        list_id = record["idList"]
        status = list_names[list_id]
        new_item = {"id": id, "status": status, "title": record['name']}
        items.append(new_item)
    return items


def get_lists(board_id, trello_token, trello_key):
    trello_lists_api = requests.get(
        f"https://api.trello.com/1/boards/{board_id}/lists?key={trello_key}&token={trello_token}").json()
    list_names = {}
    for list_name in trello_lists_api:
        list_names[list_name['id']] = list_name['name']
    return list_names


def change_status(item_id, trello_token, trello_key, list_id):
    requests.request("PUT", f"https://api.trello.com/1/cards/{item_id}?key={trello_key}&token={trello_token}&idList={list_id}")
def add_item(trello_token, trello_key, list_id, title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    requests.post(f"https://api.trello.com/1/cards?idList={list_id}&key={trello_key}&token={trello_token}&name={title}")


def get_list_id(list_names, status):
    for key, value in list_names.items():
        if value == status:
            return key

#
# def save_item(item):
#     """
#     Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.
#
#     Args:
#         item: The item to save.
#     """
