from model.contact import Contact
def test_mod_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.mod_first_contact(Contact("masha", "masha", "masha", "masha",
                                          "1111","111","123","12","456","678","1","","","","",""))
    app.session.logout()