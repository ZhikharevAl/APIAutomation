import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users/2'

# Read Input Json File
file = open('C://Users/1/Desktop/CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT request with Json input body
response = requests.put(url, request_json)
print(response.content)

# Validating Response code
assert response.status_code == 200

#  Parse Response content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])
