import os
from typing import List
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def select_louer():
    """Click on the button louer."""
    driver.find_element_by_css_selector('#agatha_quest > div:nth-child(3) > div:nth-child(1) > label:nth-child(2)').click()

def fill_field_city(city: str):
    """Fill the field city with the city parameter.

    Keyword arguments:
    city -- the city's name to add in the field"""
    driver.find_element_by_css_selector('#agatha_autocomplete_autocompleteUI__input').send_keys(city)
    element = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.slam-aui-results-line:nth-child(1)')))
    city_name = element.get_attribute('textContent').strip()
    if city in city_name:
        print(city)
        element.click()
    else:
        response = requests.get("https://autocomplete.svc.groupe-seloger.com/api/v2.0/auto/complete/fra/63/10/8/SeLoger?text=asnier")
        print('Voici la liste des villes disponibles:')
        for display_name in [elt['Display'] for elt in response.json()]:
            print(display_name)
        select_louer()

def fill_field_city_with_several_cities(cities: List[str]):
    """Fill the field city with the all city in cities parameter.

    Keyword arguments:
    cities -- a list of the city's names to add in the field"""
    for city in cities:
        fill_field_city(city)

def uncheck_field_house():
    """Click on field house to unchek it (default is check)."""
    driver.find_element_by_css_selector('#agatha_biens > div:nth-child(3) > div:nth-child(1) > label:nth-child(2)').click()

def uncheck_field_appart():
    """Click on field appart to unchek it (default is check)."""
    driver.find_element_by_css_selector('#agatha_biens > div:nth-child(3) > div:nth-child(2) > label:nth-child(2)').click()


def confirm_search():
    """Click on button search to confirm """
    driver.find_element_by_css_selector('.b-btn').click()


if __name__ == "__main__":
    options = Options()
    options.headless = False
    executable_path_driver = os.path.join(os.path.dirname(__file__),'geckodriver')
    driver = webdriver.Firefox(options=options, executable_path=executable_path_driver)
    driver.get("https://seloger.com")
    select_louer()
    fill_field_city_with_several_cities(['Paris'])
    uncheck_field_house()
    uncheck_field_appart()
    confirm_search()
