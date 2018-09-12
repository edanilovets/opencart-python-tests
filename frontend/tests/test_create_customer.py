from frontend.model.customer import Customer
import pytest

test_data = [
    Customer("John10", "Dilinger", "email10@mail.com", "+380989990066", "111111"),
    Customer("John11", "Dilinger", "email11@mail.com", "+380989990055", "111111"),
    Customer("John12", "Dilinger", "email12@mail.com", "+380989990055", "111111"),
    Customer("John13", "Dilinger", "email13@mail.com", "+380989990055", "111111")
]


@pytest.mark.parametrize("new_customer", test_data, ids=[repr(x) for x in test_data])
def test_create_customer_subscribe_off(app, db, new_customer):
    app.create_customer(new_customer, subscribe=False)
    customers = db.get_customers_list()
    assert new_customer in customers

    # post-condition: delete created customer from db
    db.delete_customer_by_name_and_lastname(new_customer)


@pytest.mark.parametrize("new_customer", test_data, ids=[repr(x) for x in test_data])
def test_create_customer_subscribe_on(app, db, new_customer):
    app.create_customer(new_customer, subscribe=True)
    customers = db.get_customers_list()
    assert new_customer in customers

    # post-condition: delete created customer from db
    db.delete_customer_by_name_and_lastname(new_customer)
