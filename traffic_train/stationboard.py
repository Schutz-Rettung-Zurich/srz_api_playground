import json
from textwrap import indent
import requests

url = "http://transport.opendata.ch/v1/stationboard?station=Flughafen"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

pretty_json = json.loads(response.text)
print (json.dumps(pretty_json, indent=4))

with open('stationboard.json', 'w', encoding='utf-8') as outfile:
    json.dump(pretty_json, outfile, ensure_ascii=False, indent=4)