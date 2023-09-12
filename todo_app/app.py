from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config
# from todo_app.data.session_items import get_items, add_item
from todo_app.data.trello_items import get_item, get_items, get_lists

app = Flask(__name__)
app.config.from_object(Config())

board_id = os.getenv(TRELLO_BOARD_ID)
trello_token = os.getenv(TRELLO_TOKEN)
trello_key = os.getenv(TRELLO_KEY)
list_names = get_lists(board_id, trello_token, trello_key)

@app.route('/')
def index():
    items = get_items(board_id, trello_token, trello_key, list_names)
    return render_template('index.html', items=items)

# @app.route('/items/new', methods=['POST'])
# def new_item():
#     title = request.form.get('item_title')
#     add_item(title)
#     return redirect(url_for('index'))