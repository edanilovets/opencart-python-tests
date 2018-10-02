from frontend.model.customer import Customer

valid_customer = [
    Customer("Name", "Last Name", "test@gmail.com", "80993082980", "111111")
]

empty_first_name_customer = [
    Customer("", "", "", "", ""),
    Customer("", "", "", "", "111111"),
    Customer("", "", "", "+380989990066", ""),
    Customer("", "", "", "+380989990066", "111111"),
    Customer("", "", "john.email@gmail.com", "", ""),
    Customer("", "", "john.email@gmail.com", "", "111111"),
    Customer("", "", "john.email@gmail.com", "+380989990066", ""),
    Customer("", "", "john.email@gmail.com", "+380989990066", "111111"),
    Customer("", "Travolta", "", "", ""),
    Customer("", "Travolta", "", "", "111111"),
    Customer("", "Travolta", "", "+380989990066", ""),
    Customer("", "Travolta", "", "+380989990066", "111111"),
    Customer("", "Travolta", "john.email@gmail.com", "", ""),
    Customer("", "Travolta", "john.email@gmail.com", "+380989990066", ""),
    Customer("", "Travolta", "john.email@gmail.com", "+380989990066", "111111")
]

# todo: create test data
empty_last_name_customer = []
empty_email_customer = []
empty_phone_customer = []
empty_password_customer = []
empty_confirm_customer = []
