import json
import requests

family  = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
# file_json = json.dumps(family)
# print(file_json)
response = requests.get("http://api.open-notify.org/iss-now.json")
# Print the content of the response.
print(response.status_code)
response = requests.get("http://api.open-notify.org/astros.json")
data = response.text
print(response.request.url)
print(response.request.body)

response  = requests.get("https://api.chucknorris.io/")
data = response.text
print(response.url)
print(response.headers)
print(response.content)
print(response.status_code)
print(response.text)
print(response.cookies.items)