import pytest
from rest_framework import status


@pytest.mark.parametrize(
    "test_slug, expected",
    [
        ("123", {"status": status.HTTP_400_BAD_REQUEST,
                 "slug": "Ensure this field has at least 5 characters."}),
        ("12345678901", {"status": status.HTTP_400_BAD_REQUEST,
                         "slug": "Ensure this field has no more than 10 characters."})
    ]
)
@pytest.mark.django_db
def test_category_create_fail(client, test_slug, expected):
    data = {
        "name": "New category name",
        "slug": test_slug
    }

    response = client.post("/category/", data=data, format="json")

    assert response.status_code == expected.get("status")
    assert expected.get("slug") in str(response.data["slug"][0])


@pytest.mark.parametrize(
    "test_slug, expected",
    [
        (
                "1234567890", {"status": status.HTTP_201_CREATED}
        ),
        (
                "12345", {"status": status.HTTP_201_CREATED}
        )
    ]
)
@pytest.mark.django_db
def test_category_create_success(client, test_slug, expected):
    data = {
        "name": "New category name",
        "slug": test_slug
    }

    response = client.post("/category/", data=data, format="json")

    assert response.status_code == expected.get("status")