import os

@app.route('/')
def index():
    todos=[]

#Fetch all to-do items (cards) for the specified board
    cards_url = f"https://api.trello.com/1/boards/{os.getenv('Trello_Board_ID')}/cards"

    query = {
        'key': os.getenv('Trello_API_Key'),
        'token': os.getenv('Trello_API_Token')
        }

    response = requests.get(
        cards_url,
        params=query
        )
    trello_data=response.json()
    for trello_card in trello_data: 
        todos.append({"id": trello_card["id"], "status": get_status(trello_card["idList"]), "title": trello_card["name"]})
    print(trello_data)
    return render_template('index.html', items = todos)


def get_status(id):
    query = {
        'key': os.getenv('Trello_API_Key'),
        'token': os.getenv('Trello_API_Token')
        }
        
    status_url = f"https://api.trello.com/1/boards/{os.getenv('Trello_Board_ID')}/lists" #needs to be lists at the end see trello docs
    response=requests.get(
        status_url,
        params=query)
    
    statuses=response.json()
    for card_status in statuses:
        if card_status["id"]==id:
            return card_status["name"]
