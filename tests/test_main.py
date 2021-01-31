def test_access(test_main):
    response = test_main.get("/")
    assert response.status_code == 200


def test_login(test_main):
    response = test_main.get("/login")
    assert response.status_code == 200


def test_home(test_main):
    response = test_main.get("/home")
    assert response.status_code == 200


def test_setup(test_main):
    response = test_main.get("/setup")
    assert response.status_code == 200
