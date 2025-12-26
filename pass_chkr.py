def pss_strng_chckr():
        password =  input("Enter the password you want checked.")

        correct_length = False
        correct_uppercase = False
        correct_lowercase = False
        correct_number = False

        #15 characters?
        if (len(password) > 15):
                correct_length = True
        else:
                print("The password length is ", 15 - len(password), "characters too short")

        #uppercase?
        for i in range(len(password)):
                if(password[i].isupper()):
                        correct_uppercase = True

        #lowercase?
        for i in range(len(password)):
                if(password[i].islower()):
                        correct_lowercase = True

        #number?
        for i in range(len(password)):
                if(password[i].isdigit()):
                        correct_number = True

        #special character
        for char in password:
                if not char.isalnum() and not char.isspace():
                        correct_special = True

        if(correct_length and correct_uppercase and correct_lowercase and correct_number and correct_special): 
                print("This is a sufficient password!")
        else:
                print("This is a poor password")
