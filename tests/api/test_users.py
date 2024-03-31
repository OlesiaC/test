import allure
import pytest
from tests.api.base import BaseTest


@allure.epic("Admin API")
@allure.suite("Users API")
class TestUsers(BaseTest):

    @allure.title("Create, update, delete user")
    @pytest.mark.regression
    @pytest.mark.api
    def test_create_update_delete_user(self):
        self.api_users.create_user()
        self.api_users.get_user_by_id(12)
        self.api_users.update_user_by_patch(12)
        self.api_users.update_user_by_put(12)
        self.api_users.delete_user(12)



