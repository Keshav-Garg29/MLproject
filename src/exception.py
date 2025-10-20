import sys #sys has exc_info() function that gives us detailed information about errors (exceptions) when they happen.

def error_message_detail(error,error_detail:sys):  #This function creates a detailed error message. error: The actual error message (e.g., "File not found"). error_detail: The sys module (to access error details)
    _,_,exc_tb =  error_detail.exc_info() #Gets information about the error that just happened
    #error_detail.exc_info()` returns 3 things:
    #1. Error type (e.g., ValueError, FileNotFoundError)
    #2. Error value (the actual error message)
    #3. Traceback object (contains WHERE the error happened)

    file_name = exc_tb.tb_frame.f_code.co_filename #Extracts the name of the Python file where error occurred

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name , exc_tb.tb_lineno , str(error))
#   {0} → `file_name` (which file?)
#   {1} → `exc_tb.tb_lineno` (which line number?)
#   {2} → `str(error)` (what went wrong?)

    return error_message #Returns the detailed error message we just created

 
class CustomException(Exception): #Creates a new class called CustomException that inherits from Python's built-in Exception class
    def __init__(self, error_message , error_detail:sys): #Initializes the custom exception when it's created
        super().__init__(error_message) #Calls the parent class (Exception) constructor
        self.error_message = error_message_detail(error_message , error_detail=error_detail) #Calls the error_message_detail function we created earlier and stores the result

    def __str__(self): #Defines what gets printed when you print this exception
        return self.error_message