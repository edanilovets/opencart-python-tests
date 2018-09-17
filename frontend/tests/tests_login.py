from selenium.common.exceptions import NoSuchElementException
from frontend.model.customer import Customer
import pytest


test_data_login_negative = [
    Customer("", "", "", "", ""),
    Customer("John", "Travolta", "john0.mail@gmail.com", "123456789", "111111")
]


test_data_login_positive = [
    Customer("John", "Travolta", "john.mail@gmail.com", "123456789", "111111")
]


@pytest.mark.parametrize("customer", test_data_login_positive, ids=[repr(x) for x in test_data_login_positive])
def test_login_existing_customer(customer, app, db):
    customers = db.get_customers_list()
    if customer not in customers or len(customers) == 0:
        app.create_customer(customer)
        app.logout()

    app.login(customer)
    assert app.is_customer_logged_in(customer)
    app.logout()


@pytest.mark.parametrize("customer", test_data_login_negative, ids=[repr(x) for x in test_data_login_negative])
def test_login_not_existing_customer(customer, app):
    app.login(customer)
    assert not app.is_customer_logged_in(customer)
    assert app.is_login_warning_message_showed()


def test_logout_if_not_logged_in(app):
    with pytest.raises(NoSuchElementException):
        app.logout()


def test_login_number_of_login_attempts(app):
    pass

