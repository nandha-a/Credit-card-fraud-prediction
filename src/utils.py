import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from src.exception import CustomException
from src.logger import logger

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise logger.info(CustomException(e,sys))


def evaluate_models(x_train,y_train,x_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(x_train, y_train)

            y_pred = model.predict(x_test)

            accuracyScore = accuracy_score(y_test, y_pred)

            classificationReport = classification_report(y_test, y_pred)

            confusionMatrix = confusion_matrix(y_test, y_pred)

            report[list(models.keys())[i]] = accuracyScore

        x = max(report.values())
        best_model = list(report.keys())[list(report.values()).index(x)]

        return best_model

    except Exception as e:
        raise logger.info(CustomException(e,sys))