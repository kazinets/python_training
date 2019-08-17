


def test_delete_first_group(app):
    app.session.login("admin","secret")

    #app.open_home_page()
    # Open Group
    app.group.open_group_page()
    app.group.delete_first_group()
    app.group.open_group_page()
    app.session.logout()