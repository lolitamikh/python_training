from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbols = string.digits
    return "+" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@dot.com"

testdata = [
    Contact(firstname=random_string("first", 10), middlename=random_string("middle", 10), lastname=random_string("last", 10),
            nickname=random_string("nickname", 10),  title=random_string("ttt", 10),
            company=random_string("company", 10), address=random_string("addr1", 10),
            home=random_number(10), mobile=random_number(10), work=random_number(10), fax=random_number(10),
            email=random_email(10), email2=random_email(10), email3=random_email(10), homepage=random_string("www", 20),
            address2=random_string("addr2", 10), phone2=random_number(10), notes=random_string("nnn", 20))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))