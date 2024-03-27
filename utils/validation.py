import re

class Validation():
    def __init__(self) -> None:
        pass
    
    def is_valid_email(self, email):
        pattern = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.match(pattern, email)
    
    def is_valid_password(self, password):
        if(len(password) < 8):
            return False
        
        if not any(c.isdigit() for c in password):
            return False
        
        if not re.search("[@_!#$%^&*()<>?/\|}{:]", password):
            return False
        
        return True
    

    def is_valid_first_name(self, first_name):
        if(len(first_name) <= 3):
            return False
        
        return True
    

    def is_valid_last_name(self, last_name):
        if(len(last_name) < 2):
            return False
        
        return True