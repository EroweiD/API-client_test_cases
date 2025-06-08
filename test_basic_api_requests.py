import json

import requests


class diff_apiclient_requests:
    base_url = "https://reqres.in/"

    def __init__(self):
        self.header = {"X-API-KEY": "reqres-free-v1"
                       }

    def get_api_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url=url, headers=self.header)
        return response

    def post_api_request(self, endpoint, body):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url=url, headers=self.header, json=body)
        return response

    def patch_api_request(self, endpoint, body):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url=url, headers=self.header, json=body)
        return response

    def delete_api_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url=url, headers=self.header)
        return response
