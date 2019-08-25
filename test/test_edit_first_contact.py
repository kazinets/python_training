from model.contact import Contact

def test_edit_first_contact(app):


    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.add_new_contact(
            Contact("first_name", "KazinetsLastYYYYY", "Address", "Homw1", "+375295107204", "work", "email1@tut.by",
                    "email2@tut.by", "19", "December", "1985", "address2", "home2"))
    app.open_home_page()
    app.contact.edit_first_contact(Contact("WOOOw", "KazinetsLast222", "Address", "Homw1", "+375295107204", "work", "email1@tut.by",
                             "email2@tut.by", "19", "December", "1985", "address2", "home2WOW"))

    app.return_to_home()
