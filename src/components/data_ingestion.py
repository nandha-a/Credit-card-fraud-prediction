import os
import sys
from src.exception import CustomException
from src.logger import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataFormationConfig


@dataclass
class DataOIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__ (self):
        self.ingestion_config = DataOIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info('Entered data ingestion component')
        try:
            df = pd.read_csv('Data\creditcard.csv')
            df = df.dropna()
            q1 = df['Amount'].quantile(0.25)
            q3 = df['Amount'].quantile(0.75)
            iqr = q3 - q1
            high = q3 + (1.5*iqr)
            low = q1 - (1.5*iqr)
            df = df[(df['Amount']>low) & (df['Amount']<high)]

            logger.info('Dataset readed and DataFrame created')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logger.info('Train test split initiated')
            train_set, test_set = train_test_split(df,test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logger.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise logger.info(CustomException(e, sys))
        
        

if __name__ == '__main__':
    obj=DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.intitiate_data_transformation(train_data, test_data)
