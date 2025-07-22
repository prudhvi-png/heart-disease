from exception import CustomException
from src.components.data_ingestion import DataIngestion
import pyjokes
from src.components.data_transformation import DataTransformation
import pandas as pd
from src.components.model_training import ModelTraining



if __name__ =="__main__":
    data_ingestion = DataIngestion()
    train_df,test_df = data_ingestion.initiate_data_ingestion()
    data_transformation = DataTransformation()
    obj = data_transformation.get_preprocessor_obj()
    train_data,test_data,_ = data_transformation.initiate_data_transformation(train_df=train_df,test_df=test_df)
    model_training = ModelTraining()
    best_score,best_model = model_training.initiate_model_training(train_data,test_data)
    print(best_score)
    print(best_model)
    print(pyjokes.get_joke())



