import requests
import pytest

BASE_URL = "https://rickandmortyapi.com/api"

# Caso 1
def test_api_status():
    response = requests.get(BASE_URL + "/character")
    assert response.status_code == 200

# Caso 2 
def test_character_name():
    response = requests.get(BASE_URL + "/character/1")
    data = response.json()
    assert data["name"] == "Rick Sanchez"

# Caso 3
def test_character_not_found():
    response = requests.get(BASE_URL + "/character/99999")
    assert response.status_code == 404

# Caso 4
def test_episode_characters():
    response = requests.get(BASE_URL + "/episode/1")
    data = response.json()
    assert len(data["characters"]) > 0

# Caso 5
def test_location():
    response = requests.get(BASE_URL + "/location/1")
    data = response.json()
    assert data["name"] == "Earth (C-137)"

# Caso 6
def test_character_response_structure():
    response = requests.get(BASE_URL + "/character/1")
    data = response.json()
    expected_keys = {"id", "name", "status", "species", "type", "gender", "origin", "location", "image", "episode", "url", "created"}
    assert set(data.keys()) == expected_keys
