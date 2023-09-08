from model.group import Group
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Group("name1", "header1", "footer1"),
    Group("name2", "header2", "footer2")
]
