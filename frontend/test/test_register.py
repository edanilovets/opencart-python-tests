from frontend.model.customer import Customer
from frontend.pages.home_page import Home


class TestRegister:
    def test_register(self, app, db, base_url):

        new_customer = Customer("Name", "Last Name", "test@gmail.com", "80993082980", "111111")

        home_page = Home(app.driver, base_url).open()
        home_page.topline.click_my_account()
        register_page = home_page.topline.click_register()

        # fill form on register page
        register_page.set_first_name(new_customer.firstname)
        register_page.set_last_name(new_customer.lastname)
        register_page.set_email(new_customer.email)
        register_page.set_phone(new_customer.phone)
        register_page.set_password(new_customer.password)
        register_page.set_confirm(new_customer.password)
        register_page.check_private_policy()
        success_page = register_page.click_continue()

        # get customers from db
        customers = db.get_customers_list()
        new_customer.password = None

        assert new_customer in customers
        assert success_page.congratulation_message == "Congratulations! Your new account has been successfully created!"
