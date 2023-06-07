import pytest

@pytest.mark.django_db
def test_list_ads(client):
    url = '/ad/'
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) > 0  # Проверяем, что получен список объявлений
