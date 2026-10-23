from datetime import date

class Idgenerator:

    def __init__(self,last_customer_id):
        self.last_customer_id=last_customer_id
    def custid(self):
      cust='cust'+f"{ self.last_customer_id+1:05d}"
      self.last_customer_id=self.last_customer_id+1
      return cust




class Account_number_generator:
   def __init__(self,last_account_number):
      self.last_account_number=last_account_number
   def acc_num(self):
      account_number='ACC'+f"{self.last_account_number+1:04d}"
      self.last_account_number=self.last_account_number+1
      return account_number




class transaction_id_generator:
   def __init__(self,last_transaction_id):
      self.last_transaction_id=last_transaction_id
   def transaction_id_module(self):
      today=date.today()
      tran_id_gen=f"TXN-{today.strftime('%Y%m%d')}-{self.last_transaction_id+1:04d}"
      self.last_transaction_id=self.last_transaction_id+1
      return tran_id_gen


class Credential_id_generator:
   def __init__(self,last_credential_id):
      self.last_credential_id=last_credential_id
   def credential_module(self):
      cred_id=f"{'BANK'}-{date.today()}-{self.last_credential_id+1:02d}"
      self.last_credential_id=self.last_credential_id+1
      return cred_id

