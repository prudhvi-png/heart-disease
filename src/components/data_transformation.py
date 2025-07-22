from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os
import sys
from utils import save_object
from logger import logging
from exception import CustomException
import numpy as np
import pandas as pd



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

        num_pipeline = Pipeline(
            [("imputer",SimpleImputer()),
            ("scaler",StandardScaler())]
        )

        transformer = ColumnTransformer(
            [("num_pipeline",num_pipeline,independent_columns)]
        )

        
        logging.info("Successfully saved the preprocessor object!!!")
        
        return transformer
    
    def initiate_data_transformation(self,train_df,test_df):
        try:

            preprocessor_obj = self.get_preprocessor_obj()
            target_column = "target"

            data_for_train = pd.read_csv(train_df)
            data_for_test = pd.read_csv(test_df)

            independent_train_data = data_for_train.drop(target_column,axis=1)
            dependent_train_data = data_for_train[target_column]

            independent_test_data = data_for_test.drop(target_column,axis=1)
            dependent_test_data = data_for_test[target_column]

            logging.info("Applying preprocessor obj ")
            independent_train_data = preprocessor_obj.fit_transform(independent_train_data)
            independent_test_data = preprocessor_obj.transform(independent_test_data)

            train_data = np.c_[independent_train_data,np.array(dependent_train_data)]
            test_data = np.c_[independent_test_data,np.array(dependent_test_data)]

            logging.info("data initiation completed !!! ")

            save_object(
                self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            return (
                train_data,
                test_data,
                preprocessor_obj)

            
        except Exception as e:
            raise CustomException(e,sys)

