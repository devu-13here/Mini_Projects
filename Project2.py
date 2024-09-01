email=input(" Enter your Email: ") #g@g.in

def validate_email(email):
    # 1. The email should have a minimum of 6 characters.
    if len(email) < 6:
        print("Email should have a minimum of 6 characters.")
        return
    
    # 2. Email should not start from a number or '@' symbol.
    if not email[0].isalpha():
        print("Email should not start with a number, '@' symbol, or non-alphabetic character.")
        return
    
    # 3. The email should contain only 1 '@' symbol.
    if email.count('@') != 1:
        print("Email should contain exactly one '@' symbol.")
        return
    
    # 4. The email should contain at least one '.' symbol after the '@' symbol.
    at_index = email.index('@')
    if '.' not in email[at_index:]:
        print("Email should contain at least one '.' symbol after the '@' symbol.")
        return
    
    # 5. The email should not contain any uppercase letters.
    if any(char.isupper() for char in email):
        print("Email should not contain any uppercase letters.")
        return
    
    # 6. Checking for invalid characters
    for char in email:
        if char.isspace():
            print("Email should not contain any spaces.")
            return
        if not (char.isalnum() or char in ['_', '.', '@']):
            print("Email contains invalid characters.")
            return
    
    print("Email is valid.")

# Test the function
email = "your_email@example.com"
validate_email(email)