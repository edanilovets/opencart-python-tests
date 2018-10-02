from frontend.pages.home_page import Home
import pytest
from frontend.data.register_test_data import valid_customer


class TestRegister:

    @pytest.mark.parametrize("new_customer", valid_customer, ids=[repr(x) for x in valid_customer])
    def test_register(self, new_customer, app, db, base_url):
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

    def test_register_without_private_policy_checked(self):
        pass

    def test_register_with_empty_first_name(self):
        pass
