from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)

class AddingProductsToCart(BaseCase):
    def test_adding_products_to_cart(self):
        """happy flow scenario -
        one product added from the product page and the second one added from the products overview page
        assertion that the cart
        icon number is reflecting the expected product number after each addition"""
        self.maximize_window()
        self.open("https://magento.softwaretestingboard.com")
        self.hover("//*[contains(text(),'Women')]")
        self.wait_for_element("//*[@id='ui-id-9']")
        self.hover("//*[@id='ui-id-9']")
        self.click("//*[@id='ui-id-11']")
        self.assert_exact_text("Jackets", "span.base")
        self.click("//a[contains(text(),'Juno Jacket')]")
        self.assert_element_visible('span.base')
        self.click("(//*[@option-id='168'])")
        self.assert_attribute("(//*[@id='option-label-size-143-item-168'])", "aria-checked", "true")
        self.click("//*[@id='option-label-color-93-item-50']")
        self.assert_attribute("(//*[@id='option-label-color-93-item-50'])", "aria-checked", "true")
        self.type("[id='qty']", '1')
        self.click("[id='product-addtocart-button']")
        self.scroll_to_top()
        self.assert_element_visible("[class='page messages']")
        self.assert_exact_text('1', '//span[@class="counter-label"]', timeout=6)
        self.click("(//*[@class='level-top ui-corner-all'])[1]")
        self.assert_exact_text('What\'s New', '.base')
        self.click("(//a[contains(text(),'Pants')])[2]")
        self.wait_for_element("//a[contains(text(),'Thorpe Track Pant ')]", timeout=4)
        self.hover_on_element("//a[contains(text(),'Thorpe Track Pant ')]")
        self.click("(//div[@id='option-label-size-143-item-177'])[6]")
        self.click("(//div[@id='option-label-color-93-item-57'])[1]")
        self.click("(//button[@class='action tocart primary'])[6]")
        self.assert_element_visible("(//*[@class='messages'])[1]")
        self.click("//a[contains(text(),'shopping cart')]")
        self.wait_for_element('.base', timeout=3)
        self.assert_exact_text('2', '//span[@class="counter-label"]', timeout=6)
        self.click("[class='action showcart']")
        self.assert_element_visible("[id='ui-id-1']")
        self.assert_element_visible("//div[@class='product']/a[@title='Thorpe Track Pant']", timeout=5)
        self.assert_element_visible("//div[@class='product']/a[@title='Juno Jacket']")
        self.assert_true(len(self.find_elements("[class='product']")) == 2)
        