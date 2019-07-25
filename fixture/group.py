
class GroupHelper:
    def __init__(self,app):
        self.app=app

    def create(self, group):
            wd = self.app.wd
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

    def open_group_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        # delete first group
        wd.find_element_by_name("delete").click()

    def edit_first_group(self,group):
            wd = self.app.wd
            self.open_group_page()
            # select first group
            wd.find_element_by_name("selected[]").click()
            # delete first group
            wd.find_element_by_name("edit").click()
            #enter new value
            wd.find_element_by_name("group_name").send_keys(group.name)
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
            # click on Update button
            wd.find_element_by_name("update").click()







