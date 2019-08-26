from model.group import Group

def test_create_empty_group(app):


    app.group.open_group_page()
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


    
def test_create_group(app):


    app.group.open_group_page()

    old_groups=app.group.get_group_list()

    app.group.create(Group(name="First Group", header="logo", footer="comment 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    #app.return_to_home_page()

