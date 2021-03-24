import json
import requests
from flask import Flask,render_template, request,url_for,redirect,jsonify

app = Flask(__name__)

person_dict = {"firstname":"Ahmet",
               "lastname":"Ucan"
               }
result = json.dumps(person_dict)

@app.route("/")
def ana_sayfa():
    return result

@app.route("/whoami", methods=["GET"])
def whoami():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    return jsonify(firstname =firstname, lastname=  lastname),200

    #return render_template('whoami.html')


@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()

    firstname = data['firstname']
    lastname = data['lastname']



    return jsonify({'firstname':firstname,'lastname':lastname}),200








if __name__ == "__main__":
    app.run(debug=True)
