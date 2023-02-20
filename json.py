import json
import requests
response = requests.get('https://github.com/Beisenbek/programming-principles-2/blob/main/Lab4/json/sample-data.json')
response_json=json.loads(response.text)

for var in response_json:
    if var['mtu'] == 9150:
        print(response_json['dn','speed','mtu'])