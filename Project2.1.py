import re

email_condition = "^[a-z]+[\._]?[a-z0-9]+[@][a-z0-9]+[.][a-z]{2,}$"
user_email = input('Enter your email:')

try:
    if re.fullmatch(email_condition, user_email):
        print("Valid Email")
    else:
        print("Invalid Email")
except re.error as e:
    print(f"Error in regular expression: {e}")