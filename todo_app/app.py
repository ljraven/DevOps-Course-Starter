from flask import render_template, Flask, redirect, request
from todo_app.data import session_items as session
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    all_items = session.get_items()
    return render_template('index.html', items = all_items)

@app.route('/add-todo', methods=['POST'])
def add_todo():
    item = request.form.get('name')
    session.add_item(item)
    return redirect('/')

#delete button
@app.route('/delete-todo', methods=['POST'])
def delete_todo():
    todo_id = request.form.get('todo_id')
    session.delete_todo(todo_id)
    return redirect('/')

#completed status
@app.route('/complete-todo', methods=['POST'])
def complete_todo():
    todo_id = request.form.get('todo_id')
    session.complete_todo(todo_id)
    return redirect('/')

#started status
@app.route('/started-todo', methods=['POST'])
def started_todo():
    todo_id = request.form.get('todo_id')
    session.started_todo(todo_id)
    return redirect("/")

@app.route('/update-todo', methods=['POST'])
def update_todo():
    item = request.form.get('todo_id')
    new_todo_value = request.form.get('title')
    new_status_value = request.form.get('status')
    session.update_item(item, new_todo_value, new_status_value)
    return redirect('/')


if __name__ == '__main__':
    app.run()