from model.group import Group

def test_edit_first_group(app):


    app.open_home_page()
    # Open Group
    app.group.open_group_page()
    app.group.edit_first_group(Group(name="New Group name", header="new logo", footer="new comment 2"))
    app.group.open_group_page()


def test_modify_group_header(app):

    app.open_home_page()
    # Open Group
    app.group.open_group_page()
    app.group.edit_first_group(Group(header="HEADER!!!"))
    app.group.open_group_page()
