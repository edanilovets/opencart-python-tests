from frontend.model.customer import Customer
import pytest
import string
import random


def random_password(max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation
    # symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for _ in range(max_len)])


# test data for subscribe: Yes or No
data_subscribe = [
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", "111111")
]

# test data for password from 4 to 20 character
data_password = [
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", "{}".format(random_password(i)))
    for i in range(4, 21)
]

# test data for password negative
data_password_negative = [
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", "{}".format(random_password(i)))
    for i in range(3)
]

# test data for empty combinations
data_empty_first_name = [
    Customer("", "", "", "", ""),
    Customer("", "", "", "", "111111"),
    Customer("", "", "", "+380989990066", ""),
    Customer("", "", "", "+380989990066", "111111"),
    Customer("", "", "john.email@gmail.com", "", ""),
    Customer("", "", "john.email@gmail.com", "", "111111"),
    Customer("", "", "john.email@gmail.com", "+380989990066", ""),
    Customer("", "", "john.email@gmail.com", "+380989990066", "111111"),
    Customer("", "Travolta", "", "", ""),
    Customer("", "Travolta", "", "", "111111"),
    Customer("", "Travolta", "", "+380989990066", ""),
    Customer("", "Travolta", "", "+380989990066", "111111"),
    Customer("", "Travolta", "john.email@gmail.com", "", ""),
    Customer("", "Travolta", "john.email@gmail.com", "+380989990066", ""),
    Customer("", "Travolta", "john.email@gmail.com", "+380989990066", "111111")
]


data_empty_combinations = [
    Customer("", "", "", "", ""),
    Customer("", "", "", "", "111111"),
    Customer("", "", "", "+380989990066", ""),
    Customer("", "", "", "+380989990066", "111111"),
    Customer("", "", "john.email@gmail.com", "", ""),
    Customer("", "", "john.email@gmail.com", "", "111111"),
    Customer("", "", "john.email@gmail.com", "+380989990066", ""),
    Customer("", "", "john.email@gmail.com", "+380989990066", "111111"),
    Customer("", "Travolta", "", "", ""),
    Customer("", "Travolta", "", "", "111111"),
    Customer("", "Travolta", "", "+380989990066", ""),
    Customer("", "Travolta", "", "+380989990066", "111111"),
    Customer("", "Travolta", "john.email@gmail.com", "", ""),
    Customer("", "Travolta", "john.email@gmail.com", "+380989990066", ""),
    Customer("", "Travolta", "john.email@gmail.com", "+380989990066", "111111"),
    Customer("John", "", "", "", ""),
    Customer("John", "", "", "", "111111"),
    Customer("John", "", "", "+380989990066", ""),
    Customer("John", "", "", "+380989990066", "111111"),
    Customer("John", "Travolta", "", "", ""),
    Customer("John", "Travolta", "", "", "111111"),
    Customer("John", "Travolta", "", "john.email@gmail.com", ""),
    Customer("John", "Travolta", "", "john.email@gmail.com", "111111"),
    Customer("John", "Travolta", "john.email@gmail.com", "", ""),
    Customer("John", "Travolta", "john.email@gmail.com", "", "111111"),
    Customer("John", "Travolta", "john.email@gmail.com", "+380989990066", ""),
]


@pytest.mark.parametrize("subscribe", [True, False], ids=["Subscribe=Yes", "Subscribe=No"])
@pytest.mark.parametrize("new_customer", data_subscribe, ids=[repr(x) for x in data_subscribe])
def test_create_customer_subscribe_positive(app, db, new_customer, subscribe):
    app.create_customer(new_customer, subscribe)
    customers = db.get_customers_list()
    assert new_customer in customers

    # post-condition: delete created customer from db
    db.delete_customer_by_name_and_lastname(new_customer)


@pytest.mark.parametrize("new_customer", data_password, ids=[repr(x) for x in data_password])
def test_create_customer_password_positive(app, db, new_customer):
    app.create_customer(new_customer)
    customers = db.get_customers_list()
    assert new_customer in customers

    # post-condition: delete created customer from db
    db.delete_customer_by_name_and_lastname(new_customer)


@pytest.mark.parametrize("new_customer", data_empty_first_name, ids=[repr(x) for x in data_empty_first_name])
def test_create_customer_empty_firstname(app, new_customer):
    app.create_customer(new_customer)
    assert app.register_page.is_first_name_warning()


# @pytest.mark.parametrize("new_customer", test_data_password_negative,
#                          ids=[repr(x) for x in test_data_password_negative])
# def test_create_customer_password_negative(app, new_customer):
#     app.create_customer(new_customer)
#     assert app.is_warning_message_showed("Password")
