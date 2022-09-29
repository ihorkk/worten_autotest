from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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


# Hover button "Grandes Eletrodomésticos"

    # MÁQUINAS DE ROUPA

expectedresult_list = ['Máquinas de Roupa\nVer todos\nMáquinas de Lavar Roupa\nMáquinas de Secar Roupa\nMáquinas de Lavar e Secar Roupa\nMáquinas de Roupa de Encastrar\nAcessórios Máquinas de Roupa']
actualresult_list = []
hoverbutton = driver.find_element(By.CSS_SELECTOR, "label[for=nav-level-1030599603-0]")
ActionChains(driver).move_to_element(hoverbutton).perform()
button1 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((
        By.CSS_SELECTOR, "a[href*=como-escolher-maquinas-roupa]"))).click()
actualresult = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class*=menu]"))).text
actualresult_list.append(actualresult)
assert actualresult_list == expectedresult_list, f"Names do not match \nActualResult is: {actualresult_list}"

    # MÁQUINAS DE LOIÇA

expectedresult_list = ['Máquinas de Loiça\nVer todos\nMáquinas de Lavar Loiça\nAcessórios Máquinas de Loiça']
actualresult_list = []
hover_produtos = driver.find_element(By.CSS_SELECTOR, "li[class*=js-nav-products]")
ActionChains(driver).move_to_element(hover_produtos).perform()
hoverbutton1 = driver.find_element(By.CSS_SELECTOR, "label[for=nav-level-1030599603-0]")
ActionChains(driver).move_to_element(hoverbutton1).perform()
button_loica = driver.find_element(By.CSS_SELECTOR, "a[href*=como-escolher-maquinas-loica]").click()
actualresult = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class*=menu]"))).text
actualresult_list.append(actualresult)
assert actualresult_list == expectedresult_list, f"Names do not match \nActualResult is: {actualresult_list}"

    # FOGÕES

expectedresult_list = ['Fogões\nVer todos\nFogões a Gás\nFogões Elétricos\nFogões Mistos\nFogões Semi-Industriais\nFogões Portáteis\nAcessórios Fogões']
actualresult_list = []
hover_produtos = driver.find_element(By.CSS_SELECTOR, "li[class*=js-nav-products]")
ActionChains(driver).move_to_element(hover_produtos).perform()
hoverbutton1 = driver.find_element(By.CSS_SELECTOR, "label[for=nav-level-1030599603-0]")
ActionChains(driver).move_to_element(hoverbutton1).perform()
button_fogoes = driver.find_element(By.CSS_SELECTOR, "a[href*=como-escolher-fogoes]").click()
actualresult = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class*=menu]"))).text
actualresult_list.append(actualresult)
assert actualresult_list == expectedresult_list, f"Names do not match \nActualResult is: {actualresult_list}"
driver.quit()
