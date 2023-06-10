import pytest


@pytest.fixture()
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test"
    password = "test"

    django_user_model.objects.create_user(username=username, password=password, role="admin")

    response = client.post("/token/", {"username": username, "password": password}, format='json')

    return response.data.get("access")


@pytest.fixture()
@pytest.mark.django_db
def user_access_token(client, django_user_model):
    username = "test"
    password = "test"

    new_user = django_user_model.objects.create_user(username=username, password=password, role="admin")

    response = client.post("/token/", {"username": username, "password": password}, format='json')

    return new_user, response.data.get("access")