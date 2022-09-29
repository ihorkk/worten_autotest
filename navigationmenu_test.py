from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Disable annoying notifications in browser
option = Options()
option.add_argument('--disable-notifications')

s = Service('D:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=option)
driver.maximize_window()
url = "https://www.worten.pt"

# Go to site
driver.get(url)

# Accept cookies
acceptcookies = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((
        By.CSS_SELECTOR, "button[class*=w-button-primary]"))).click()

# Navigation menu test
expectedresult_list = ['Diretório de Categorias',
                     'Promoções',
                     'Novidades Tecnológicas',
                     'Serviços Worten Resolve',
                     'Prestadores de Serviços e Profissionais Zaask',
                     'Lojas',
                     'Outlet',
                     'Worten Business | Worten para Empresas e Negócios']
actualresult_list = []
for indx in range(8):
    button1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li[class*=nav-item-first]")))
    button1[indx].click()
    actualresult = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*=w-breadcrumbs__text-big-name]"))).text
    actualresult_list.append(actualresult)
assert expectedresult_list == actualresult_list, f"Names do not match \nActualResult is: {actualresult_list}"
driver.quit()
