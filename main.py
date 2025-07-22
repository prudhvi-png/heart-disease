from exception import CustomException
from src.components.data_ingestion import DataIngestion
import pyjokes
from src.components.data_transformation import DataTransformation



if __name__ =="__main__":
    data_ingestion = DataIngestion()
    train_df,test_df = data_ingestion.initiate_data_ingestion()
    data_transformation = DataTransformation()
    obj = data_transformation.get_preprocessor_obj()
    print(obj)
    print(pyjokes.get_joke())



