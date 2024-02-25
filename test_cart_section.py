from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)


class HappyFlow(BaseCase):


    def happyflow_scenario(self):
        """happy flow scenario -
        two products added from the product pages, test the cart window from the cart icon
        delete one product, assert number of products in the cart, proceed with the checkout"""
        #adding the products to the cart
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
        self.go_back()
        self.click("(//img[@class='product-image-photo'])[4]")
        self.click("(//*[@option-id='168'])")
        self.assert_attribute("(//*[@id='option-label-size-143-item-168'])", "aria-checked", "true")
        self.click("//*[@id='option-label-color-93-item-49']")
        self.assert_attribute("(//*[@id='option-label-color-93-item-49'])", "aria-checked", "true")
        self.type("[id='qty']", '1')
        self.click("[id='product-addtocart-button']")
        self.scroll_to_top()
        # open the cart window and assert the number and the products name
        self.click("//a[contains(text(),'shopping cart')]")
        self.wait_for_element('.base', timeout=3)
        self.assert_exact_text('2', '//span[@class="counter-label"]', timeout=8)
        self.click("[class='action showcart']")
        self.assert_element_visible("[id='ui-id-1']")
        self.assert_element_visible("//div[@class='product']/a[@title='Juno Jacket']")
        self.assert_element_visible("//div[@class='product']/a[@title='Nadia Elements Shell']")
        self.assert_true(len(self.find_elements("[class='product']")) == 2)
        # delete one product from the cart, assert the number of the products
        self.click("(//div[@class='secondary']/a/span)[1]")
        self.assert_element_visible("[class='modal-popup confirm                                 _show']")
        self.assert_element_visible("[class='action-secondary action-dismiss']")
        self.assert_element_visible("[class='action-primary action-accept']")
        self.click("[class='action-primary action-accept']")
        self.wait(8)
        self.assert_true(len(self.find_elements("[class='product']")) == 1)
        # proceed with the checkout flow and assert error messages for the required fields
        self.click('(//button[@class="action primary checkout"])[2]')
        self.wait_for_element("[id='checkout']")
        self.assert_element_visible("[id='customer-email-fieldset']")
        self.assert_element_visible("[id='shipping-new-address-form']")
        self.assert_element_visible("[id='opc-shipping_method']")
        self.type("//input[@id='customer-email'][1]", "dummy2dummy.ro")
        self.click("[name='firstname']")
        self.assert_exact_text("Please enter a valid email address (Ex: johndoe@domain.com).",
                              "[id='customer-email-error']")
        self.clear("//input[@id='customer-email'][1]")
        self.click("[name='firstname']")
        self.type("[name='firstname']", "Tester")
        self.type("//input[@id='customer-email'][1]", "dummy@dummy.ro")
        # self.click("[name='lastname']")
        self.type("[name='lastname']", '!!')
        self.click("[name='street[0]']")
        self.type("[name='street[0]']", 'Test')
        self.click("[name='city']")
        self.type("[name='city']", "Ari")
        self.click('[name="region_id"]')
        self.click("//select/option[@value='4']")
        self.click("[name='postcode']")
        self.type("[name='postcode']", "9")
        self.click("[name='country_id']")
        self.assert_exact_text(
            "Provided Zip/Postal Code seems to be invalid. Example: 12345-6789; 12345. If you believe it is the right one you can ignore this notice.",
            "//div[@class='message warning']/span")
        self.clear("[name='postcode']")
        self.type("[name='postcode']", "12345-6789")
        self.type("[name='telephone']", 'abcdef')
        self.click("//button[@class='button action continue primary']")
        self.assert_exact_text("The shipping method is missing. Select the shipping method and try again.", "//div[@class='message notice']/span")
        self.click("(//input[@class='radio'])[1]")
        self.click("//button[@class='button action continue primary']")
        self.wait_for_element("[class='shipping-information']")
        self.assert_element_visible('[class="opc-block-summary"]')
        self.click('[class="action primary checkout"]')
        self.wait_for_element('[class="base"]')
        self.assert_exact_text("Thank you for your purchase!", '[class="base"]')
        self.assert_element_visible('[class="checkout-success"]')
        self.assert_element_visible('[id="registration"]')
        #assert 'no products in the cart' message when baskcket is empty
        self.click("[class='action showcart']")
        self.assert_element_visible("[id='minicart-content-wrapper']")
        self.assert_exact_text("You have no items in your shopping cart.", "//strong[@class='subtitle empty']")

