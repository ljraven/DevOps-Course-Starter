import requests 

def get_items():
    # This code sample uses the 'requests' library:
    # http://docs.python-requests.org
    url = "https://api.trello.com/1/boards/60103b91b643743d059ee1bb/cards"

    query = {
    'key': 'fb08e8a1c59ad3a564b8db2418f9c697',
    'token': 'a842bc9d83091396464aa788df89e400015931af2f13bb2aaae9e2c5b673f1e2'
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