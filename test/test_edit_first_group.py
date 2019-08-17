from model.group import Group

def test_edit_first_group(app):

    #Add creation new group because of empty group list
    #app.open_home_page()
    app.session.login("admin", "secret")
    # Open Group
    app.group.open_group_page()
    app.group.create(Group(name="First Group", header="logo", footer="comment 1"))
    app.group.open_group_page()

    #edit group

    app.open_home_page()
    # Open Group
    app.group.open_group_page()
    app.group.edit_first_group(Group(name="New Group name", header="new logo", footer="new comment 2"))
    app.group.open_group_page()
    app.session.logout()