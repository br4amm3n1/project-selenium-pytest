from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
from pages.locators import ProductPageLocators


@pytest.mark.skip
@pytest.mark.parametrize(
    "link_tail",
    [
        "?promo=offer0",
        "?promo=offer1",
        "?promo=offer2",
        "?promo=offer3",
        "?promo=offer4",
        "?promo=offer5",
        "?promo=offer6",
        pytest.param("?promo=offer7", marks=pytest.mark.xfail),
        "?promo=offer8",
        "?promo=offer9"
    ]
)
def test_guest_can_add_product_to_basket(browser, link_tail):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + link_tail
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_title_added_equals_title_in_message()
    page.should_be_price_added_equals_price_in_message()


@pytest.mark.skip # xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_in_basket()

    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is available."


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "All right! Success message isn't available."


@pytest.mark.skip # xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_in_basket()

    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Message success isn't disappeared."


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, url=browser.current_url)

    assert basket_page.is_basket_empty() and basket_page.basket_has_no_products(), "Basket isn't empty"
