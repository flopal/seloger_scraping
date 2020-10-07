"""SearchSeLogerModule : contains class to search on the site seloger.com"""

import os
from typing import List
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class SearchSeLoger(object):
    """SearchSeLoger is a class that automates the search for goods on the site seloger.com."""


    def __init__(self, headless: bool):
        """Initialize selenium driver

        Keyword argument:
        headless -- display navigator (false) or not (true)
        """
        options = Options()
        options.headless = headless
        executable_path_driver = os.path.join(os.path.dirname(__file__),'geckodriver')
        self.driver = webdriver.Firefox(options=options, executable_path=executable_path_driver)
        self.driver.get("https://seloger.com")
        self.isLouer = False
        self.isConfirm = False


    def select_louer(self):
        """Click on the button louer."""
        self.driver.find_element_by_css_selector('#agatha_quest > div:nth-child(3) > div:nth-child(1) > label:nth-child(2)').click()
        self.isLouer = True


    def select_acheter(self):
        """Click on the button acheter."""
        self.driver.find_element_by_css_selector('#agatha_quest > div:nth-child(3) > div:nth-child(2) > label:nth-child(2)').click()
        self.isLouer = False


    def fill_field_city(self,city: str):
        """Fill the field city with the city parameter.

        Keyword arguments:
        city -- the city's name to add in the field"""
        self.driver.find_element_by_css_selector('#agatha_autocomplete_autocompleteUI__input').send_keys(city)
        element = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.slam-aui-results-line:nth-child(1)')))
        city_name = element.get_attribute('textContent').strip()
        if city in city_name:
            print(city)
            element.click()
        else:
            response = requests.get("https://autocomplete.svc.groupe-seloger.com/api/v2.0/auto/complete/fra/63/10/8/SeLoger?text=" + city)
            print('Voici la liste des villes disponibles:')
            for display_name in [elt['Display'] for elt in response.json()]:
                print(display_name)
            if self.isLouer:
                self.select_louer()
            else:
                self.select_acheter()


    def fill_field_city_with_several_cities(self, cities: List[str]):
        """Fill the field city with the all city in cities parameter.

        Keyword arguments:
        cities -- a list of the city's names to add in the field"""
        for city in cities:
            self.fill_field_city(city)


    def uncheck_field_house(self):
        """Click on field house to unchek it (default is check)."""
        self.driver.find_element_by_css_selector('#agatha_biens > div:nth-child(3) > div:nth-child(1) > label:nth-child(2)').click()


    def uncheck_field_appart(self):
        """Click on field appart to unchek it (default is check)."""
        self.driver.find_element_by_css_selector('#agatha_biens > div:nth-child(3) > div:nth-child(2) > label:nth-child(2)').click()


    def confirm_search(self):
        """Click on button search to confirm """
        self.driver.find_element_by_css_selector('.b-btn').click()
        self.isConfirm = True


    def number_of_rooms(self, number:int):
        """"""
        if not self.isConfirm:
            return
        self.driver.find_element_by_css_selector('.search_bar_room > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1)').click()
        if number < 2:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div[5]/div[2]/div[2]/div[24]/div/div[1]/label').click()
        elif number >= 5:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div[5]/div[2]/div[2]/div[24]/div/div[5]/label').click()
        else:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div[5]/div[2]/div[2]/div[24]/div/div[' + str(number) + ']/label').click()
        self.driver.find_element_by_css_selector('.search_bar_room > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1)').click()
