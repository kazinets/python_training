from model.contact import Contact

def test_edit_first_contact(app):


    #edit test
    app.contact.edit_first_contact(Contact("WOOOw", "KazinetsLast222", "Address", "Homw1", "+375295107204", "work", "email1@tut.by",
                             "email2@tut.by", "19", "December", "1985", "address2", "home2WOW"))
    #app.tap_on_home_menu_item()
    app.return_to_home()
