from cfg.constants import API_TEST_HOST as HOST


class Endpoints:
    """
    Class to store and manage API endpoint URLs.
    """
    create_user = f"{HOST}/users"
    get_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"
    update_user = lambda self, uuid: f"{HOST}/users/{uuid}"
    delete_user = lambda self, uuid: f"{HOST}/users/{uuid}"


