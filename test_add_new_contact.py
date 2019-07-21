# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from contact import Contact
import unittest

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.add_new_contact(wd, Contact("first_name", "KazinetsLast", "Address", "Homw1", "+375295107204", "work", "email1",
                             "sdfsd", "email2@tut.by", "19", "December", "1985", "address2", "home2"))
        self.tap_on_home_menu_item(wd)

    def add_new_contact(self, wd, contact):
        self.tap_on_menu_AddNew_item(wd)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address_1)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_1)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Edit / add address book entry'])[1]/following::form[1]").click()
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[20]").click()
        wd.find_element_by_name(contact.bmonth).click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[45]").click()
        wd.find_element_by_name(contact.byear).click()
        wd.find_element_by_name(contact.byear).clear()
        wd.find_element_by_name(contact.byear).send_keys(contact.byear)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Group:'])[1]/following::option[1]").click()
        wd.find_element_by_name(contact.address2).click()
        wd.find_element_by_name(contact.address2).clear()
        wd.find_element_by_name(contact.address2).send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home_2)
        wd.find_element_by_name("submit").click()

    def tap_on_menu_AddNew_item(self, wd):
        wd.find_element_by_link_text("add new").click()

    def tap_on_home_menu_item(self, wd):
        wd.find_element_by_link_text("home").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbookv4/index.php")
        self.tap_on_home_menu_item(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
