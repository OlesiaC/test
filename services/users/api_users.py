import allure
import requests

from services.users.models import user_model
from utils.helper import Helper
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints


class UsersAPI(Helper):
    """Class for interacting with user-related API endpoints"""
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()

    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            json=self.payloads.create_user
        )
        assert response.status_code == 201, response.json()
        self.attach_response(response.json())
        model = user_model.UserCreatedModel(**response.json())
        return model

    @allure.step("Get Single User by ID")
    def get_user_by_id(self, user_id):
        response = requests.get(
            url=self.endpoints.get_user_by_id(user_id),
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = user_model.GetUserByID(**response.json())
        return model

    @allure.step("Update user by PATCH method")
    def update_user_by_patch(self, user_id):
        response = requests.patch(
            url=self.endpoints.update_user(user_id),
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = user_model.UserUpdatedModel(**response.json())
        return model

    @allure.step("Update user by PUT method")
    def update_user_by_put(self, user_id):
        response = requests.put(
            url=self.endpoints.update_user(user_id),
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = user_model.UserUpdatedModel(**response.json())
        return model

    @allure.step("Delete user")
    def delete_user(self, user_id):
        response = requests.delete(
            url=self.endpoints.delete_user(user_id),
        )
        assert response.status_code == 204
        self.attach_response(response.status_code)
