from selenium.common.exceptions import NoSuchElementException
from frontend.model.customer import Customer
import pytest


@pytest.mark.smoke
def test_login_existing_customer(app, db):
    current_customer = Customer("John", "Travolta", "john.mail@gmail.com", "123456789", "111111")
    customers = db.get_customers_list()
    if current_customer not in customers or len(customers) == 0:
        app.create_customer(current_customer)
        app.logout()

    assert app.login(current_customer)
    app.logout()


def test_logout_if_not_logged_in(app):
    with pytest.raises(NoSuchElementException):
        app.logout()

