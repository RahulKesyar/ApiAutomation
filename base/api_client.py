import requests


class APIClient:
    def __init__(self):
        self.base_url = "https://reqres.in/api"

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response

    def post(self, endpoint, payload):
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload)
        return response