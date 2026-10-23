from utils.id_generator import transaction_id_generator

class Transaction:
    transaction_id=transaction_id_generator(0)
    def __init__(self,transaction_id,account_number, transaction_type, amount,transaction_date):
        self.__transaction_id=transaction_id
        self.__account_number=account_number
        self.__transaction_type= transaction_type
        self.__amount=amount
        self.__transaction_date= transaction_date

    def setaccount_number(self,account_number):
        self.__account_number=account_number
    def settransaction_type(self,transaction_type):
            self.__transaction_type=transaction_type
    def setamount(self,amount):
            self.__amount=amount
    def settransaction_date(self,transaction_date):
            self.__transaction_date=transaction_date
    
    def gettransaction_id(self):
           return self.__transaction_id
    def getaccount_number(self):
           return self.__account_number
    def gettransaction_type(self):
             return self.__transaction_type
    def getamount(self):
             return self.__amount
    def gettransaction_date(self):
             return self.__transaction_date
        
    
