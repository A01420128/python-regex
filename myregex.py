import re

def email(str):    
    p = re.compile(r"[\w]+[\w.]*[\w]+@[\w]{3,}(.[a-z]{2,4}){1,2}$")
    m = p.match(str)
    return True if m else False

def phone_number(str):
    p = re.compile(r"(\+1 ?(\([0-9]{1,3}\)))? ?[0-9]{2} ?[0-9]{4} ?[0-9]{4}$")
    m = p.match(str)
    return True if m else False
    
def hexadecimal(str):
    p = re.compile(r"0x([0-9a-fA-F]{2})+$")
    m = p.match(str)
    return True if m else False
