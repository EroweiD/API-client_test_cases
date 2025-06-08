import json
import uuid
import pytest
import http
from test_basic_api_requests import diff_apiclient_requests


@pytest.fixture(scope="module")
def api_client():
    return diff_apiclient_requests()


def test_get_request(api_client):
    response = api_client.get_api_request("api/users")
    json_str = json.dumps(response.json(), indent=4)
    print(json_str)
    assert response.status_code == http.HTTPStatus.OK


def test_post_request(api_client, user_create_data):
    user_data = user_create_data.get("new_user", {})
    unique_name = f"{uuid.uuid4()}"
    user_data["name"] = unique_name
    unique_job = f"{uuid.uuid4()}"
    user_data["job"] = unique_job
    response = api_client.post_api_request("api/users", user_data)
    json_str = json.dumps(response.json(), indent=4)
    print(json_str)
    assert response.status_code == http.HTTPStatus.CREATED


def test_patch_request(api_client):
    body = {"name": "morpheus",
            "job": "soulfinder"}
    response = api_client.patch_api_request("api/users", body)
    json_str = json.dumps(response.json(), indent=4)
    print(json_str)
    assert response.status_code == http.HTTPStatus.CREATED
    assert response.json()["job"] == "soulfinder"


def test_delete_request(api_client):
    response = api_client.delete_api_request("api/users/1")
    assert response.status_code == http.HTTPStatus.NO_CONTENT
