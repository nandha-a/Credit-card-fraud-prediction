import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException
from src.logger import logger

def save_object(file_path, train, test):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(train, file_obj)
            dill.dump(test,file_obj)

    except Exception as e:
        raise logger.info(CustomException(e,sys))
    