from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage:
    SHIPPING_FEE_BLOCKS = (
        By.CSS_SELECTOR,
        "div.delivery-option-item__shipping-fee"
    )

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait   = WebDriverWait(driver, timeout)

    def has_free_shipping(self) -> bool:
        try:
            fees = self.wait.until(EC.presence_of_all_elements_located(self.SHIPPING_FEE_BLOCKS))
            for fee in fees:
                if "free" in fee.text.strip().lower():
                    return True
            return False
        except TimeoutException:
            return False
