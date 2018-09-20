from frontend.model.customer import Customer
import pytest

# existing customer
test_data_edit = [
    Customer("John", "Travolta", "john.mail@gmail.com", "123456789", "111111")
]


@pytest.mark.parametrize("customer", test_data_edit, ids=[repr(x) for x in test_data_edit])
def test_edit_account_firstname(app, db, customer):
    new_customer = Customer("Ne777_John", "Travolta", "john.mail@gmail.com", "123456789", "111111")
    app.login(customer)
    app.edit_customer_firstname(new_customer)

    customers = db.get_customers_list()
    match = None
    for x in customers:
        if x.firstname == new_customer.firstname and x.email == new_customer.email:
            match = x
    assert match is not None
