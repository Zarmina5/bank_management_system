from services import customer_service,account_services,transaction_service,credential_service

choice=-1
while choice!=0:
    print("________________________________")
    print("Bank Account Management System")
    print("________________________")
    print("1.Add Customer Information")
    print("2.Display Customer Information")
    print("3.Search Customer Information ")
    print("4.Update Customer Information")
    print("5.Delete Customer Information")
    print("6.Create Account")
    print("7.Display Account Details")
    print("8.Search Account")
    print("9.Update Account")
    print("10.Delete Account")
    print("11.Deposit Money")
    print("12.Withdraw Money")
    print("13.Transaction History")
    print("14.Send Money")
    print("15.Change PIN")
    print("0.Exit..press '0' to Exit")
    choice=int(input("Enter Your Choice:"))
    print("________________________________")

    if choice==1:
        cust_info=customer_service.customer_info()
    elif choice==2:
       customer_service.display_customer()
    elif choice==3:
           customer_service.search_customer()
    elif choice==4:
       customer_service.update_customer()
    elif choice==5:
       customer_service.delete_customer()
    elif choice==6:
        account_services.create_account()
    elif choice==7:
        account_services.display_accounts()
    elif choice==8:
        account_services.search_accounts()
    elif choice==9:
        account_services.update_accounts()
    elif choice==10:
        account_services.delete_account()
    elif choice==11:
        transaction_service.deposit()
    elif choice==12:
        transaction_service.withdraw()
    elif choice==13:
        transaction_service.transaction_history()
    elif choice==14:
        transaction_service.transfer_money()
    elif choice==15:
        credential_service.updating_pin()
    elif choice==0:
        print("Exiting..")
        break
   
        


       
       
       
    

