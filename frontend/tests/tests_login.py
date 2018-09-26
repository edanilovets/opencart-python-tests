from selenium.common.exceptions import NoSuchElementException
from frontend.model.customer import Customer
import pytest


data_login_positive = [
    Customer("Eugene", "Danilovets", "evgeniy.danilovets@gmail.com", "+380970359901", "111111")
]


@pytest.mark.parametrize("customer", data_login_positive, ids=[repr(x) for x in data_login_positive])
def test_login_existing_customer(customer, app, db):
    customers = db.get_customers_list()
    if customer not in customers or len(customers) == 0:
        app.create_customer(customer)
        app.logout()

    app.login(customer)
    assert app.is_customer_logged_in(customer)
    app.logout()
    # app.save_screen_shot()


def test_logout_if_not_logged_in(app):
    with pytest.raises(NoSuchElementException):
        app.logout()


def test_login_number_of_login_attempts():
    pass


def test_login_non_existing_customer():
    pass
