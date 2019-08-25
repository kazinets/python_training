from model.group import Group

def test_create_empty_group(app):


    app.group.open_group_page()
    app.group.create(Group(name="", header="", footer=""))
    app.return_to_home_page()


    
def test_create_group(app):


    app.group.open_group_page()
    app.group.create(Group(name="First Group", header="logo", footer="comment 1"))
    app.return_to_home_page()

