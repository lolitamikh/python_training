from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def go_to_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("add")) > 0 and len(wd.find_elements_by_name("to_group")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_page_create_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        self.open_page_create_contact()
        # fill contact firm
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_home_page()

    def mod_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        # open first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.go_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.go_to_home_page()

    def count(self):
        self.go_to_home_page()
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.go_to_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            firstname = element.find_element_by_xpath(".//td[3]").text
            lastname = element.find_element_by_xpath(".//td[2]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts
