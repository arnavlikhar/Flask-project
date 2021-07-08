from flask import Flask,jsonify, request

app = Flask(__name__)

Contacts = [
    {
        'id': 1,
        'Contact':"9987644456",
        'Name':"Raju", 
        'done': False
    },
    {
        'id': 2,
        'Contact': '9876543222',
        'Name': 'Rahul', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please send the message!"
        },400)

    Contact = {
        'id': Contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    Contacts.append(Contact)
    return jsonify({
        "status":"success",
        "message": "message sent succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : Contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)