import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '4bea06a7fb33aa8bb5adb5f8d0cb07af'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 2632})
    assert response.status_code == 200
                          

def test_part_of_body():
    response = requests.put(f'{host}/trainers', headers={"trainer_token": token}, 
                            json={"name": "ThissKisss", "city": "Tokyo"})
    assert response.json()['message'] == 'Информация о тренере обновлена' 

@pytest.mark.parametrize('key, value', [("trainer_name", "ThissKisss"), 
                                       ("id", "2632"),
                                       ("city", "Tokyo")])
def test_response_json(key, value):
    response = requests.get(f'{host}/trainers', params={'trainer_id': 2632})
    assert response.json()[key] == value
