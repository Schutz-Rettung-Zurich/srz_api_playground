import requests
import pandas as pd
import json

url = "https://apps.rescuetrack.com/api/routing/standard/v2/point-to-point"

payload = json.dumps({
  "start": [
    47.36629,
    8.49707
  ],
  "stop": [
    47.37015,
    8.519277
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'rt-sso-sid=f4ce5577-b294-43eb-b232-91e8f4a01ae8'
}

response = requests.request("POST", url, headers=headers, data=payload)

pretty_json = json.loads(response.text)
print (json.dumps(pretty_json, indent=2))

with open('routing.json', 'w', encoding='utf-8') as outfile:
    json.dump(pretty_json, outfile, ensure_ascii=False, indent=4)