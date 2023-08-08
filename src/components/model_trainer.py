import os
import sys
from dataclasses import dataclass
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from src.exception import CustomException
from src.logger import logger
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logger.info("Spliting training train and test input data")
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                'Logistic Regression' : LogisticRegression(),
                'Random Forest Classifier' : RandomForestClassifier()
            }

            logger.info('Model training initiated')

            model_report:dict=evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                train= x_train,
                test = x_test
            )

            return model_report

        except Exception as e:
            raise logger.info(CustomException(e,sys))
