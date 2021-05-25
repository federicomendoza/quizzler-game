import requests

opentdb_request_params = {'amount': '20', 'type': 'boolean', 'category': '18'}
response = requests.get(url="https://opentdb.com/api.php", params=opentdb_request_params)
response.raise_for_status()

question_data = response.json()["results"]
