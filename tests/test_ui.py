import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://localhost:3000")
    yield driver
    driver.quit()

def test_sort_by_title_and_last_movie(driver):
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, "//a[normalize-space()='The Phantom Menace']").text == "The Phantom Menace"

def test_species_contains_wookie(driver):
    time.sleep(10)
    driver.find_element(By.LINK_TEXT, "The Empire Strikes Back").click()
    time.sleep(10)
    species_block = driver.find_element(By.CSS_SELECTOR, "body > section:nth-child(1) > main:nth-child(3) > div:nth-child(2) > div:nth-child(3)").text
    species_list = species_block.split("\n")
    assert "Wookie" in species_list

def test_camino_not_in_phantom_menace(driver):
    time.sleep(10)
    driver.find_element(By.LINK_TEXT, "The Phantom Menace").click()
    time.sleep(10)
    planets_block = driver.find_element(By.CSS_SELECTOR, "div[class='layout_lists__rBjPn'] div:nth-child(2)").text
    planet_names = planets_block.split("\n")
    assert "Camino" not in planet_names
