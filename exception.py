import exception
import sys
import os


def custom_message(error_msg,error_detail:sys):
    _,_,error_tb = error_detail.exc_info()
    filename = error_tb.tb_frame.f_code.co_filename
    lineno = error_tb.tb_lineno
    craft_message = f"(Error occured in [{filename}], in the no [{lineno}] and the error msg[{error_msg}] !!!!!)"
    return craft_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = custom_message(error_message,error_detail)

    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        print(10/0)
    except Exception as e:
        raise CustomException(e,sys)