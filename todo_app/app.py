from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.trello_items import Trello

app = Flask(__name__)
app.config.from_object(Config())
trello = Trello()

@app.route('/')
def index():
    items = trello.get_items()
    return render_template('index.html', items=items)


@app.route('/items/new', methods=['POST'])
def new_item():
    title = request.form.get('item_title')
    status = request.form.get('status')
    trello.add_item(status, title)
    return redirect(url_for('index'))


@app.route('/<item_id>/done', methods=['POST'])
def move_to_done(item_id):
    trello.change_status(item_id, status='Done')
    return redirect(url_for('index'))


@app.route('/<item_id>/in_progress', methods=['POST'])
def move_to_in_progress(item_id):
    trello.change_status(item_id, status='In Progress')
    return redirect(url_for('index'))


@app.route('/<item_id>/to_do', methods=['POST'])
def move_to_to_do(item_id):
    trello.change_status(item_id, status='To Do')
    return redirect(url_for('index'))
