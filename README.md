# caseapi-ahmetucan-bestcloudforme


####Installation libraries

    pip install flask # terminal 
    
    from flask import Flask,jsonify,request import json
    
#### The process of mapping URLs to functions is called routing
    
    @app.route("/")  # Main Page
    @app.route("/whoami", methods=["GET"]) #/whomai Endpoint  # For workinkg the page with only GET requests
    @app.route('/alert', methods=['POST']) #/alert Endpoint   # For workinkg the page with only POST requests
    
#### request
    firstname = request.args.get("firstname")  # For whoami endpoint static code url parameters 
    lastname = request.args.get("lastname")
    
#### jsonify 

    return jsonify(firstname =firstname, lastname=  lastname),200
    
#### App Run
    if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1", port=int("5000")) # when publish the api must be "debug = False"


# Docker 

# Build image :

    Docker image build -t ahmetucan/caseapi .

# Run a Container:

    Dockercontainer run -p 80:5000 ahmetucan/caseapi

 
 
