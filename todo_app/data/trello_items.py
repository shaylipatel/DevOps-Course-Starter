import requests

_DEFAULT_ITEMS = []


# board_id = os.getenv(TRELLO_BOARD_ID)
# trello_token = os.getenv(TRELLO_TOKEN)
# trello_key = os.getenv(TRELLO_KEY)


def get_items(board_id, trello_token, trello_key, list_names):
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """

    trello_get_cards_api = requests.get(
        f"https://api.trello.com/1/boards/{board_id}/cards/open?key={trello_key}&token={trello_token}").json()
    items = _select_fields(trello_get_cards_api, list_names)
    return items


def _select_fields(data, list_names):
    for record in data:
        id = record['id']
        vals = [list['id'] for list in _DEFAULT_ITEMS]
        if id not in vals:
            title = record['name']
            list_id = record["idList"]
            status = list_names[list_id]
            new_item = {"id": id, "status": status, "title": title}
            _DEFAULT_ITEMS.append(new_item)
    return _DEFAULT_ITEMS.copy()


def get_lists(board_id, trello_token, trello_key):
    trello_lists_api = requests.get(
        f"https://api.trello.com/1/boards/{board_id}/lists?key={trello_key}&token={trello_token}").json()
    list_names = {}
    for list_name in trello_lists_api:
        list_names[list_name['id']] = list_name['name']
    return list_names


# def get_item(id):
#     """
#     Adds a new item with the specified title to the session.
#
#     Args:
#         title: The title of the item.
#
#     Returns:
#         item: The saved item.
#     """
#
#
# def add_item(title):
#     """
#     Adds a new item with the specified title to the session.
#
#     Args:
#         title: The title of the item.
#
#     Returns:
#         item: The saved item.
#     """
#
#
# def save_item(item):
#     """
#     Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.
#
#     Args:
#         item: The item to save.
#     """
