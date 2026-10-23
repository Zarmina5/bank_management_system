
class Customer:
    
    def __init__(self,customer_id,name,father_name,dob,gender,cnic,occupation,income,phone,email,address,city):
        self.__customer_id=customer_id
        self.__name=name
        self.__father_name=father_name
        self.__dob=dob
        self.__gender=gender
        self.__cnic=cnic
        self.__occupation=occupation
        self.__income=income
        self.__phone=phone
        self.__email=email
        self.__address=address
        self.__city=city

    def setname(self,name):
        self.__name=name
    def setfather_name(self,father_name):
            self.__father_name=father_name
    def setdob(self,dob):
            self.__dob=dob
    def setgender(self,gender):
            self.__gender=gender
    def setcnic(self,cnic):
            self.__cnic=cnic
    def setoccupation(self,occupation):
            self.__occupation=occupation
    def setmon_income(self,income):
         self.__income=income
    def setphone(self,phone):
        self.__phone=phone
    def setemail(self,email):
         self.__email=email
    def setaddress(self,address):
        self.__address=address
    def setcity(self,city):
          self.__city=city

    def getid(self):
         return self.__customer_id
    def getname(self):
        return self.__name
    def getfather_name(self):
            return self.__father_name
    def getdob(self):
        return self.__dob
    def getgender(self):
        return  self.__gender
    def getcnic(self):
        return self.__cnic
    def getoccupation(self):
        return self.__occupation
    def getmon_income(self):
        return self.__income
    def getphone(self):
        return self.__phone
    def getemail(self):
        return self.__email
    def getaddress(self):
        return self.__address
    def getcity(self):
        return self.__city
    def display(self):
         print("DISPLAYING INFORMATION....")
         print("===========================")
         print("Customer ID:",self.getid())
         print("Name:",self.getname())
         print("Father name:",self.getfather_name())
         print("Date of Birth:",self.getdob())
         print("Gender:",self.getgender())
         print("Cnic:",self.getcnic())
         print("Occupation/Source Of Income:",self.getoccupation())
         print("Monthly Income:",self.getmon_income())
         print("Phone Number:",self.getphone())
         print("Email:",self.getemail())
         print("Address",self.getaddress())
         print("City:",self.getcity())
         print("============================")
    

         



    
    
    

    