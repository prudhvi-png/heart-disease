from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import os
import sys
from utils import save_object
from logger import logging



class DataTransformationConfig:
    def __init__(self):
        self.preprocessor_obj_file_path = os.path.join("models","preprocessor.pkl")

class DataTransformation:
    def __init__(self)->None:
        self.data_transformation_config = DataTransformationConfig()
    
    def get_preprocessor_obj(self):
        independent_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']
        dependent_column = ["target"]

        transformer = ColumnTransformer([
            ("independent_columns",SimpleImputer()),
            ("independent_columns",StandardScaler())
        ])

        save_object(self.data_transformation_config.preprocessor_obj_file_path,transformer)
        logging.info("Successfully saved the preprocessor object!!!")
        
        return transformer

