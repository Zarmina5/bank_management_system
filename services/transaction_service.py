from utils import transaction_validator,id_generator
from database import db_connection
from models.transaction import Transaction
from datetime import date
from decimal import Decimal
from services import credential_service
from getpass import getpass

def get_last_transaction_id():
    mysql_connection = db_connection.get_connection()
    cursor = mysql_connection.cursor()
    sql = """
    SELECT transaction_id
    FROM transactions
    ORDER BY transaction_id DESC
    LIMIT 1
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    mysql_connection.close()
    if result is None:
        return 0
    last_id = result[0]
    return int(last_id[-4:])

def deposit():
    print("Depositing into account...")
    print("==========================")
    account_number=input("Account Number:")
    mysql_connection=db_connection.get_connection()
    cursor=mysql_connection.cursor()
    sql="SELECT * FROM accounts where account_number=%s"
    values=(account_number,)
    cursor.execute(sql,values)
    result=cursor.fetchone()
    
    if result:
        status=result[5]
        bal=result[3]
        if status=='active': 
           valid=False
           while not valid: 
              deposit_amount=input("Enter the amount you want to deposit:")
              valid=transaction_validator.validating_transactions(deposit_amount)
           converting_amount=Decimal(deposit_amount)
           new_balance=bal+converting_amount
           transaction_type = "deposit"
           transaction_date = date.today()
           last_id = get_last_transaction_id()
           transaction_id = id_generator.transaction_id_generator(last_id)
           transaction_id = transaction_id.transaction_id_module()
           Transaction_object=Transaction(transaction_id,account_number, transaction_type, converting_amount,transaction_date)
           try:
              sql=""" INSERT INTO transactions(transaction_id,account_number,transaction_type,amount,transaction_date)
              values(%s,%s,%s,%s,%s)"""
              values=(Transaction_object.gettransaction_id(),
                   Transaction_object.getaccount_number(),
                   Transaction_object.gettransaction_type(),
                   Transaction_object.getamount(),
                   Transaction_object.gettransaction_date())
              cursor.execute(sql,values)
              sql="update accounts set balance=%s where account_number=%s"
              values=(new_balance,account_number)
              cursor.execute(sql,values)
              mysql_connection.commit()
              print("Amount is deposited successfully.")
           except:
                mysql_connection.rollback()
                print("Transaction failed.")
               
        else:
            print("Your Account is INACTIVE.")
    else:
        print("Account number doesn't exist.")
    cursor.close()
    mysql_connection.close()



def withdraw():
    print("Withdrawal From Account..")
    print("==========================")
    account_number=input("Account Number:")
    mysql_connection=db_connection.get_connection()
    cursor=mysql_connection.cursor()
    sql="SELECT * FROM accounts where account_number=%s"
    values=(account_number,)
    cursor.execute(sql,values)
    result=cursor.fetchone()
    if result:
        status=result[5]
        current_bal=result[3]
        if status=='active':
            pin_verified=credential_service.verify_pin(account_number)  
            if not pin_verified:
                cursor.close
                mysql_connection.close()
                return          
            valid=False
            while not valid:
                withdrawal_amount=input("Enter the amount you want to withdraw:")
                valid=transaction_validator.validating_transactions(withdrawal_amount)
            converting_withdraw_amount=Decimal( withdrawal_amount)
            if  converting_withdraw_amount>current_bal:
                print("The amount you have entered is greater than you bank balance.\nYour balance:",current_bal)
                cursor.close()
                mysql_connection.close()
                return 
            else:
                new_balance=current_bal-converting_withdraw_amount
                transaction_type = "withdraw"
                transaction_date = date.today()
                last_id = get_last_transaction_id()
                transaction_id =id_generator.transaction_id_generator(last_id)
                transaction_id = transaction_id.transaction_id_module()
                Transaction_object=Transaction(transaction_id,account_number, transaction_type, converting_withdraw_amount,transaction_date)

                try:
                     sql=""" INSERT INTO transactions(transaction_id,account_number,transaction_type,amount,transaction_date)
                      values(%s,%s,%s,%s,%s)"""
                     values=(Transaction_object.gettransaction_id(),
                     Transaction_object.getaccount_number(),
                     Transaction_object.gettransaction_type(),
                     Transaction_object.getamount(),
                     Transaction_object.gettransaction_date())
                     cursor.execute(sql,values)
                     sql="update accounts set balance=%s where account_number=%s"
                     values=(new_balance,account_number)
                     cursor.execute(sql,values)
                     mysql_connection.commit()
                     print("Transaction Successfull.")
                except:
                 mysql_connection.rollback()
                 print("Transaction failed.")
                               
        else:
                print("Your Account is INACTIVE.")
                print("You cannot perform transactions on an inactive account.")
                print("Please reactivate your account before using it.")
    else:
         print("Account number doesn't exist.")
    cursor.close()
    mysql_connection.close()




def transaction_history():
    account_number=input("Enter Account Number:")
    mysql_connection=db_connection.get_connection()
    cursor=mysql_connection.cursor()
    sql="""SELECT customers.customer_id,customers.name,accounts.account_number,
    accounts.account_type,accounts.balance,transactions.transaction_id,transactions.transaction_type,
    transactions.amount,transactions.transaction_date 
    from accounts inner join customers
      on customers.customer_id=accounts.customer_id 
      left join transactions 
      on transactions.account_number=accounts.account_number  
      where accounts.account_number=%s"""
    values=(account_number,)
    cursor.execute(sql,values)
    result=cursor.fetchall()
    if result:
        print("_____________________")
        print("Transaction History")
        print("Customer ID:",result[0][0])
        print("Customer name:",result[0][1])
        print("Account Number:",result[0][2])
        print("Account Type:",result[0][3])
        print("Balance:",result[0][4]) 
        trans_id=result[0][5]
        if trans_id==None:
         print("NO TRANSACTION FOUND")
        else:
         print("--------------------------Transactions------------------------------------------")
         print(f"{'Transaction ID':<25}{'Transaction Type':<20}{'Amount':<15}{'Date':<15}") 
         for i in result:
          print(f"{i[5]:<25}{i[6]:<20}{i[7]:<15}{str(i[8]):<15}")
    else:
        print("Account number doesn't exist")


def transfer_money():
        print("=============================")
        print("Transfer Money")
        sender_account_number=input("Sender account number:")
        mysql_connection=db_connection.get_connection()
        cursor=mysql_connection.cursor()
        sql="SELECT * FROM accounts where account_number=%s"
        values=(sender_account_number,)
        cursor.execute(sql,values)
        result=cursor.fetchone()
        if result:
          bal=result[3]
          status=result[5]
          if status=='active':
           pin_verified=credential_service.verify_pin(sender_account_number)
           if not pin_verified:
               cursor.close
               mysql_connection.close
               return                       
           receiver_account_number=input("Receiver account number:")
           if sender_account_number == receiver_account_number:
            print("Sender and receiver accounts cannot be the same.")
            return
           sql="SELECT * FROM accounts where account_number=%s"
           values=(receiver_account_number,)
           cursor.execute(sql,values)
           reciever_result=cursor.fetchone()
           reciever_status=reciever_result[5]
           if reciever_status=='active':        
               valid=False
               while not valid:
                 transfer_amount=input("Transfer amount:")
                 valid=transaction_validator.validating_transactions(transfer_amount)
               convert_amount=Decimal(transfer_amount)
               if bal<convert_amount:
                   print("Transfer Failed.\n Your Balance",bal)
               else:
                   sender_new_balance=bal-convert_amount
                   reciever_current_bal=reciever_result[3]
                   receiver_new_balance = reciever_current_bal+convert_amount
                   try:
                    #    sender
                     last_id = get_last_transaction_id()
                     sender_transaction_id =id_generator.transaction_id_generator(last_id)
                     sender_transaction_id = sender_transaction_id.transaction_id_module()
                     sql="update accounts set balance=%s where account_number=%s"
                     values=(sender_new_balance,sender_account_number)
                     cursor.execute(sql,values)
                     transaction_type="Transfer"
                     transfer_date=date.today()

                     Transaction_object=Transaction(sender_transaction_id,sender_account_number,transaction_type,convert_amount,transfer_date)
                     sql=""" INSERT INTO transactions(transaction_id,account_number,transaction_type,amount,transaction_date)
                        values(%s,%s,%s,%s,%s)"""
                     values=(Transaction_object.gettransaction_id(),
                            Transaction_object.getaccount_number(),
                            Transaction_object.gettransaction_type(),
                            Transaction_object.getamount(),
                            Transaction_object.gettransaction_date())
                     cursor.execute(sql,values)

                     
                    #    receiver 
                     sql="update accounts set balance=%s where account_number=%s"
                     values=(receiver_new_balance,receiver_account_number)
                     cursor.execute(sql,values)
                     convertion_str_int=int(sender_transaction_id[-4:])
                     transaction_id =id_generator.transaction_id_generator( convertion_str_int)
                     transaction_id = transaction_id.transaction_id_module()
                     transaction_type="Receive"
                     transfer_date=date.today()
                     
                     Transaction_object=Transaction(transaction_id,receiver_account_number,transaction_type,convert_amount,transfer_date)
                     sql=""" INSERT INTO transactions(transaction_id,account_number,transaction_type,amount,transaction_date)
                                             values(%s,%s,%s,%s,%s)"""
                     values=(Transaction_object.gettransaction_id(),
                                                 Transaction_object.getaccount_number(),
                                                 Transaction_object.gettransaction_type(),
                                                 Transaction_object.getamount(),
                                                 Transaction_object.gettransaction_date())
                     cursor.execute(sql,values)
                         
                     mysql_connection.commit()
                     print("Transfer Successful")
                     print("Sender new balance:", sender_new_balance)
                     print("Reciever new balance:", receiver_new_balance)
                     print("Amount Transfered:", convert_amount)
                   except Exception as e:
                       mysql_connection.rollback()
                       print("Transfer failed..")
                       print("error",e)
                
           else:
               print("Receiver account is inactive.") 
          else:
            print("Sender account is Inactive.")
        else:
            print("Account Number doesn't exist.")
        cursor.close
        mysql_connection.close

                   
                   
            

            


