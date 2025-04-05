from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = Options()
options.add_argument("--headless")
service = Service("C:/Users/jhoib/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

url_base = "https://www.cacaushow.com.br/categoria/páscoa"
driver.get(url_base)
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "product-tile"))
)


while True:
    try:
        botao_mais = driver.find_element(By.CLASS_NAME, "more")
        driver.execute_script("arguments[0].scrollIntoView(true);", botao_mais)
        time.sleep(1)
        botao_mais.click()
        print("Carregando mais produtos...")
        time.sleep(3)
    except NoSuchElementException:
        print("Todos os produtos carregados.")
        break
    except Exception as e:
        print("Erro ao clicar no botao:", e)
        break

nomes = []
preco_normal = []
preco_lovers = []

produtos = driver.find_elements(By.CLASS_NAME, "product-tile")
print(f"{len(produtos)} produtos encontrados.")

for produto in produtos:
    try:
        nome = produto.find_element(By.CLASS_NAME, "pdp-link").text
        preco_lovers_val = produto.find_element(By.CLASS_NAME, "it__shelf__discountPrice").text
        preco_lovers_val = preco_lovers_val.replace("\n", " ").strip()
        try:
            preco_normal_val = produto.find_element(By.CLASS_NAME, "strike-through").text
            preco_normal_val = preco_normal_val.replace("\n", " ").strip()
        except:
            preco_normal_val = preco_lovers_val

        nomes.append(nome)
        preco_normal.append(preco_normal_val)
        preco_lovers.append(preco_lovers_val)

    except Exception as e:
        print("Erro ao extrair produto:", e)
        continue

driver.quit()

df = pd.DataFrame({
    "Produto": nomes,
    "Preço Normal": preco_normal,
    "Preço Cacau Lovers": preco_lovers
})

df = df[df["Produto"].str.strip() != ""]
df.to_excel("cacau_show_precos_pascoa.xlsx", index=False)
print("Planilha gerada com sucesso: cacau_show_precos_pascoa.xlsx")