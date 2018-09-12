import mysql.connector
from frontend.model.customer import Customer


class Db:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def get_customers_list(self):
        customer_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT firstname, lastname, email, telephone FROM oc_customer")
            for row in cursor:
                (firstname, lastname, email, telephone) = row
                customer_list.append(Customer(firstname=firstname, lastname=lastname, email=email, phone=telephone))
        finally:
            cursor.close()
        return customer_list

    def delete_customer_by_name_and_lastname(self, customer):
        cursor = self.connection.cursor()
        try:
            query = "DELETE FROM oc_customer WHERE firstname = '{}' AND lastname = '{}'".format(customer.firstname,
                                                                                                customer.lastname)
            cursor.execute("set autocommit = 1")
            cursor.execute(query)
            print("{} was deleted from db.".format(customer.__repr__()))
        finally:
            cursor.close()

    def destroy(self):
        self.connection.close()
