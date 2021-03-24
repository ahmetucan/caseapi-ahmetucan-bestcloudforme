from flask import Flask
import json 
person_dict = {
    "firstname" : "Ahmet",
    "lastname" : "UCAN"
}
result = json.dumps(person_dict)
app = Flask(__name__)

@app.route('/')
def baslangic_api():
    return result

#@app.route('/whoami',method = 'GET')
# def baslangic_api():
    # return result


# @app.route('/alert',method = 'POST')
# def baslangic_api():
    # return result




if __name__ == "__main__":
    app.run()