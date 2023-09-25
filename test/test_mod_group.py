from model.group import Group
import random

def test_mod_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
#    index = randrange(len(old_groups))
    group.name = Group(name="one").name
    group.header = Group(header="two").header
    group.footer = Group(footer="tree").footer
#    group.id = old_groups[index].id
    app.group.modify_group_by_id(group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
#    old_groups[group.id] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="new group"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

# def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="new header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)