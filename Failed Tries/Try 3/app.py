import json
import requests
endpoint = "http://127.0.0.1:5000/alert"
myData = {"firstname":"Ahmet","lastname":"Ucan"}
'''
r = requests.get(endpoint, params=json.dumps(myData))
r.status_code
print(r.status_code)
print(r.url)
endpoint2="http://caseapiahmetucan.cf/alert"
r2 = requests.post(endpoint2, data=json.dumps(myData))
print(r2.status_code)
print(r2.url)
'''
#endpoint3 = "https://caseapi.bestcloudfor.me/whoami?firstname=ali&lastname=veli"
r3 = requests.post(endpoint, data = json.dumps(myData))
print(r3.status_code)
print(r3.url)
