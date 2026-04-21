from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def obtener_precio_pccomponentes(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        time.sleep(5)

        elemento_precio = driver.find_element(By.CLASS_NAME, "p-price")
        texto_precio = elemento_precio.text  # Ejemplo: "1.249€"
        # Limpieza de datos
        precio_limpio = texto_precio.replace('€', '').replace(
            '.', '').replace(',', '.').strip()
        return float(precio_limpio)
    except Exception as e:
        print(f"Error al extraer: {e}")
    finally:
        driver.quit()


url_producto = "https://www.pccomponentes.com/pccom-imperial-by-b0rjacs-amd-ryzen-7-7800x3d-32gb-2tb-ssd-rtx-5070-windows-11-home?s_kwcid=AL!14405!3!!!!x!!&gad_source=1&gad_campaignid=21322380416&gclid=CjwKCAjwwJzPBhBREiwAJfHRnRlO7OK-NSv0QSFIM_m4YceZSEkko6DhAIQxvcuN_NaK2irGledHchoC0E8QAvD_BwE"
print(f"El precio actual es: {obtener_precio_pccomponentes(url_producto)}")
