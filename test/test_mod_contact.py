import random

from model.contact import Contact
from random import randrange

def test_mod_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    # index = randrange(len(old_contacts))
    contact.firstname = Contact(firstname="masha").firstname
    contact.middlename = Contact(middlename="masha").middlename
    contact.lastname = Contact(lastname="masha").lastname
    app.contact.mod_contact_by_id(contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_firstname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.mod_first_contact(Contact(firstname="new contact"))
