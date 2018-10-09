from frontend.pages.home_page import Home
import pytest
from frontend.data.register_test_data import valid_customer
from frontend.data.register_test_data import empty_first_name_customer
from frontend.data.register_test_data import data_password_negative
from frontend.data.register_test_data import data_password


class TestRegister:

    @pytest.mark.parametrize("subscribe", [True, False], ids=["Subscribe=Yes", "Subscribe=No"])
    @pytest.mark.parametrize("new_customer", valid_customer, ids=[repr(x) for x in valid_customer])
    def test_register(self, app, db, base_url, new_customer, subscribe):
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

        if subscribe:
            register_page.set_subscribe_yes()

        register_page.check_private_policy()
        success_page = register_page.click_continue()

        # get customers from db
        customers = db.get_customers_list()

        assert new_customer in customers
        assert success_page.congratulation_message == "Congratulations! Your new account has been successfully created!"

        # post-condition: delete customer from db
        db.delete_customer_by_name_and_lastname(new_customer)

    @pytest.mark.parametrize("new_customer", valid_customer, ids=[repr(x) for x in valid_customer])
    def test_register_without_private_policy_checked(self, new_customer, app, base_url):
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
        register_page.click_continue(leave_page=False)

        assert register_page.alert_danger_message == "Warning: You must agree to the Privacy Policy!"

    @pytest.mark.parametrize("new_customer", empty_first_name_customer, ids=[repr(x) for x in empty_first_name_customer])
    def test_register_with_empty_first_name(self, new_customer, app, base_url):
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
        register_page.click_continue(leave_page=False)

        assert register_page.is_first_name_text_danger_present()

    # todo: complete test below
    @pytest.mark.parametrize("new_customer", data_password, ids=[repr(x) for x in data_password])
    def test_register_with_different_password_length(self, new_customer, app, base_url):
        pass

    @pytest.mark.parametrize("new_customer", data_password_negative, ids=[repr(x) for x in data_password_negative])
    def test_register_with_short_password(self, new_customer, app, base_url):
        pass
