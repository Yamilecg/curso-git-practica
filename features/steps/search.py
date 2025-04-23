from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.iteso.mx")

try:
    # Espera a que el botón de búsqueda esté presente y haz clic
    search_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "search-toggle"))
    )
    search_icon.click()

    # Ahora espera a que aparezca el input de búsqueda
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "busqueda"))
    )
    search_input.send_keys("carreras\n")

except Exception as e:
    print("Error:", e)
    driver.save_screenshot("error.png")

finally:
    # Espera unos segundos para ver resultados
    WebDriverWait(driver, 10).until(
        EC.title_contains("carreras")
    )
    print("Página de resultados:", driver.title)
    driver.quit()
