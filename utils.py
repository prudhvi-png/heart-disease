from exception import CustomException
from logger import logging
import os,sys
import dill
import pickle



def save_object(file_path,obj):
    try:
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def save_info(file_path,model,score):
    try:
        with open(file_path,'w') as file_obj:
            file_obj.write(f"The Winner for this project is {model}, with the accuracy score of {score*100}")
            file_obj.close()
    except Exception as e:
        raise CustomException(e,sys)