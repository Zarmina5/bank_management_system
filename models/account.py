
class Account:

    def __init__(self,account_number,customer_id,account_type,balance,opening_date,status): 
        self.__account_number = account_number
        self.__customer_id = customer_id
        self.__account_type=account_type
        self.__balance=balance
        self.__opening_date=opening_date
        self.__status=status

    # def setaccount_number(self,account_number):
    #     self.__account_number=account_number 
    def setcustomer_id(self,customer_id):
        self.__customer_id=customer_id
    def setaccount_type(self,account_type):
        self.__account_type=account_type
    def setbalance(self,balance):
        self.__balance=balance
    def setopening_date(self,opening_date):
        self.__opening_date=opening_date
    def setstatus(self,status):
        self.__status=status

    def getaccount_number(self):
             return self.__account_number
    def getcustomer_id(self):
          return self.__customer_id
    def getaccount_type(self):
             return self.__account_type
    def getbalance(self):
            return self.__balance
    def getopening_date(self):
             return self.__opening_date
    def getstatus(self):
             return  self.__status


    

    
    
    
        
