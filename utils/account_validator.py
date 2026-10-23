
def validate_account_type(account_type):

    if not account_type.strip():
        print("Account cannnot be empty is can be either current account or saving account.")
        return False
    if not account_type.isalpha():
        print("Enter a valid choice. Numbers and special charachter are not allowed.")
        return False
    account_validation=account_type.strip().lower()
    if account_validation not in("current" ,"saving"):
        print("Please enter a valid choice: Current/Saving")
        return False
    return True

def validate_balance(balance):
    if not balance.strip():
        print("Balance cannot be empty.")
        return False
    try:
      valid_balance=float(balance)

    except ValueError:
          print("Enter balance in Numbers.")
          return False
    if valid_balance<=0:
        print("Balance should be greater than 0.")
        return False
    return True






    

