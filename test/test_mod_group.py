from model.group import Group

def test_mod_first_group(app):
    app.group.modify_first_group(Group("one", "two", "three"))

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="new group"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="new header"))