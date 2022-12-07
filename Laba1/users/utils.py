
from hashlib import md5


def hashing(password, password_salt):

    salted_password = password + password_salt

    password_hash = md5(salted_password.encode("utf8")).hexdigest()

    return password_hash



