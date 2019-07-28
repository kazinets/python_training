from model.contact import Contact

def test_edit_first_contact(app):

    app.open_home_page()

    # Add creation new contact because test can be failed because of empty contact list
    app.open_home_page()
    app.contact.add_new_contact(
        Contact("first_name", "KazinetsLast", "Address", "Homw1", "+375295107204", "work", "email1@tut.by",
                "email2@tut.by", "19", "December", "1985", "address2", "home2"))
    app.tap_on_home_menu_item()
    #edit test

    app.contact.edit_first_contact(Contact("first_name222", "KazinetsLast222", "Address", "Homw1", "+375295107204", "work", "email1@tut.by",
                             "email2@tut.by", "19", "December", "1985", "address2", "home2"))
    #app.tap_on_home_menu_item()
    app.return_to_home()