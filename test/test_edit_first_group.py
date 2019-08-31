from model.group import Group

def test_edit_first_group(app):

    app.open_home_page()
    old_groups = app.group.get_group_list()
    app.group.open_group_page()
    group = Group(name="First")
    group.id=old_groups[0].id
    if app.group.count()==0:
        app.group.create(group)

    app.group.edit_first_group(group)
    old_groups[0]=group
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





'''def test_modify_group_header(app):

    app.open_home_page()
    old_groups = app.group.get_group_list()
    app.group.open_group_page()

    if app.group.count()==0:
        app.group.create(Group(name="First", header="First"))
    app.group.edit_first_group(Group(header="HEADER!!!"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
'''
