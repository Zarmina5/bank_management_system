from models.customer import Customer
from database import db_connection
from utils import customer_validator
from utils.id_generator import Idgenerator
def get_last_customer_id():
    mysql_connection = db_connection.get_connection()
    cursor = mysql_connection.cursor()

    sql = """
    SELECT customer_id
    FROM customers
    ORDER BY customer_id DESC
    LIMIT 1
    """

    cursor.execute(sql)

    result = cursor.fetchone()

    cursor.close()
    mysql_connection.close()

    if result is None:
        return 0

    last_id = result[0]
    return int(last_id[4:])


def customer_info():

    print("__________________________")
    print("ENTER CUSTOMER INFORMATION")
   #  FULL NAME 
    valid=False
    while not valid:
     name=input("Full Name:")
   #   true returned by the validate function is store in name enter
     valid=customer_validator.validate(name)

   #   FATHER'S NAME
    valid=False
    while not valid:
     father_name=input("Father Name:")
     valid=customer_validator.validate(father_name)

   #   DATE OF BIRTH 
    valid=False
    while not valid:
       dob=input("Date Of Birth:")
       valid=customer_validator.validate_dob(dob)
    

   #  GENDER
    valid=False
    while not valid:
       gender=input("Gender:")
       valid=customer_validator.validate_gender(gender)

   #CNIC
    valid=False
    while not valid:
      cnic=input("CNIC:")
      valid=customer_validator.validate_cnic(cnic)

   # OCCUPATION OR SOURCE OF INCOME
    valid=False
    while not valid:
        occupation=input("Occupation:")
        valid=customer_validator.validate_occupation(occupation)

    # INCOME
    valid=False
    while not valid:
      mon_income=input("Income:")
      valid=customer_validator.validate_mon_income(mon_income)
    income=float(mon_income)

    

      # PHONE NUMBER
    valid=False
    while not valid:
      phone_num=input("Phone Number:")
      valid=customer_validator.validate_number(phone_num)

      #  EMAIL
    valid=False
    while not valid:
     email=input("Email:")
     valid=customer_validator.validate_email(email)

      # ADDRESS  
    valid=False
    while not valid:
     address=input("Address:")
     valid=customer_validator.validate_address(address)

      # CITY
    valid=False
    while not valid:
     city=input("City:")
     valid=customer_validator.validate_City(city)

    last_id = get_last_customer_id()
    generator = Idgenerator(last_id)
    customer_id = generator.custid()

    


    #  SQL AND PYTHON CONNECTION
# object
    customer=Customer(customer_id,name,father_name,dob,gender,cnic,occupation,income,phone_num,email,address,city)
#  establishes the communication between Python and MySQL
    mysql_connection=db_connection.get_connection()
    # cursor =>sql_connection → your active connection between Python and MySQL
    # .cursor() → asks that connection to create a cursor.
    # cursor → stores that cursor so you can use it to send SQL commands.cursor will be responsibel for sendign sql commands
    cursor = mysql_connection.cursor()
    sql = """
    INSERT INTO customers
    (customer_id, name, father_name, dob, gender, cnic, occupation,
    monthly_income, phone, email, address, city)
    VALUES (%s, %s, %s, STR_TO_DATE(%s, '%d/%m/%Y'), %s, %s, %s, %s, %s, %s, %s, %s)
    """
     # These %s are placeholders. 
    values = (
    customer.getid(),
    customer.getname(),
    customer.getfather_name(),
    customer.getdob(),
    customer.getgender(),
    customer.getcnic(),
    customer.getoccupation(),
    customer.getmon_income(),
    customer.getphone(),
    customer.getemail(),
    customer.getaddress(),
    customer.getcity()
)
    # execute(sql, values):You give the cursor both the SQL instruction and the actual values, and it sends the operation to MySQL.
    cursor.execute(sql, values)
    # commit() This confirms the change so the inserted customer record is saved permanently.
    mysql_connection.commit()
    # You're finished using the cursor, so you close it.
    cursor.close()
    # You're finished communicating with MySQL, so you close the connection.
    mysql_connection.close()

    return customer



