# we need it because we want to check whether the DOB the customer enters is a real date
# we need this lib to recongnize and validate dates
from datetime import datetime
def validate(names):
        word_valid=True
       # If after removing the outside spaces nothing is left then the name is invalid.
       # strip is use to remove empty spaces
        if not names.strip():
           print("NO NAME...EMPTY BLOCK IS NOT ALLOWED ")
           return False 
           # split() gives you the individual words not characters
           # isalpha is use to check weather all are char
        for word in names.split():
           if not word.isalpha():
               print("SPECIAL CHARACTERS AND NUMBERS ARE NOT ALLOWED")
               word_valid=False
        if not word_valid:
            return False
        if  len(names)<4 or len(names)>50:
           print("YOUR NAME SHOULD CONTAIN MINIMUM OF 4 LETTERS AND MAXIMUM OF 50 LETTERS")
           return False  
        
        # the function sends true  to wherever its called 
        return True

def validate_dob(dob):
   # cheking if date is entered empty means empty string
   if not dob.strip():
      print("DOB CANNOT BE EMPTY.. ")
      return False
   # here we are checking the format of the date 
   try: 
      # Python, take whatever is inside dob and try to interpret it as day/month/year
      date=datetime.strptime(dob,"%d/%m/%Y")

   except Exception as e:
      print("THE FORMAT SHOULD BE IN DD/MM/YYYY")
      return False 
   # here we are checking that the date should not be greater than todays date 
   if date>datetime.today():
      print("Date shouldn't be greater than todays date")
      return False
   
   return True

def validate_gender(gender):
   if not gender.strip():
      print("EMPTY STRING IS NOT ALLOWED...")
      return False
   
   # this is the chaining method we can use 2 builtin function at the same time 
   gender_lower=gender.lower().strip()
   if gender_lower not in ('male','female','others') :
      print("INVALID ENTRY..CHOOSE THE GENDER CORRECTLY")
      return False
   return True

def validate_cnic(cnic):
   if not cnic.strip():
      print("EMPTY SPACES ARE NOT ALLOWED...")
      return False
# this means after cutting the cnic at every - did i get 3 pieces
#  split gives us a list now we can easily access list parts by indexing
# cnic.split()Take the CNIC string and split/cut it wherever a - appears
   val_checking=cnic.split("-")
   if len(val_checking)!=3:
      print("CHECK THE LENGTH OF CNIC")
      return False
   # checking weather the numbers in cnic format are correct or not
   if len(val_checking[0])!=5:
        print("FIRST PART OF CNIC SHOULD HAVE 5 DIGITS")
        return False
   if  len(val_checking[1])!=7:
      print("MID PART OF CNIC SHOULD HAVE 7 DIGITS")
      return False
   if len(val_checking[2])!=1:
      print("lAST PART OF CNIC SHOULD HAVE 1 DIGIT")
      return False
   # checking if the input is digits or not 
   if not val_checking[0].isdigit():
           print("INVALID INPUT..ONLY DIGITS ARE ALLOWED")
           return False
   if not val_checking[1].isdigit():
         print("INVALID INPUT..ONLY DIGITS ARE ALLOWED")
         return False
   if not val_checking[2].isdigit():
         print("INVALID INPUT..ONLY DIGITS ARE ALLOWED")
         return False
   return True

def validate_occupation(occupation):
    if not occupation.strip():
        print("EMPTY SPACES ARE NOT ALLOWED...")
        return False
    word_valid=True
    for word in occupation.split():
     if not word.isalpha():
        print("NUMBERS AND SPECIAL CHARACTERS  ARE NOT ALLOWED...")
        word_valid= False
     if not word_valid:
         return False
    return True

def validate_mon_income(mon_income):   
    if not mon_income.strip():
        print("EMPTY SPACES ARE NOT ALLOWED..")
        return False
    try:
        income=float(mon_income)
    except Exception as e:
         print("ENTER YOUR SALARY IN NUMBERS..")
         return False
    if income<=0:
        print("INCOME CANNOT BE NEGATIVE OR ZERO..")
        return False
    return True

def validate_number(phone_number):
    if not phone_number.strip():
        print("EMPTY SPACES ARE NOT ALLOWED...")
        return False
    if len(phone_number)!=11:
        print("INVALID INPUT..\n PHONE NUMBER HAVE 11 DIGITS")
        return False
    if not phone_number.isdigit():
        print("ONLY NUMBERS ARE ALLOWED...")
        return False
    return True

def validate_email(email):
    if not email.strip():
      print("EMAIL CANNOT BE EMPTY OR ONLY SPACES...")
      return False

   #  now we need to check @ in email using either "in" operator or either find
    if  "@" not in email:
        print("FORMAT OF EMAIL IS WRONG..")
        return False 
    if  "." not in email:
            print("FORMAT OF EMAIL IS WRONG..")
            return False
  
    email_checking=email.split("@")
     #  now to check we have only one @
    if len(email_checking)!=2:
        print("INVALID FORMAT..")
        return False

 #  now we will check the part before and after@ weather it had something or not
    if  not email_checking[0].strip():
        print("WRONG FORMAT")
        return False
    if not email_checking[1].strip():
        print("WRONG FORMAT")
        return False

   #   now we have to check the parts before and after the dot 
    email_checking_dot=email.split("@")
    further_splitting=email_checking_dot[1].split(".")
    if not further_splitting[0].strip():
        print("INVALID FORMAT...")
        return False
    if not further_splitting[1].strip():
       print("INVALID FORMAT...")
       return False

   #  now we have to check spaces 
    if " " in email:
        print(" SPACES ARE NOT ALLOWED")
        return False

   #  now to check consecutive dots 
    if ".." in email:
        print("YOU CANNOT ADD MORE THAN 1 DOT")
        return False
    
   #for checking Valid TOP LEVEL domains  
    if not further_splitting[1].isalpha():
        print("ENTER A VALID TLD")
        return False
    if len(further_splitting[1])<2:
        print("ENTER A VALID TLD..")
        return False
    return True 


def validate_address(address):
     if not address.strip():
          print("ADDRESS CANNOT BE EMPTY OR ONLY SPACES...")
          return False
     if len(address)<4:
         print("ENTER A VALID AND PROPER ADDRESS")
         return False
     return True

def validate_City(city):
        if not city.strip():
          print("CITY CANNOT BE EMPTY OR ONLY SPACES...")
          return False
               
        for word in city.split():
            if not word.isalpha():
                print("ENTER CORRECT CITY NAME")
                return False          
        return True