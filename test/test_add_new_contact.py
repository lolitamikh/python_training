# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("petrova", "ivanova", "anna", "anya", "title", "company", "spb", "33", "8800", "500",
                            "123", "anya@mail.com", "www", "spb", "33", "blabla")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



