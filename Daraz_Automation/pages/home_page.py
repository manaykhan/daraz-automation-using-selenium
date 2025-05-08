from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL        = "https://www.daraz.pk/"
    SEARCH_BOX = (By.ID, "q")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait   = WebDriverWait(driver, timeout)

    def load(self):
        self.driver.get(self.URL)

    def search_for_item(self, term: str):
        box = self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        box.clear()
        box.send_keys(term)
        box.submit()
