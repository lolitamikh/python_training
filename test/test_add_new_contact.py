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
    app.session.login("admin", "secret")
    app.contact.create(Contact("petrova", "ivanova", "anna", "anya", "title", "company", "spb", "33", "8800", "500",
                            "123", "anya@mail.com", "www", "spb", "33", "blabla"))
    app.session.logout()


