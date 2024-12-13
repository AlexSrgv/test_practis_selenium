import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from functions import get_root_path

download_path = get_root_path("data/download")

@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_path
    }
    options.add_argument("--window-size=1600,1000")  # размер окна
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--headless")   # без окна браузера
    # options.add_argument("--incognito")  # режим инкогнито
    # options.add_argument("--disable-cache")  # режим без хеша
    # options.add_argument("--start-maximized")   #v regime max okna
    #options.add_argument("--ignor-certificate-error") #zapusk bez sertificata
    # options.page_load_strategy = "normal" #skorost zagruzki stranici
    # options.page_load_strategy = 'eager'
    # options.page_load_strategy = "none"
    driver = webdriver.Chrome(service=service, options=options)
    # driver.set_window_size(900, 600)  #sm punkt 10
    # driver.maximize_window()  #sm punkt 14
    yield driver
    driver.quit()