from database import db_connection
from utils import account_validator,id_generator,credential_validator
from datetime import datetime
from models.account import Account
from models.credentials import Credential
from services.credential_service import create_credentials


def get_last_account_number():

    mysql_connection = db_connection.get_connection()
    cursor = mysql_connection.cursor()

    sql = """
    SELECT account_number
    FROM accounts
    ORDER BY account_number DESC
    LIMIT 1
    """

    cursor.execute(sql)

    result = cursor.fetchone()

    cursor.close()
    mysql_connection.close()

    if result is None:
        return 0

    last_number = result[0]

    return int(last_number[3:])


def create_account():
    print("===============")
    print("Create Account")
    print("Enter The Information Carefully")
    customer_id=input("Enter customer ID:")
    mysql_connection=db_connection.get_connection()
    sql="select * from customers where customer_id=%s"
    cursor=mysql_connection.cursor()
    values=(customer_id,)
    cursor.execute(sql,values)
    result=cursor.fetchone()
    if result:
     valid=False
     while not valid:
       account_type=input("Account type: Current/Saving..")
       valid=account_validator.validate_account_type(account_type)

     valid=False
     while not valid:
       balance=input("Initial Balance:")
       valid=account_validator.validate_balance(balance)
     bal=float(balance)

     opening_date=datetime.today().date()
     status = "active"
     last_number = get_last_account_number()
     account_num = id_generator.Account_number_generator(last_number)
     account_number = account_num.acc_num()

     account_object=Account(account_number,customer_id,account_type,bal,opening_date,status)
     
     cursor=mysql_connection.cursor()
     sql="""
      INSERT INTO accounts(account_number,customer_id,account_type,balance,opening_date,status)
      VALUES (%s,%s,%s,%s,%s,%s)
               """
     values=( 
          account_object.getaccount_number(),
             account_object.getcustomer_id(),
             account_object.getaccount_type(),
             account_object.getbalance(),
             account_object.getopening_date(),
             account_object.getstatus()
             )
     cursor.execute(sql,values)
       #  Pin 
     credentials_created=create_credentials(account_number,mysql_connection, cursor)
     if not credentials_created:
        mysql_connection.rollback()
        cursor.close()
        mysql_connection.close()
        return None
     mysql_connection.commit()
     cursor.close()
     mysql_connection.close()


  

     return account_object
    else:
     print("ID doesn't exist..")
     return None

def display_accounts():
  mysql_connection=db_connection.get_connection()
  cursor=mysql_connection.cursor()
  sql="select * from accounts"
  cursor.execute(sql)
  result=cursor.fetchall()
  print("Displaying Customers Account Information..")
  print("__________________________________________")
  for i in result:  
    print("Account Number:",i[0])
    print("Customer ID:",i[1])
    print("Account Type:",i[2])
    print("Balance:",i[3])
    print("Opening Date:",i[4])
    print("Status:",i[5])
    print("==========================")

  cursor.close()
  mysql_connection.close()


def search_accounts():
  account_number=input("Enter Account Number:")
  sql_connection=db_connection.get_connection()
  cursor=sql_connection.cursor()
  sql="select * from accounts where account_number=%s"
  values=(account_number,)
  cursor.execute(sql,values)
  result=cursor.fetchone()
  if result:
   print("Searching Displaying Customer Account Information")
   print("=================================================")
   print("Account Number:",result[0])
   print("Customer ID:",result[1])
   print("Account Type:",result[2])
   print("Balance:",result[3])
   print("Opening Date:",result[4])
   print("Status:",result[5])
  else:
    print("Customer ID doesn't exist.")


def update_accounts():
  account_number=input("Enter Account Number:")
  sql_connection=db_connection.get_connection()
  cursor=sql_connection.cursor()
  sql="select * from accounts where account_number=%s"
  values=(account_number,)
  cursor.execute(sql,values)
  result=cursor.fetchone()
  if result:
     current_status=result[5]
     print("Searching Displaying Customer Account Information")
     print("=================================================")
     print("Account Number:",result[0])
     print("Customer ID:",result[1])
     print("Account Type:",result[2])
     print("Balance:",result[3])
     print("Opening Date:",result[4])
     print("Status:",result[5])
     print("=========================")
     choice=-1
     while choice!=0:
      print("Updating Account's Details")
      print("==========================")
      print("Choose what do you want to change...")
      print("1.Account Type")
      print("2.Status")
      print("Press 0 to exit..:")
      choice=int(input("Enter your choice:"))

      if choice==1:
       print("Changing Account Type")
       print("=====================")
       valid=False
       while not valid:
         type_updation=input("Account type: Current/Saving..")
         valid=account_validator.validate_account_type(type_updation)
       sql="update accounts set account_type=%s where account_number=%s"
       values=(type_updation,account_number)
       cursor.execute(sql,values)
       sql_connection.commit()
       print("updation successfull...")
      elif choice==2:
         print("Changing Account Status")
         print("========================")
        
         if current_status =='active':
          new_status='inactive'
         else:
           new_status='active'
         sql="update accounts set status=%s where account_number=%s"
         values=(new_status,account_number)
         cursor.execute(sql,values)
         sql_connection.commit()
         current_status=new_status
         print("updation successfull...")
        
      elif choice==0:
       print("Exiting...!")
       break
      else:
       print("Invalid choice entry!")
     cursor.close()
     sql_connection.close()
  else:
    print("Account Number is not found..")

def delete_account():
  print("Deleting Customer Account Details")
  print("=================================")
  account_number=input("Enter Account Number:")
  sql_connection=db_connection.get_connection()
  cursor=sql_connection.cursor()
  sql="select transaction_id from transactions where account_number=%s LIMIT 1"
  values=(account_number,)
  cursor.execute(sql,values)
  result=cursor.fetchone()
  if result:
    print("Cannot delete account because transaction records exist for this account.")
    cursor.close()
    sql_connection.close()
  else:
   sql="DELETE from accounts where account_number=%s"
   values=(account_number,)
   cursor.execute(sql,values)
   if cursor.rowcount>0:
     sql_connection.commit()
     print("Deletion Successfull....")
   else:
    print("Customer ID doesn't exist..")
  cursor.close()
  sql_connection.close()
  






