from model.group import Group


def test_delete_first_group(app):

    # Open Group
    app.group.open_group_page()
    if app.group.count() == 0:
       app.group.create(Group(name="First Group", header="logo", footer="comment 1"))
    app.group.delete_first_group()
    app.group.open_group_page()