import requests
import json

key = 'a9OP2jf04tL6ExMYMzucnqqxJA3cpV8EMhBrYA9H'
url = 'https://api.congress.gov/v3/bill/117/hr?api_key=a9OP2jf04tL6ExMYMzucnqqxJA3cpV8EMhBrYA9H'

def fetch_data():
    res = requests.get(url)
    response = json.loads(res.text)
    print(response)

# def fetch_data():
#     fetch(url, {
#         headers:{
#             'Accept': 'application/json',
#             'X-Requested-With': 'XMLHttpRequest',
#         },
#     })
#     .then(response => {
#         return response.json()
#     })
#     .then(data => {
#         print(data)
#     })