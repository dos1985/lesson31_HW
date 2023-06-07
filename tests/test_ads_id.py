import pytest

@pytest.mark.django_db
def test_retrieve_ad(client):
    ad_id = 1  # Идентификатор объявления, которое нужно получить
    url = f'/ad/{int:pk}/'
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == ad_id  # Проверяем, что получено объявление с правильным идентификатором
