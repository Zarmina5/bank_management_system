class Credential:

    def __init__(self,credential_id,account_number,pin,):
        self.__credential_id=credential_id
        self.__account_number=account_number
        self.__pin=pin

    def setcredential_id(self,credential_id):
        self.__credential_id=credential_id
    def setaccount_number(self,account_number):
        self.__account_number=account_number
    def setpin(self,pin):
        self.__pin=pin

    def getcredential_id(self):
          return  self.__credential_id
    def getaccount_number(self):
            return self.__account_number
    def getpin(self):
           return self.__pin
    



