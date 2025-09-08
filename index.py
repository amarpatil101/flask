from flask import Flask, request 

app = Flask(__name__)

@app.route("/")
def home():
    return "home route"

#             👇 API endpoint
@app.route("/test", methods=["POST"])
def about():
    data = request.json
    print(data)
    return "about route"

@app.route("/update", methods=["put"])
def updateNote():
    return "Note Update Success"

@app.route("/remove", methods=["Delete"])
def removeNote():
    return "Note remove Success"

# server
app.run(debug=True)