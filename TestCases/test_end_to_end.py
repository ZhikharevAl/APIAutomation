import requests
import json
import jsonpath


def test_add_new_data():
    app_url = ""
    f = open('', 'r')
    requests_json = json.loads(f.read())
    response = requests.post(app_url, requests_json)
    id = jsonpath.jsonpath(reponse.json(), 'id')
    print(id[0])

    tech_api_url = ""
    f = open('', 'r')
    requests_json = json.loads(f.read())
    requests_json['id'] = int(id[0])
    requests_json['st_id'] = id[0]
    response = requests.post(tech_api_url, requests_json)
    print(response.text)

    add_api_url = ""
    f = open('', 'r')
    requests_json = json.loads(f.read())
    requests_json['st_id'] = id[0]
    response = requests.post(add_api_url, requests_json)

    final_details = "" + str(id[0])
    response = requests.get(final_details)
    print(response.text)
