import pytest
from Pages.basket_page import BasketPage
from Pages.main_page import MainPage
from Pages.login_page import LoginPage

"""Checking Login page"""

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page_on_main_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link_on_main_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()


# """Checking empty basket"""

# Pass - The product shouldn't be


def test_guest_cant_see_product_in_basket_opened_from_main_page_when_product_is_not_added(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_basket_button()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()

# Fail - The product shouldn't be


@pytest.mark.xfail(reason="The product should not be in the basket when a product isn't added")
def test_guest_can_see_product_in_basket_opened_from_main_page_when_product_is_not_added(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_basket_button()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_product_in_basket()

# Pass - The empty message should be


def test_guest_can_see_empty_message_in_basket_opened_from_main_page_when_product_is_not_added(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_basket_button()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_basket_is_empty()


# # Fail - The empty message should be

@pytest.mark.xfail(reason="The empty message should be in the basket when a product isn't added")
def test_guest_cant_see_empty_message_in_basket_opened_from_main_page_when_product_is_not_added(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_basket_button()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_message_basket_is_empty()
