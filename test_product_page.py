import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest

#@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    '''Тесты для взаимодествия с зарегистрированным пользователем'''

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/en-gb/')
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email, password = str(time.time()) + "@fakemail.org", 'asdww_75899333'
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        '''Тест для добавления товара в корзину пользователем'''

        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_product_in_basket()
        page.compare_name_of_book()
        page.compare_price_of_book()

    def test_user_cant_see_success_message(self, browser):
        '''Тест: проверка, что нет сообщения об успехе
        после добавления товара в корзину пользователем'''

        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    '''Тест для добавления товара в корзину'''

    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_product_in_basket()
    page.compare_name_of_book()
    page.compare_price_of_book()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    '''Тест: Ожидаем, что есть текст о том, что корзина пуста'''

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    '''Тест: проверка перехода на страницу login со страницы product'''

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    '''Тест: проверка, что есть ссылка, которая ведет на логин'''

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail(reason="must be negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    '''Негативный Тест: проверка, что нет сообщения об успехе после добавления товара в корзину
    (упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый)'''

    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="must be negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    '''Тест: проверка, что нет сообщения об успехе после добавления товара в корзину
    (будет ждать до тех пор, пока элемент не исчезнет)'''

    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_dissapeared_success_message()


