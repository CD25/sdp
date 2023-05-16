import pytest


@pytest.fixture(scope="session")
def fxt_new_user():
    return {
        "email": "billybob@example.com",
        "firstname": "Billy",
        "lastname": "Bob",
        "password": "p@ssword123",
        "usertype": "student",
    }
