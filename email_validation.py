import re

#define a function

def email_validation(email):

#this is a REGEX pattern used for email validation

   
    pattern= r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

#using re.match function to check the pattern and email address to be True or False according to the REGEX pattern
  
    if re.match(pattern, email):
        return True
    else:
        return False
    
#prompt for user to enter email

email=input("please enter your email to validate")

#these if &else will use to function email_valdation to print result whatever be the condition checked by the def function above

if email_validation(email):
    print("Valid email")

else:
    print("invalid")    