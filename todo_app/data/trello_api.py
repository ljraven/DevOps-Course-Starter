import requests 
import os

def get_items():
    # This code sample uses the 'requests' library:
    # http://docs.python-requests.org
    url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/cards"

    query = {
    'key': os.getenv('TRELLO_KEY'),
    'token': os.getenv('TRELLO_TOKEN'),
    }

    response = requests.get(
    url,
    params=query
    )

    return response.json()


def add_item(title):
    pass 

def delete_item(todo_id):
    pass

def complete_item(todo_id):
    pass

def started_item(todo_id):
    pass

def update_title(new_todo_title, todo_id):
    pass