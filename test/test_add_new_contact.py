# -*- coding: utf-8 -*-

from model.contact import Contact



def test_add_new_contact(app):

    app.open_home_page()
    old_contact=app.contact.get_contact_list()
    contact=Contact("first_name", "KazinetsLastYYYYY", "Address", "Homw1", "+375295107204", "work", "email1@tut.by",
                             "email2@tut.by", "19", "December", "1985", "address2", "home2")
    app.contact.add_new_contact(contact)
    app.tap_on_home_menu_item()

    new_contact=app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)

    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)




