import re

#Function to check if the phone number is a valid Indian Number or not
def phone_numbers(ph_number):
    regex=re.compile('^((\+)?91)(\ )?(\d{10})$',re.VERBOSE)
    ph=regex.search(ph_number)
    if ph is None:
        print("No, "+ph_number+" is not a valid Indian Ph. number")
    else:
        print("Yes, "+ph_number +" is a valid Indian Ph. number")


#Input Phone number
response =input("Please enter your phone number \n")

#Call the function "phone_numbers"
phone_numbers((str(response))




