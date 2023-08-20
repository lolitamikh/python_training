from model.contact import Contact
def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.mod_first_contact(Contact("masha", "masha", "masha", "masha",
                                          "1111","111","123","12","456","678","1","","","","",""))

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.mod_first_contact(Contact(firstname="new contact"))
