import json
import requests
from flask import Flask,render_template, request,url_for,redirect,jsonify

app = Flask(__name__)

@app.route("/whoami", methods=["GET"])
def whoami():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    return jsonify(firstname =firstname, lastname=  lastname),200

if __name__ == "__main__":
    app.run(debug=True)
