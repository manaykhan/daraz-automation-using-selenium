import pytest
from pages.home_page           import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page        import ProductPage

@pytest.mark.usefixtures("driver")
class TestDaraz:

    def test_results_count_after_filter(self, driver):
        home    = HomePage(driver)
        home.load()
        home.search_for_item("electronics")

        results = SearchResultsPage(driver)
        results.filter_by_price(500, 5000)

        count = results.get_results_count()
        assert count > 0, f"Expected >0 products after filtering, but got {count}"

    def test_free_shipping_on_first_product(self, driver):
        home    = HomePage(driver)
        home.load()
        home.search_for_item("electronics")

        results = SearchResultsPage(driver)
        results.filter_by_price(500, 5000)
        results.click_first_product()

        product = ProductPage(driver)
        assert product.has_free_shipping(), "Free shipping/delivery was NOT found on the product page"
