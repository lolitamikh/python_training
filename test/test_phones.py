import re
from fixture.contact import Contact
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_all_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contact_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_db) == len(contact_from_ui)
    for x in range(len(contact_from_ui)):
        assert contact_from_ui[x].firstname == contact_from_db[x].firstname
        assert contact_from_ui[x].lastname == contact_from_db[x].lastname
        assert contact_from_ui[x].address == contact_from_db[x].address
        assert contact_from_ui[x].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[x])
        assert contact_from_ui[x].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[x])

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))