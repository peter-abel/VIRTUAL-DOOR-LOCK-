

#################################################################
#               VIRTUAL DOOR  LOCK                              #
#                                                               #

#importing datetime module
from datetime import datetime

#This function handles user commands and calls relevant funtions
def prompt1():
    _input = input("Type in your command")
    if _input==open_door:
        _open()
    elif _input == close_door:
        print("The door is not open yet")
        start()
        
    elif _input == _quit:
        quit1()

    else:
         print("Invalid command")
         start()


#This function handles user commands and calls relevant funtions
def prompt2():
    _input1 = input("Type in your command")
    if _input1==open_door:
        opened()
    elif _input1 == close_door:
        close()
        
    elif _input1 == _quit:
        quit1()

    else:
         print("Invalid command")
         prompt2()


#This function handles user commands and calls relevant funtions
def prompt3():
    _input1 = input("Type in your command")
    if _input1==open_door:
        _open()
    elif _input1 == close_door:
        closed()
        
    elif _input1 == _quit:
        quit1()

    else:
         print("Invalid command")
         prompt3()

#This function is called when the user uses command 'open'    
def _open():
    
    x = input("Type in your password")                    
    while x!= pass_word:
        print("wrong password. Try again")
        x = input("Type in your password")
    print("door is now open")
    print("Door last open at:" + str(date))
    prompt2()

 #This function is called when the user uses command 'open' when the door is already open 
def opened():
    print("door is already open")
    _input = input("Type in your command")
    if _input == open_door:
        opened()
    elif _input == close_door:
        close()
        
    elif _input == _quit:
        quit1()

     
    #incase the user types an invalid command
    else:
         print("Invalid command")
         opened()
        
#This function is called when the user uses command 'close'    
def close():
    print("door is now locked")
    print("Door last open at:" + str(date))
    _input = input("Type in your command?")
    if _input == close_door:
        closed()
    else: prompt3()

#This function is called when the user uses command 'close' when door is already closed    
def closed():
    print("the door is already closed")            
    _input = input("Type in your command?")
    if _input == open_door:
        _open()
    elif _input == close_door:
        closed()
        
    elif _input == _quit:
        quit1()

    #incase the user types an invalid command
    else:
         print("Invalid command")
         closed()

 #This function is called when user commands 'quit'        
def quit1():
     print("End of process")
    
#This function calls the prompt1 function
def start():
     
     prompt1()
    
    
if __name__=="__main__":
    date = datetime.today()

    #commands for the door as variables
    open_door = "open"
    close_door = "close"
    _quit = "quit"
    pass_word = "12345"

   #calls start function to begin the program
    start()

    
# END!