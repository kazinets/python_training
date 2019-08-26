from model.group import Group

def test_edit_first_group(app):


    app.open_home_page()
    old_groups = app.group.get_group_list()
    app.group.open_group_page()

    if app.group.count()==0:
        app.group.create(Group(name="First"))
    app.group.edit_first_group(Group(name="New Group name", header="new logo", footer="new comment 2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)



def test_modify_group_header(app):

    app.open_home_page()
    old_groups = app.group.get_group_list()
    app.group.open_group_page()

    if app.group.count()==0:
        app.group.create(Group(name="First", header="First"))
    app.group.edit_first_group(Group(header="HEADER!!!"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

