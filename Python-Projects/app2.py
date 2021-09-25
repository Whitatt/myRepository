

import app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__name__":
    #The following is calling code from within this script
    print("I am running code from {}".format(print_app2()))

    
    #The following is calling code from imported app.py
    print("I am running code from {}".format(print_app()))
