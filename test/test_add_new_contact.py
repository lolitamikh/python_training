# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_new_contact(app):
    app.contact.create(Contact("petrova", "ivanova", "anna", "anya", "title", "company", "spb", "33", "8800", "500",
                            "123", "anya@mail.com", "www", "spb", "33", "blabla"))


