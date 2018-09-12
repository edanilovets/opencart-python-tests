from frontend.model.customer import Customer
import pytest

test_data = [
    Customer("John10", "Dilinger", "email10@mail.com", "+380989990066", "111111"),
    Customer("John11", "Dilinger", "email11@mail.com", "+380989990055", "111111")
]


@pytest.mark.parametrize("new_customer", test_data, ids=[repr(x) for x in test_data])
def test_create_customer_subscribe_off(app, db, new_customer):
    app.create_customer(new_customer, subscribe=False)
    customers = db.get_customers_list()
    assert new_customer in customers


@pytest.mark.parametrize("new_customer", test_data, ids=[repr(x) for x in test_data])
def test_create_customer_subscribe_on(app, db, new_customer):
    app.create_customer(new_customer, subscribe=True)
    customers = db.get_customers_list()
    assert new_customer in customers
