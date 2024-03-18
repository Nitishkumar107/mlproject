import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename   # it will give the filename of the error
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    

class CustomException(Exception):  # to call the error function
    def __init__(self,error_message,error_detail:sys):   # constructor
        super().__init__(error_message) # inherited from init function
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message


    
