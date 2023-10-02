from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture
import random


def test_delete_contact_from_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group_list = orm.get_group_list()
    group = random.choice(group_list)
    contact_list = orm.get_contacts_not_in_group(group)
    if len(orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(contact_list)
        app.contact.add_contact_to_group_by_id(group.id, contact.id)
    contact_del = random.choice(orm.get_contacts_in_group(group))
    app.contact.delete_contact_from_group(group.id, contact_del.id)
    assert contact_del not in orm.get_contacts_in_group(group)
