# must have at least one lowercse and uppercase character
# must have one specaial symbol
# must have one digit symbol
# password length must exceed 8 characters
import re
def check_password_strength(password):
    if len(password)<8:
        return("Your password must be at least 8 characters long")
    pattern = r'[!@#$%^&*(),.?":{}|<>]'
    match = re.findall(pattern, password)
    if match:
        pattern1 = r'[A-Z]'
        match1 = re.findall(pattern1, password)
        if match1:
            pattern2 = r'[a-z]'
            match2 = re.findall(pattern2, password)
            if match2:
                pattern3 = r'[0-9]'
                match3 = re.findall(pattern3, password)
                if match3:
                        return("Your password has been created successfully")
                else:
                        return("Your password must have at least one digit symbol")
            else:
                return("Your password must have at least one lowercase character")
    
        else:
            return("Your password must have at least one uppercase character")
    else:
        return("Your password must have at least one special character")
    
    
password = input("Please enter your password: ")
print(check_password_strength(password))



