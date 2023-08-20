from model.group import Group

def test_mod_first_group(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group("one", "two", "three"))
    app.session.logout()

def test_modify_group_name(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(name="new group"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(header="new header"))
    app.session.logout()