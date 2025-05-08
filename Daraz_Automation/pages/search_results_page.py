import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    MIN_PRICE_INPUT  = (By.CSS_SELECTOR, 'input[placeholder="Min"]')
    MAX_PRICE_INPUT  = (By.CSS_SELECTOR, 'input[placeholder="Max"]')
    FIRST_PRODUCT    = (By.XPATH, "(//a[contains(@href,'/products/')])[1]")
    RESULTS_HEADER   = (By.XPATH, "//*[contains(text(),'items found')]")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait   = WebDriverWait(driver, timeout)

    def filter_by_price(self, min_price: int, max_price: int):
        mi = self.wait.until(EC.presence_of_element_located(self.MIN_PRICE_INPUT))
        ma = self.wait.until(EC.presence_of_element_located(self.MAX_PRICE_INPUT))
        mi.clear(); mi.send_keys(str(min_price))
        ma.clear(); ma.send_keys(str(max_price))
        # click the “Go” button right after the Max input
        go = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            '//input[@placeholder="Max"]/following-sibling::button'
        )))
        go.click()
        # wait for results to reload
        self.wait.until(EC.presence_of_element_located(self.FIRST_PRODUCT))

    def get_results_count(self) -> int:
        header = self.wait.until(EC.visibility_of_element_located(self.RESULTS_HEADER))
        text   = header.text  # e.g. "21091 items found for “electronics”"
        m = re.search(r'([\d,]+)\s+items found', text)
        return int(m.group(1).replace(',', '')) if m else 0

    def click_first_product(self):
        link = self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT))
        link.click()
        # wait until we’re on a /products/ URL
        self.wait.until(lambda d: "/products/" in d.current_url)
