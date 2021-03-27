from flask import Flask, request,jsonify

app = Flask(__name__)




@app.route("/")
def ana_sayfa():
    return {"firstname":"Ahmet","lastname":"Ucan"}

@app.route("/whoami", methods=["GET"])
def whoami():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    return jsonify(firstname =firstname, lastname=  lastname),200


@app.route('/alert', methods=['POST'])
def alert():

    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']



    return jsonify({'firstname':firstname,'lastname':lastname}),200




if __name__ == "__main__":
   app.run(host="0.0.0.0", port=int("5000"), debug=True)
