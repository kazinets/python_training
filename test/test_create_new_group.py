# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_empty_group(app):

    app.open_home_page()
    # Open Group
    app.open_group_page()
    app.create_new_group(Group(name="", header="", footer=""))
    app.open_group_page()

    
def test_create_group(app):
    app.open_home_page()
    # Open Group
    app.open_group_page()
    app.create_new_group(Group(name="First Group", header="logo", footer="comment 1"))
    app.open_group_page()
