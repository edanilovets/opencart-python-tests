from selenium.common.exceptions import NoSuchElementException
from frontend.model.customer import Customer
import pytest


@pytest.mark.functional
@pytest.mark.positive
def test_login_existing_customer(app, db):
    current_customer = Customer("John", "Travolta", "john.mail@gmail.com", "123456789", "111111")
    customers = db.get_customers_list()
    if current_customer not in customers or len(customers) == 0:
        app.create_customer(current_customer)
        app.logout()

    app.login(current_customer)
    assert app.is_customer_logged_in(current_customer)
    app.logout()


@pytest.mark.functional
@pytest.mark.negative
def test_login_not_existing_customer(app):
    current_customer = Customer("John", "Travolta", "john0.mail@gmail.com", "123456789", "111111")
    app.login(current_customer)
    assert not app.is_customer_logged_in(current_customer)


@pytest.mark.functional
@pytest.mark.negative
def test_logout_if_not_logged_in(app):
    with pytest.raises(NoSuchElementException):
        app.logout()
