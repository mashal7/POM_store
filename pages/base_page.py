import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK)
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        assert self.is_element_present(BasePageLocators.BASKET_LINK)
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    # проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    # проверяет, исчез ли элемент с указанным локатором за заданное время.
    # Если элемент исчез, метод возвращает True. Если нет — возвращает False.
    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(*locator))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"

    # для сравнения текста двух локаторов
    def compare_text(self, locator1, locator2):
        text1 = self.browser.find_element(*locator1).text
        text2 = self.browser.find_element(*locator2).text
        return True if text1 == text2 else False



    def solve_quiz_and_get_code(self):
        '''Для решения уравнения и отправки кода в alert'''

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")