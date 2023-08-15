# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_new_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("petrova", "ivanova", "anna", "anya", "title", "company", "spb", "33", "8800", "500",
                            "123", "anya@mail.com", "www", "spb", "33", "blabla"))
    app.logout()


