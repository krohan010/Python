# Gloabl Scope -> Variables which are declared outside of a function 
# and are accessible from anywhere is known as..

txt1 = "Global Variable"
def myfunc():                                         #Function Declaration
    # global keyword used to make local variable accessible from outside...
    global txt2
    # Local Scope -> Variable which are declare and used inside of a function is known as..    
    txt2 = "Local Variable"
    txt1 = "Another local variable"                    # Same but local variable..
    print(txt1)                                        # print local variable
    print(txt2)
   

myfunc()
print(txt1)                                            # Print Global Variable
print(txt2)               # it cannot be access until it define as a global variable