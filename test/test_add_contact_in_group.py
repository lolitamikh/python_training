from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture
import random


def test_add_contact_in_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group_list = orm.get_group_list()
    group = random.choice(group_list)
    contacts_list = orm.get_contacts_not_in_group(group)
    # если все контакты уже в группах
    if len(contacts_list) == 0:
        app.contact.create(Contact(firstname="test"))
        contacts_list = orm.get_contacts_not_in_group(group_list)
    contact = random.choice(contacts_list)
    app.contact.add_contact_to_group_by_id(group.id, contact.id)
    # проверка что контакт в группе
    assert contact in orm.get_contacts_in_group(group)
