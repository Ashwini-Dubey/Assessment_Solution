import requests
import json
import pytest

BASE_URL = "https://swapi-node.vercel.app/api"
Movies_EP = "/films"
Movies_3_EP  = "/films/3"
Movies_5_EP  = "/films/5"
People_EP = "/people"

def send_get_request(base_url:str,endpoint:str):
    url = f"{base_url}{endpoint}"
    return requests.get(url, timeout=10)

def test_films_count_is_6():
    """/films should list exactly 6 movies."""
    data = send_get_request(BASE_URL, Movies_EP).json()
    count = data.get("count")
    assert count == 6, f"Expected 6 films, got {count}"

def test_third_film_director():
    film = send_get_request(BASE_URL, Movies_3_EP).json().get("fields", {})
    assert film["director"] == "Richard Marquand", f"Unexpected director: {film['director']}"

def test_fifth_film_producers_exclude_names():
    producers = send_get_request(BASE_URL, Movies_5_EP).json()["fields"]["producer"]
    assert "Gary Kurtz" not in producers and "George Lucas" not in producers, producers




