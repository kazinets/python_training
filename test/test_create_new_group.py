from model.group import Group

def test_create_empty_group(app):

    # Open Group
    app.group.open_group_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.open_group_page()
    #app.session.logout()

    
def test_create_group(app):

    # Open Group
    app.group.open_group_page()
    app.group.create(Group(name="First Group", header="logo", footer="comment 1"))
    app.group.open_group_page()

