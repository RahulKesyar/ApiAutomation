from endpoints.user_endpoints import UserEndpoints

class TestUsers:
    def setup_method(self):
        self.user_api = UserEndpoints()

    def test_get_user_success(self):
        response = self.user_api.get_single_user(2)
        assert response.status_code == 200
        assert response.json()["data"]["first_name"] == "Janet"

    def test_create_user(self):
        response = self.user_api.create_user("Rahul", "QA Engineer")
        assert response.status_code == 201
        assert response.json()["name"] == "Rahul"