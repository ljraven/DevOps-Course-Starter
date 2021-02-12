from flask import render_template, Flask, redirect, request
from todo_app.data import trello_api as trello
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    all_items = trello.get_items()
    return render_template('index.html', items = all_items)

@app.route('/add-todo', methods=['POST'])
def add_todo():
    title = request.form.get('name')
    trello.add_item(title)
    return redirect('/')

#delete button
@app.route('/delete-todo', methods=['POST'])
def delete_todo():
    todo_id = request.form.get('todo_id')
    trello.delete_item(todo_id)
    return redirect('/')

#completed status
@app.route('/complete-todo', methods=['POST'])
def complete_todo():
    todo_id = request.form.get('todo_id')
    trello.complete_item(todo_id)
    return redirect('/')

#started status
@app.route('/started-todo', methods=['POST'])
def started_todo():
    todo_id = request.form.get('todo_id')
    trello.started_item(todo_id)
    return redirect("/")

#update title
@app.route('/update-title', methods=['POST'])
def update_title():
    todo_id = request.form.get('todo_id')
    new_todo_title = request.form.get('title')
    trello.update_title(new_todo_title, todo_id)
    return redirect('/')

if __name__ == '__main__':
    app.run()