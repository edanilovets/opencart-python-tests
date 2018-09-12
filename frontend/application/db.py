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

    def destroy(self):
        self.connection.close()
