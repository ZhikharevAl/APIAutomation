import requests
import json
import jsonpath

# API URL

url = 'https://reqres.in/api/users'

# Read Input Json File

file = open('C://Users/1/Desktop/CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with Json input body

response = requests.post(url, request_json)
print(response.content)

# Validating Response code
assert response.status_code == 201

# Fetch Header from response

print(response.headers)
print(response.headers.get('Content-Type'))

# Parse response to json format

response_json = json.loads(response.text)

# Pick id using Json Path

id = jsonpath.jsonpath(response_json, 'id')
print(id[0])
