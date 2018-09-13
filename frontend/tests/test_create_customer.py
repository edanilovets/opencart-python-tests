from frontend.model.customer import Customer
import pytest
import string
import random


def random_password(max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation
    # symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for _ in range(max_len)])


# test data for subscribe: Yes or No
test_data_subscribe = [
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", "111111")
]

# test data for password from 4 to 20 character
test_data_password = [
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", "{}".format(random_password(i)))
    for i in range(4, 21)
]

# test data for password negative
test_data_password_negative = [
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", "{}".format(random_password(i)))
    for i in range(3)
]


@pytest.mark.parametrize("subscribe", [True, False], ids=["Subscribe=Yes", "Subscribe=No"])
@pytest.mark.parametrize("new_customer", test_data_subscribe, ids=[repr(x) for x in test_data_subscribe])
def test_create_customer_subscribe_positive(app, db, new_customer, subscribe):
    app.create_customer(new_customer, subscribe)
    customers = db.get_customers_list()
    assert new_customer in customers

    # post-condition: delete created customer from db
    db.delete_customer_by_name_and_lastname(new_customer)


@pytest.mark.parametrize("new_customer", test_data_password, ids=[repr(x) for x in test_data_password])
def test_create_customer_password_positive(app, db, new_customer):
    app.create_customer(new_customer)
    customers = db.get_customers_list()
    assert new_customer in customers

    # post-condition: delete created customer from db
    db.delete_customer_by_name_and_lastname(new_customer)


@pytest.mark.parametrize("new_customer", test_data_password_negative, ids=[repr(x) for x in test_data_password_negative])
def test_create_customer_password_negative(app, new_customer):
    app.create_customer(new_customer)
    assert app.is_warning_message_showed("Password")


def test_create_customer_personal_info_empty(app):
    app.create_customer(Customer("", "", "", "", ""))
    assert app.is_warning_message_showed("First Name")
    assert app.is_warning_message_showed("Last Name")
    assert app.is_warning_message_showed("E-mail")
    assert app.is_warning_message_showed("Telephone")
