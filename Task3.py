def is_valid_email(email):
    if "@" not in email:
        return False
    
    user, domain = email.split("@", 1)
    
    if not user or not domain:
        return False
    
    if "." not in domain:
        return False
    
    return True

email_input = input("Enter an email address: ")
if is_valid_email(email_input):
    print("Valid email address.")
else:
    print("Invalid email address.")