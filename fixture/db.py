import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, address, home, mobile, "
                           "work, fax, email, email2, email3,"
                           "phone2, notes from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, address, home, mobile, work, fax, email, email2, email3, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                                    company=company, address=address, home=home, mobile=mobile, work=work, fax=fax,  email=email,
                                    email2=email2, email3=email3, phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()