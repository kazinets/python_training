from model.group import Group
from sys import maxsize

def test_create_empty_group(app):


    app.group.open_group_page()
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max)==sorted(new_groups,key=Group.id_or_max)

def test_create_group(app):


    app.group.open_group_page()

    old_groups=app.group.get_group_list()
    group=Group(name="First Group", header="logo", footer="comment 1")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) ==sorted(new_groups, key=Group.id_or_max)


