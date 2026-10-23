def validate_pin(pin):
    if not pin.strip():
        print("Empty spaces are not allowed.\n Please enter a valid password.")
        return False
    if len(pin)!=4:
        print("PIN should have 4 digits.")
        return False
    if not pin.isdigit():
       print("PIN should have numbers only.\n Characters and Symbols are not allowed.")
       return False
    
    return True
            

    
      
    
