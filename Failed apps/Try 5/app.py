from flask import Flask,render_template,request,redirect,url_for
import requests
from markupsafe import escape

app= Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html")
'''
@app.route("/whoami",methods=["GET"])
def whoami(firstname, lastname, self):
    self.firstname = 'Ahmet'
    self.lastname = 'Ucan'
    return redirect(url_for('whoami',self.firstname,self.lastname)
'''

@app.route("/alert", methods = ["POST"])
def alert():
    return render_template('alert.html')



if __name__ == "__main__":
    app.run(debug=True)
