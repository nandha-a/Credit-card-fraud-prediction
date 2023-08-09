import sys 
import  pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__ (self,
                  Time: int,
                  V1: float,
                  V2: float,
                  V3: float,
                  V4: float,
                  V5: float,
                  V6: float,
                  V7: float,
                  V8: float,
                  V9: float,
                  V10: float,
                  V11: float,
                  V12: float,
                  V13: float,
                  V14: float,
                  V15: float,
                  V16: float,
                  V17: float,
                  V18: float,
                  V19: float,
                  V20: float,
                  V21: float,
                  V22: float,
                  V23: float,
                  V24: float,
                  V25: float,
                  V26: float,
                  V27: float,
                  V28: float,
                  Amount: float):
        self.Time = Time
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
        self.V4 = V4
        self.V5 = V5
        self.V6 = V6
        self.V7 = V7
        self.V8 = V8
        self.V9 = V9
        self.V10 = V10
        self.V11 = V11
        self.V12 = V12
        self.V13 = V13
        self.V14 = V14
        self.V15 = V15
        self.V16 = V16
        self.V17 = V17
        self.V18 = V18
        self.V19 = V19
        self.V20 = V20
        self.V21 = V21
        self.V22 = V22
        self.V23 = V23
        self.V24 = V24
        self.V25 = V25
        self.V26 = V26
        self.V27 = V27
        self.V28 = V28
        self.Amount = Amount

    def get_data_as_frame(self):
        try:
            custom_input_data_dict = {
                'Time':[self.Time],
                'v1':[self.V1],
                    'v2':[self.V2],
                    'v3':[self.V3],
                    'v4':[self.V4],
                    'v5':[self.V5],
                    'v6':[self.V6],
                    'v7':[self.V7],
                    'v8':[self.V8],
                    'v9':[self.V9],
                    'v10':[self.V10],
                    'v11':[self.V11],
                    'v12':[self.V12],
                    'v13':[self.V13],
                    'v14':[self.V14],
                    'v15':[self.V15],
                    'v16':[self.V16],
                    'v17':[self.V17],
                    'v18':[self.V18],
                    'v19':[self.V19],
                    'v20':[self.V20],
                    'v21':[self.V21],
                    'v22':[self.V22],
                    'v23':[self.V23],
                    'v24':[self.V24],
                    'v25':[self.V25],
                    'v26':[self.V26],
                    'v27':[self.V27],
                    'v28':[self.V28],
                    'Amount':[self.Amount]
            }
        except:
            pass