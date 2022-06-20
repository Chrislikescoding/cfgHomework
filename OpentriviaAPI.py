import requests
from pprint import pprint

url = 'https://opentdb.com/api.php'

parameters = {
    "amount": 10,
    "type": "multiple"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]

pprint(question_data)





