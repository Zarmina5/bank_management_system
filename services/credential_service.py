
from database import db_connection
from utils import id_generator,credential_validator
from models.credentials import Credential
from getpass import getpass

def get_last_credential_id():
    mysql_connection = db_connection.get_connection()
    cursor = mysql_connection.cursor()
    sql = """
    SELECT credential_id
    FROM credentials
    ORDER BY credential_id DESC
    LIMIT 1
   """
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    mysql_connection.close()
    if result is None:
        return 0
    last_number = result[0]
    return int(last_number[-2:])


def create_credentials(account_number, mysql_connection, cursor):
  print("SETTING PIN")
  print("==========================")
  valid=False
  while not valid:
   pin=getpass("Enter PIN:")
   valid=credential_validator.validate_pin(pin)

  
  sql="INSERT INTO credentials(credential_id,account_number,pin) values(%s,%s,%s)"
  last_id=get_last_credential_id()
  cred_id=id_generator.Credential_id_generator(last_id)
  credential_id=cred_id.credential_module()
  credential_object=Credential(credential_id,account_number,pin)
  values=(credential_object.getcredential_id(),credential_object.getaccount_number(),credential_object.getpin())
  try:
    cursor.execute(sql,values)
    print("PIN set successfully.")
    return True
  except:
    mysql_connection.rollback()
    print("Setting PIN is failed.")
    return False


def verify_pin(account_number):
   pin=getpass("Enter PIN:")
   mysql_connection=db_connection.get_connection()
   cursor=mysql_connection.cursor()
   sql="SELECT * from credentials where account_number=%s"
   values=(account_number,)
   cursor.execute(sql,values)
   result=cursor.fetchone()
   if result:
     pin_entered=result[2]
     if pin_entered==pin:
       print("PIN is correct")
       cursor.close()
       mysql_connection.close()
       return True
     else:
        print("Your PIN is incorrect.")
        cursor.close()
        mysql_connection.close()
        return False
     
   else:
      print("Account Number is not found.")
      cursor.close()
      mysql_connection.close()
      return None



def updating_pin():
   print("=============")
   print("Changing PIN")
   print("=============")
   account_number=input("Enter account number:")
   mysql_connection=db_connection.get_connection()
   cursor=mysql_connection.cursor()
   sql="SELECT * from credentials where account_number=%s"
   values=(account_number,)
   cursor.execute(sql,values)
   result=cursor.fetchone()
   if result:
      pre_pin=result[2]
      pin=getpass("Enter your existing PIN:")
      if pre_pin==pin:
         valid=False
         while not valid:
          new_pin=getpass("New PIN:")
          valid=credential_validator.validate_pin(new_pin)
         confirm_pin=getpass("Confirm PIN:")
         if new_pin==confirm_pin:
            sql="update credentials set pin=%s where account_number=%s"
            values=(new_pin,account_number) 
            try:
             cursor.execute(sql,values)
             mysql_connection.commit()
             print("PIN CHANGED SUCCESSFULLY.")
            except Exception as e:
               mysql_connection.rollback()
               print("PIN updation failed.")
               print("Error:",e)
               cursor.close()
               mysql_connection.close()
               return
         else:
            print("Enter wrong confirmation PIN.")
      else:
         print("Wrong PIN")
   else:
      print("Account number doesn't exist.")
   cursor.close()
   mysql_connection.close()
      
        

         

   




    
 
