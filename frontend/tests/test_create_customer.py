from frontend.model.customer import Customer
import pytest
import string
import random


def random_password(max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation
    # symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for _ in range(max_len)])


test_data_sample = [
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", "111111")
]

# test data for password from 0 to 20 character
test_data_password = [
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", "{}".format(random_password(i)))
    for i in range(21)
]


@pytest.mark.parametrize("new_customer", test_data_sample, ids=[repr(x) for x in test_data_sample])
@pytest.mark.parametrize("subscribe", [True, False], ids=["Subscribe=Yes", "Subscribe=No"])
def test_create_customer_subscribe(app, db, new_customer, subscribe):
    app.create_customer(new_customer, subscribe)
    customers = db.get_customers_list()
    assert new_customer in customers

    # post-condition: delete created customer from db
    db.delete_customer_by_name_and_lastname(new_customer)


@pytest.mark.parametrize("new_customer", test_data_password, ids=[repr(x) for x in test_data_password])
def test_create_customer_password(app, db, new_customer):
    app.create_customer(new_customer)
    customers = db.get_customers_list()
    assert new_customer in customers

    # post-condition: delete created customer from db
    db.delete_customer_by_name_and_lastname(new_customer)



