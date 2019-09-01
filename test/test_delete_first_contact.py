from model.contact import Contact

def test_delete_first_contact(app):

    app.open_home_page()
    if app.contact.count()==0:
        app.contact.add_new_contact(Contact("first_name", "KazinetsLastYYYYY", "Address", "Homw1", "+375295107204", "work", "email1@tut.by",
                             "email2@tut.by", "19", "December", "1985", "address2", "home2"))
    app.open_home_page()
    old_contact=app.contact.get_contact_list()
    app.contact.delete_first_contact()
    app.tap_on_home_menu_item()
    app.open_home_page()
    new_contact = app.contact.get_contact_list()
#    assert len(old_contact) - 1 == len(new_contact)
    #old_contact[0:1] = []
    assert old_contact == new_contact
