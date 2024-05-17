import sys
import os

def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    
    error_message = f"error occured in the file name [{filename}], the linenumber is [{exc_tb.tb_lineno}], and the error is [{str(error)}]"

    return error_message



class SensorException(Exception):

    def __init__(self, error_message) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message
    

