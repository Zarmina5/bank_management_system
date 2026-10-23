



def validating_transactions(amount):
    if not amount.split():
        print("Empty spaces are not allowed.\n Enter amount!")
        return False
    try:
        amount_convertor=float(amount)
    except ValueError:
        print("Enter the amount in Numbers.")
        return False

    if amount_convertor<=0:
        print("The amount shouldn't be less or equal to zero.")
        return False
    return True






    