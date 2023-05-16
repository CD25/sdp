from exampractise import app


def test_user_signup():
    """For checking user signup"""
    response = app.test_client().post("/signup")
    assert response.status_code == 201


def test_user_login():
    """For checking user login"""
    response = app.test_client().post("/login")
    assert response.status_code == 200


def test_user_logout():
    """For checking user logout"""
    response = app.test_client().post("/logout")
    assert response.status_code == 200
