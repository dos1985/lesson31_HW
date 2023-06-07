import pytest

@pytest.mark.django_db
def test_create_ad(client):
    url = '/ad/'
    data = {
        "name": "Стол из слэба и эпоксидной клея",
        "author": 1,
        "price": 100,
        "description": "Описание объявления",
        "is_published": False,
        "category": 1
    }

    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data["name"] == "Стол из слэба и эпоксидной клея"
