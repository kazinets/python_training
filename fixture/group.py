
class GroupHelper:
    def __init__(self,app):
        self.app=app

    def create(self, group):
            wd = self.app.wd
            wd.find_element_by_name("new").click()
            self.fill_group_form(group)

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
            self.fill_group_form(group)

            # click on Update button
            wd.find_element_by_name("update").click()

    def fill_group_form(self, group):
        wd=self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)






