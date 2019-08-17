
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.session import SessionHelper



class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session=SessionHelper(self)
        self.group=GroupHelper(self)
        self.contact=ContactHelper(self)


    def tap_on_home_menu_item(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbookv4/index.php")
        #self.tap_on_home_menu_item()

    def return_to_home_page(self):
        wd=self.wd
        wd.find_element_by_link_text("group page").click()

    def return_to_home(self):
        wd=self.wd
        wd.find_element_by_link_text("home page").click()


    def destroy(self):
        self.wd.quit()