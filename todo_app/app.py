from flask import Flask, render_template, request, redirect, url_for
import os
from todo_app.flask_config import Config
# from todo_app.data.session_items import get_items, add_item
from todo_app.data.trello_items import get_items, add_item, get_list_id, change_status

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)


@app.route('/items/new', methods=['POST'])
def new_item():
    title = request.form.get('item_title')
    status = request.form.get('status')
    list_id = get_list_id(status)
    add_item(list_id, title)
    return redirect(url_for('index'))


@app.route('/<item_id>/done', methods=['POST','PUT','GET'])
def move_to_done(item_id):
    list_id = get_list_id('Done')
    change_status(item_id, list_id)
    return redirect(url_for('index'))


@app.route('/<item_id>/in_progress', methods=['POST','PUT','GET'])
def move_to_in_progress(item_id):
    list_id = get_list_id('In Progress')
    change_status(item_id, list_id)
    return redirect(url_for('index'))


@app.route('/<item_id>/to_do', methods=['POST','PUT', 'GET'])
def move_to_to_do(item_id):
    list_id = get_list_id('To Do')
    change_status(item_id, list_id)
    return redirect(url_for('index'))