def search_customer():
    print("_______________________________")
    print("Searching Customer Information..")
    search_id=input(("Enter Customer ID:"))
    mysql_connection=db_connection.get_connection()
    cursor=mysql_connection.cursor()
    sql="select * from customers where customer_id=%s"
    cursor.execute(sql,(search_id,))
    result=cursor.fetchone()
    if result:
       print("Customer ID:", result[0])
       print("Name:", result[1])
       print("Father Name:", result[2])
       print("Date of Birth:", result[3])
       print("Gender:", result[4])
       print("CNIC:", result[5])
       print("Occupation:", result[6])
       print("Monthly Income:", result[7])
       print("Phone:", result[8])
       print("Email:", result[9])
       print("Address:", result[10])
       print("City:", result[11])
       
    else:
       print("ID doesn't exist")
    cursor.close()
    mysql_connection.close()




 
def update_customer():
    print("_______________________________")
    print("Updating Customer Information..")
    search_id=input(("Enter Customer ID:"))
    mysql_connection=db_connection.get_connection()
    cursor=mysql_connection.cursor()
    sql="SELECT * FROM customers WHERE customer_id=%s"
    # Execute the SELECT query and put search_id into the %s placeholder.
    cursor.execute(sql,(search_id,)) 
    # fetchone() mean:Give me the first matching row that MySQL found 
    # Customer exists → result contains that customer's row
    result=cursor.fetchone()
    if result:
     print("Customer Found")
     select=-1
     while select!=0:
             print("Updating Menu...")
             print("_________________")
             print("What do you want to change..")
             print("1.Name")
             print("2.Father Name")
             print("3.Date Of Birth")
             print("4.Gender")
             print("5.Cnic")
             print("6.Occupation")
             print("7.Income")
             print("8.Phone Number")
             print("9.Email")
             print("10.Address")
             print("11.City")
             print("If you want to exit press 0")
             select=int(input("Enter your choice:"))

             if select==1:
                 valid=False
                 while not valid:
                  new_name=input("Enter updated name:")
                  valid=customer_validator.validate(new_name)

                #   assinging updated name
                 sql="UPDATE customers SET name=%s WHERE customer_id=%s"
                 values=(new_name,search_id)
                 cursor.execute(sql,values)
                 mysql_connection.commit()
                 print("Name Updated Successfully...")
                 print("============================")
             elif select==2:
                 valid=False
                 while not valid:
                    updated_father_name=input("Enter updated name:")
                    valid=customer_validator.validate(updated_father_name)
                 sql="UPDATE customers set father_name=%s where customer_id=%s"
                    # values = the actual data that fills the placeholders
                 values=(updated_father_name,search_id)
                    # send the query +values to mysql to perform the update 
                 cursor.execute(sql,values)
                    # permanently save the changes
                 mysql_connection.commit()
                 print("Father Name Updated Succesfully...")
                 print("===================================")

             elif select==3:
                 valid=False
                 while not valid:
                    new_dob=input("Enter updated Date Of Birth:")
                    valid=customer_validator.validate_dob(new_dob)
                 sql="UPDATE customers set dob=STR_TO_DATE(%s, '%d/%m/%Y') where customer_id=%s"
                 values=(new_dob,search_id)
                 cursor.execute(sql,values)
                 mysql_connection.commit()
                 print("Date Of Birth Updated Successfully..")
                 print("====================================")

             elif select==4:
                 valid=False
                 while not valid:
                   new_gender=input("Enter updated Gender:")
                   valid=customer_validator.validate_gender(new_gender)
                 sql="UPDATE customers set gender=%s where customer_id=%s"
                 values=(new_gender,search_id)
                 cursor.execute(sql,values)
                 mysql_connection.commit()
                 print("Gender Updated Successfully..")
                 print("====================================")

             elif select==5:
                 valid=False
                 while not valid:
                  new_cnic=input("Enter updated cnic:")
                  valid=customer_validator.validate_cnic(new_cnic)
                 sql="UPDATE customers set cnic=%s where customer_id=%s"
                 values=(new_cnic,search_id)
                 cursor.execute(sql,values)
                 mysql_connection.commit()
                 print("cnic Updated Successfully..")
                 print("====================================")

             elif select==6:
                 valid=False
                 while not valid:
                  new_occupation=input("Enter updated occupation:")
                  valid=customer_validator.validate_occupation(new_occupation)
                 sql="update customers set occupation=%s where customer_id=%s"
                 values=(new_occupation,search_id)
                 cursor.execute(sql,values)
                 mysql_connection.commit()
                
                 print("Occupation Updated Successfully..")
                 print("====================================")

             elif select==7:
                 valid=False
                 while not valid:
                  new_income=input("Enter updated Income:")
                  valid=customer_validator.validate_mon_income(new_income)
                 convert_income=float(new_income)
                 sql="update customers set monthly_income=%s where customer_id=%s"
                 values=(convert_income,search_id)
                 cursor.execute(sql,values)
                 mysql_connection.commit()
                 print("Income Updated Successfully..")
                 print("====================================")

             elif select==8:
                valid=False
                while not valid:
                  new_number=input("Enter updated or new Phone number:")
                  valid=customer_validator.validate_number(new_number)
                sql="update customers set phone=%s where customer_id=%s"
                values=( new_number,search_id)
                cursor.execute(sql,values)
                mysql_connection.commit()
                print("Phone Number Updated Successfully..")
                print("====================================")

             elif select==9:
                valid=False
                while not valid:
                  new_email=input("Enter updated or new email:")
                  valid=customer_validator.validate_email(new_email)
                sql="update customers set email=%s where customer_id=%s"
                values=( new_email,search_id)
                cursor.execute(sql,values)
                mysql_connection.commit()
                
                print("Email Updated Successfully..")
                print("====================================")

             elif select==10:
                valid=False
                while not valid:
                  new_address=input("Enter updated or new address:")
                  valid=customer_validator.validate_address(new_address)
                sql="update customers set address=%s where customer_id=%s"
                values=( new_address,search_id)
                cursor.execute(sql,values)
                mysql_connection.commit()
                
                print(" Address Updated Successfully..")
                print("====================================")

             elif select==11:
                valid=False
                while not valid:
                 new_city=input("Enter updated city:")
                 valid=customer_validator.validate_City(new_city)
                sql="update customers set city=%s where customer_id=%s"
                values=( new_city,search_id)
                cursor.execute(sql,values)
                mysql_connection.commit()
                
                print("City Updated Successfully..")
                print("====================================")

             else:
                print("Invalid choice..")
     cursor.close()
     mysql_connection.close()
    

    else:
     print("Id doesn't exist")
     print("=================")

