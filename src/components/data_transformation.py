import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.exception import CustomException
from src.logger import logger
from src.utils import save_object

@dataclass
class DataFormationConfig:
    preprocessor_ob_file_path = os.path.join('artifacts\preprocesssor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataFormationConfig()

    def data_transformaer_ob(self):
        try:

            scaler = StandardScaler()
            
            logger.info('Standard scaling initiated')

            return scaler
        
        except Exception as e:
            raise logger.info(CustomException(e,sys))
             

    def intitiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logger.info('Read train and Test data is completed')

            logger.info('Obtaining preprocessing object')

            preprocessing_obj=self.data_transformaer_ob()

            target_column = 'Class'
            columns_list = ['Amount','Time']

            input_feature_train = train_df.drop(columns=[target_column], axis=1)
            target_feature_train = train_df[target_column]

            input_feature_test = test_df.drop([target_column], axis=1)
            target_feature_test = test_df[target_column]

            logger.info('Applying preprocessing object on training and testing dataframe')

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test)]

            logger.info('Saved preprocessing object')

            save_object(
                file_path = self.data_transformation_config.preprocessor_ob_file_path,
                obj = preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path
            )

        except Exception as e:
            raise logger.info(CustomException(e, sys))