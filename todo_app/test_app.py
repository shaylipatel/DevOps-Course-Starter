import os
import pytest
import requests
from dotenv import load_dotenv, find_dotenv
from todo_app import app


@pytest.fixture
def client(monkeypatch):
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    monkeypatch.setattr(requests, 'get', stub)
    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client


class StubResponse:
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


def stub(url):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    test_trello_key = os.environ.get('TRELLO_KEY')
    test_trello_token = os.environ.get('TRELLO_TOKEN')

    if url == f"https://api.trello.com/1/boards/{test_board_id}/lists?key={test_trello_key}&token={test_trello_token}":
        fake_response_data = [{
            "id": "123abc",
            "name": "To Do",
            "cards": [{"id": "456", "name": "Test card"}]
        }]
        return StubResponse(fake_response_data)
    elif url == f"https://api.trello.com/1/boards/{test_board_id}/cards/open?key={test_trello_key}&token={test_trello_token}":
        fake_response_data = [{"idList":"123abc","id": "456", "name": "Test card"}]
        return StubResponse(fake_response_data)


    raise Exception(f'Integration test did not expect URL "{url}"')


def test_index_page(client):

    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()
