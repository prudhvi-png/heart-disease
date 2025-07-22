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