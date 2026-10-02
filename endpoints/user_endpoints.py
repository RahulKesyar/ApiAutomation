from base.api_client import APIClient


class UserEndpoints(APIClient):
    def get_single_user(self, user_id):
        return self.get(f"users/{user_id}")

    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        return self.post("users", payload)