from selenium import webdriver
import pandas as pd
from time import sleep

from store_scrapper.shopping_scrapper.base import BaseShoppingScrapper

class ShoppingVitoria(BaseShoppingScrapper):
    def __init__(self):
        super().__init__('shopping vitoria', 'https://www.shoppingvitoria.com.br/lojas')
    def run(self) -> pd.DataFrame:
        final_data = {'categoria': [], 'nome': [], 'telefone': []}
        browser = webdriver.Chrome('store_scrapper/chromedriver')
        browser.get(self.base_url)
        for i in range(0, 20):
            browser.find_element_by_xpath("//*[@id='ver_mais']").click()
            sleep(0.3)
        elements = browser.find_elements_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/ul/li[@style='display: list-item;']")
        for element in elements:
            store = element.text
            fields = store.split('\n')
            final_data['categoria'].append(fields[0])
            final_data['nome'].append(fields[1])
            final_data['telefone'].append(fields[-1])
        browser.close()
        store_data = pd.DataFrame(final_data)
        return store_data
