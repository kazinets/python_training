# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group

import unittest

class TestCreateNewGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_create_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        # Open Group
        self.open_group_page(wd)
        self.create_new_group(wd, Group(name="", header="", footer=""))
        self.open_group_page(wd)

    
    def test_create_group(self):
        wd = self.wd
        self.open_home_page(wd)
        # Open Group
        self.open_group_page(wd)
        self.create_new_group(wd, Group(name="First Group", header="logo", footer="comment 1"))
        self.open_group_page(wd)

    def create_new_group(self, wd, group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # click on Submit button
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbookv4/index.php")

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
