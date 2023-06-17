class user:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

class registration(user):
     def __init__(self,name,email,password):
        super().__init__(name,email,password)
        
name =input("Enter the name of the user ")
email =input("Enter the email of the user ")
password = input("Enter the password of the user ")
confirmation = input("Please re-enter your e-mail id ")
if(confirmation == email):
        print("Registration successful")
else:
     print("Please register again ")
     email = 0
user_registration = registration(name,email,password)
user_registration.display_info()

file = open("userdetails.txt", "w")
file.write(f"Name: {user_registration.name}\n")
file.write(f"Email: {user_registration.email}\n")
file.write(f"Password: {user_registration.password}\n")
file.close()

