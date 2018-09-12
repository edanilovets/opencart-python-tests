class Customer:
    def __init__(self, firstname=None, lastname=None, email=None, phone=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return "Customer({}, {}, {}, {}, {})".format(self.firstname, self.lastname, self.email, self.phone,
                                                     self.password)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and self.email == other.email and \
               self.phone == other.phone