def delete_customer():
   print("_______________________________")
   print("Delete Customer Information..")
   search_id=input(("Enter Customer ID:")) 
   mysql_connection=db_connection.get_connection()
   cursor=mysql_connection.cursor()
   sql="SELECT account_number FROM accounts WHERE customer_id=%s"
   values=(search_id,)
   cursor.execute(sql,values)
   result=cursor.fetchone()
   if result:
      print("Cannot delete customer because an account exists for this customer.")
      cursor.close()
      mysql_connection.close()
      return 
   else:
    sql="delete from customers where customer_id=%s"
    cursor.execute(sql,(search_id,))  # after this MYSQL perform the delete operation Now Python needs to know:Did MySQL actually find and delete a customer? thats what rowcount tells us
    if cursor.rowcount>0:
     mysql_connection.commit()
     print("Deletion Successfull...")
    else:
      print("Customer ID doesn't exist.")
    cursor.close()
    mysql_connection.close()
  
def display_customer():
    mysql_connection=db_connection.get_connection()
    cursor=mysql_connection.cursor()
    sql="select * from customers"
    cursor.execute(sql)
    result=cursor.fetchall()
    for i in result:
       print("Customer ID:", i[0])
       print("Name:", i[1])
       print("Father Name:", i[2])
       print("Date Of Birth:",i[3])
       print("Gender:",i[4])
       print("Cnic:",i[5])
       print("Occupation:",i[6])
       print("Income:",i[7])
       print("Phone Number:",i[8])
       print("Email:",i[9])
       print("Address:",i[10])
       print("City:",i[11])
       print("===============================")

    cursor.close()
    mysql_connection.close()


   

         
   




   

        
                                 
                                 
            
                                 
                                 

                                  
                                

            
                                  
                 
                

            
            

                 
                 
            


                





                

   

    

      
      











    






    

   

    


    
    

        
    

