import pytest
from rest_framework import status


@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "Стол из дерева",
        "price": 200
    }

    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "Стол из дерева",
        "price": 200,
        "description": None,
        "image": None,
        "author": user.pk,
        "category": category.pk
    }

    response = client.post("/ad/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data


@pytest.mark.parametrize(
    "test_name, expected",
    [
        (
                "123456789", {"status": status.HTTP_400_BAD_REQUEST,
                              "message": "Ensure this field has at least 10 characters."}
        ),
        (
                "", {"status": status.HTTP_400_BAD_REQUEST,
                     "message": "This field may not be blank."}
        )
    ]
)
@pytest.mark.django_db
def test_ad_create_name_fail(client, user, category, access_token, test_name, expected):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": test_name,
        "price": 200
    }

    response = client.post("/ad/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == expected.get("status")
    assert expected.get("message") in str(response.data["name"][0])


@pytest.mark.django_db
def test_ad_create_price_fail(client, user, category, access_token):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "test_name",
        "price": -100
    }

    response = client.post("/ad/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Ensure this value is greater than or equal to 0." in str(response.data["price"][0])


@pytest.mark.django_db
def test_ad_create_is_published_fail(client, user, category, access_token):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "test_name",
        "price": 100,
        "is_published": True
    }

    response = client.post("/ad/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Нельзя создавать опубликованные объявления." in str(response.data["is_published"][0])