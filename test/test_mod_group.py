from model.group import Group

def test_mod_first_group(app):
    app.session.login("admin", "secret")
    app.group.mod_first_group(Group("one","two","three"))
    app.session.logout()