# -*- coding: utf-8 -*-

from model.contact import Contact

from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):

    app.open_home_page()
    app.add_new_contact(Contact("first_name", "KazinetsLast", "Address", "Homw1", "+375295107204", "work", "email1@tut.by",
                             "email2@tut.by", "19", "December", "1985", "address2", "home2"))
    app.tap_on_home_menu_item()



