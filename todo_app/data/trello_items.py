import requests
import os


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
            list_names[list_name['name']] = list_name['id']
        return list_names

    def get_items(self):
        """
        Fetches all items on Trello board via API

        Returns:
            list: The list of Trello items.
        """
        trello_get_cards_api = requests.get(
            f"https://api.trello.com/1/boards/{self.board_id}/cards/open?key={self.trello_key}&token={self.trello_token}").json()
        items = self._select_fields(trello_get_cards_api)
        return items

    def change_status(self, item_id, status):
        """
        Makes an api request to Trello to change the status of the selected item

        Args:
            item_id: The id of item that is being changed
            status: The new status
        """
        list_id = self._get_list_id(status)
        requests.request("PUT",
                         f"https://api.trello.com/1/cards/{item_id}?key={self.trello_key}&token={self.trello_token}&idList={list_id}")

    def add_item(self, status, title):
        """
        Adds a new item with the specified title and status.

        Args:
            status: The status for the new item.
            title: The title of the item.

        """
        list_id = self._get_list_id(status)

        requests.post(
            f"https://api.trello.com/1/cards?idList={list_id}&key={self.trello_key}&token={self.trello_token}&name={title}")

    def _get_list_id(self, status):
        """
        Retrieves the list id for a list with a given status
        Args:
            status: The status of the item in a string

        Returns:
            str: the list id for the given status

        """
        return self.lists.get(status)

    def _select_fields(self, data):
        """
        Iterates through the Trello api data and puts the item's name. status and id into a new class object
        Args:
            data: Trello api data in json format.

        Returns:
            list: List of Trello items.

        """
        items = []
        for record in data:
            list_id = record["idList"]
            for key, value in self.lists.items():
                if value == list_id:
                    status = key
            item = Item(record['id'], record['name'], status)
            items.append(item)
        return items


class Item:
    def __init__(self, item_id, name, status):
        self.id = item_id
        self.name = name
        self.status = status
