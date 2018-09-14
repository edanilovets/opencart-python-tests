from frontend.model.customer import Customer


def test_login_existing_customer(app, db):
    current_customer = Customer("John", "Travolta", "john.mail@gmail.com", "123456789", "111111")
    customers = db.get_customers_list()
    if current_customer not in customers or len(customers) == 0:
        app.create_customer(current_customer)
        app.logout()

    assert app.login(current_customer)
    app.logout()

