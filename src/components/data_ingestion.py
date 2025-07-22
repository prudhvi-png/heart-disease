import pandas as pd  
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os
import sys 
from logger import logging
from exception import CustomException


@dataclass
class DataIngestionConfig:
    train_file_path = os.path.join("artifacts","train_data.csv")
    test_file_path = os.path.join("artifacts","test_data.csv")
    raw_file_path = os.path.join("artifacts","raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:

            df = pd.read_csv("notebooks\\heart.csv")

            os.makedirs(os.path.dirname(self.data_ingestion_config.test_file_path),exist_ok=True)

            logging.info("Data ingestion Started *** ")
            
            train_df,test_df = train_test_split(df,test_size=0.3,random_state=42)
            
            train_df.to_csv(self.data_ingestion_config.train_file_path,index=False,header=True)
            test_df.to_csv(self.data_ingestion_config.test_file_path,index=False,header=True)
            df.to_csv(self.data_ingestion_config.raw_file_path,index=False,header=True)

            logging.info("Data Ingestion completed !!!")

            return(
                self.data_ingestion_config.train_file_path,
                self.data_ingestion_config.test_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)

