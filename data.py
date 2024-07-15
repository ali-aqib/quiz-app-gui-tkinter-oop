import requests

parameters = {
    # amount = no. of questions
    "amount": 15,
    # type = true or false
    "type": "boolean",
    # category 18 = computer science
    "category": 18
}
# Fetching questions from opentdb.com using API by passing the parameters
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
