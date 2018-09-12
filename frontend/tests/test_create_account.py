from frontend.model.customer import Customer


def test_create_customer_subscribe_off(app, db):
    new_customer = Customer("John7", "Dilinger7", "email7@mail.com", "+380989990066", "111111")
    app.create_customer(new_customer, subscribe=False)
    customers = db.get_customers_list()
    assert new_customer in customers


def test_create_customer_subscribe_on(app, db):
    new_customer = Customer("John6", "Dilinger6", "email6@mail.com", "+380989990066", "111111")
    app.create_customer(new_customer, subscribe=True)
    customers = db.get_customers_list()
    assert new_customer in customers
