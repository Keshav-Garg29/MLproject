import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

@dataclass #@dataclass turns the class into a simple data holder with minimal code. @dataclass, Python automatically creates the __init__()
class DataIngestionConfig: #This class stores all the file paths needed for data ingestion
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #This will create the object of above class and store all the three path variable in this particular variable

    def Initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")
        #   This makedirs is responsible of creating the artifacts folder and we can use any path in place of .train_data_path as this os.path.dirname will consider only folder name that is artifacts not artifacts/train.csv
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #exist_ok=True: If the directory already exists, don't raise an error (just skip creating it) 
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set , test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys) 
        
if __name__ == "__main__":
    obj= DataIngestion()
    train_data , test_data = obj.Initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr , test_arr , _ = data_transformation.initiate_data_transformation(train_data , test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr , test_arr))