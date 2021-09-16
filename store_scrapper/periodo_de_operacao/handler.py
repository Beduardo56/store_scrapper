from selenium import webdriver
import time
import pandas as pd

def find_hour_operation(store_data: pd.DataFrame) -> pd.DataFrame:
    """This functions aims to get periods information about some store in google search

    Args:
        store_data (pd.DataFrame): DataFrame with store name and shopping name: required_columns: 'nome' and 'shopping'

    Returns:
        pd.DataFrame: Data containing periods information about passed stores,
                      columns: dia da semana, periodo de funcionamento e store_id(store_data index)
    """
    browser = webdriver.Chrome('store_scrapper/chromedriver')
    hour_data = pd.DataFrame()
    for index in store_data.index:
        nome = store_data.at[index, 'nome']
        shopping = store_data.at[index, 'shopping']
        shopping = shopping.replace(" ", "+")
        search_name = nome.lower() + "+" + shopping
        browser.get(f'https://www.google.com/search?channel=fs&client=ubuntu&q={search_name}')
        try:
            browser.find_element_by_xpath("//*[@id='kp-wp-tab-overview']/div[1]/div/div/div/div/div[7]/div/div/div[1]/div[1]/span/span/span/span").click()
            element = browser.find_element_by_xpath("//*[@id='kp-wp-tab-overview']/div[1]/div/div/div/div/div[7]/div/div")
            hour_data_store = pd.read_html(element.get_attribute('innerHTML'))[0]
            hour_data_store.rename({0: 'dia da semana', 1: 'periodo de funcionamento'}, axis=1, inplace=True)
            hour_data_store['store_id'] = index
            hour_data = pd.concat([hour_data, hour_data_store])
            time.sleep(0.2)
        except Exception: 
            pass
    browser.close()
    return hour_data
