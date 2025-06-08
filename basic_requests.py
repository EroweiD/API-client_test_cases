import json

import requests
from requests import request


def test_get_request1():
    response = requests.get("https://www.youtube.com/")
    assert response.status_code == 200


def test_get_request2():
    base_url = "https://gorest.co.in"
    url = "/public/v2/users"
    header = {"Authentication": "Bearer 30b8edb25c6738ae81dc241a33720d9a4082346a9ab6de181067ebc080dc7163"}
    response = requests.get(base_url + url, headers=header)
    print(response.json())
    assert response.status_code == 200


def test_get_request3():
    base_url = "https://gorest.co.in"
    url = "/public/v2/users"
    header = {"Authentication": "Bearer 30b8edb25c6738ae81dc241a33720d9a4082346a9ab6de181067ebc080dc7163"}
    response = requests.get(base_url + url + "/7931896", headers=header)
    print(response.json())
    assert response.status_code == 200


def test_post_request():
    base_url = "https://gorest.co.in"
    url = "/public/v2/users"
    header = {"Authorization": "Bearer 30b8edb25c6738ae81dc241a33720d9a4082346a9ab6de181067ebc080dc7163"}
    body = {"name": "Annthony",
            "gender": "male",
            "email": "tenali.ramakrishna411@15ce.com",
            "status": "active"
            }
    response = requests.post(base_url + url, headers=header, json=body)
    print(response.json())
    assert response.status_code == 201


def test_put_request():
    base_url = "https://gorest.co.in"
    url = "/public/v2/users"
    header = {"Authorization": "Bearer 30b8edb25c6738ae81dc241a33720d9a4082346a9ab6de181067ebc080dc7163"}
    body = {"id": 7931880,
            "name": "Annthony",
            "gender": "male",
            "email": "tenali.ramakrishna421@15ce.ca",
            "status": "inactive"
            }
    response = requests.post(base_url + url, headers=header, json=body)
    print(response.json())
    assert response.status_code == 201


def test_get_param_request():
    base_url = "https://gorest.co.in"
    url = "/public/v2/users"
    parameters = {"page": 3,
                  "per_page": 2
                  }
    response = requests.get(base_url + url, params=parameters)
    json_str = json.dumps(response.json(), indent=3)
    print(json_str)

    assert response.status_code == 200


def test_post_request_with_fileopen():
    base_url = "https://reqres.in"
    head = {"X-API-KEY": "reqres-free-v1",
        "Content-type": "application/json"}
    url = "/api/users"
    json_file = open("./user_input_credentials.json")
    json_body = json.load(json_file)
    response = requests.post(base_url + url, headers=head, json=json_body)
    json_str = json.dumps(response.json(), indent=1)
    print(json_str)
    assert response.status_code == 201
