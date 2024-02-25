from bs4 import element
from selenium.webdriver import Keys
from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)


class TestSearchAction(BaseCase):

    def test_search_field(self):
        """scenario to test search results with dummy value and with valid product,
        assert the visibility of the following elements: ratings, reviews, add a review, price, stock and SKU code element
        error message validation for product quantity not available"""
        self.maximize_window()
        self.open("https://magento.softwaretestingboard.com")
        self.click("[id='search']")
        self.type("[id='search']", 'xyz')
        self.click("[class='action search']")
        self.wait_for_element("h1")
        self.assert_exact_text("Your search returned no results. ", "(//div[@class='message notice'])/div")
        self.clear("[id='search']")
        self.type("[id='search']","Push It Messenger Bag")
        self.click("[class='action search']")
        self.assert_element_visible("//a[contains(text(),'Push It Messenger Bag')]")
        self.click("(//img[@class='product-image-photo'])[1]")
        self.assert_element_visible("[class='rating-result']")
        self.assert_element_visible("[class='action view']")
        self.assert_element_visible("[class='action add']")
        self.assert_element_visible("(//span[@class='price'])[1]")
        self.assert_element_visible("//div[@class='stock available']")
        self.assert_element_visible("//div[@class='product attribute sku']")
        self.assert_element_visible("//div[@class='product data items']")
        self.click("[id='product-addtocart-button']")
        self.wait_for_element("//div[@data-ui-id='message-error']/div")
        self.assert_exact_text("The requested qty is not available","//div[@data-ui-id='message-error']/div", timeout=6)