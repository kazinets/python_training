from model.contact import Contact

def test_delete_first_contact(app):

    app.open_home_page()

    app.contact.delete_first_contact()
    #app.tap_on_home_menu_item()
    app.return_to_home()
