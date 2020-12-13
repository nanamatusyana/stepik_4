from .pages.main_page import MaimPage
from .pages.login_page import LoginPage

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page= MaimPage(browser, link)
    page.open()
    page.go_to_login_page()
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MaimPage(browser, link)
    page.open()
    page.should_be_login_link()
def test_guest_can_login(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page=LoginPage(browser, link)
    page.open()
    page.should_be_login_page()





