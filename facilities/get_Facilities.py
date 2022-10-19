import requests
import pandas as pd
import json

url = "https://search.k8s.srz.els.loc/api/geo/v2/institutions/getData"

payload={}
headers = {
  'Cookie': 'ingresscookie-rescad=1666089565.541.25629.727648'
  'Content-Type': 'application/json',
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

json_string = response.text

with open('facilities/facilities.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_string, outfile, ensure_ascii=False, indent=4)