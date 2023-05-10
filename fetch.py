import requests
import json
from pathlib import Path
from secret import key


url = f'https://api.congress.gov/v3/bill/117/hr?api_key={key}'

def fetch_data():
    res = requests.get(url)
    response = res.json()
    json_data = json.dumps(response, indent=4)
    bill = Path('./bill_data.json')

    if not bill:
        open('bill_data.json', 'x')
    else:
        with open('bill_data.json', 'w') as outfile:
            outfile.write(json_data)
