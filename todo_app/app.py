from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/items/new', methods=['POST'])
def new_item():
    title = request.form.get('title_name')
    add_item(title)
    return redirect(url_for('index'))