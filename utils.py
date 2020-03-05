#Utils file that holds various misc. utility functions.

#Logging utlity that just logs out whatever is passed to it.
#Param level int 1-3; Level of verbosity.
class Logger():
    def __init__(self, level=1):
        self.level = level
    
    #Log function logs the message to the console.
    #Param message string; Message to print.
    #Param is_priority bool; Should message be sent when log level is 1?
    def log(self, message, is_priority):
        if self.level == 0:
            return
        elif self.level == 1 and is_priority == True:
            print(message)
        elif self.level == 2:
            print(message)

#Utility function to test for empty variables
#Param value any; checks if a value is "empty"
def empty(value):
    try:
        value = float(value)
    except ValueError:
        pass
    return bool(value)