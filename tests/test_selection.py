import pytest

@pytest.mark.django_db
def test_create_selection(client):
    url = '/selection/'
    data = {
        "name": "Моя подборка",
        "description": "Описание моей подборки",
        "ads": [1, 2, 3]  # Список идентификаторов объявлений, которые хотите добавить в подборку
    }

    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data["name"] == "Моя подборка"
    assert response.data["description"] == "Описание моей подборки"
    assert len(response.data["ads"]) == 3  # Проверяем, что объявления добавлены в подборку
