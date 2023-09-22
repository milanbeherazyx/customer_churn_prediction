import os
import sys
import pandas as pd
from src.churn.exception import CustomException
from src.churn.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            return model.predict(data_scaled)
        except Exception as e:
            raise CustomException(e, sys) from e


class CustomData:
    def __init__(self,
                 Age: int,
                 Gender: object,
                 Location: object,
                 Subscription_Length_Months: int,
                 Monthly_Bill: float,
                 Total_Usage_GB: int):

        self.Age = Age
        self.Gender = Gender
        self.Location = Location
        self.Subscription_Length_Months = Subscription_Length_Months
        self.Monthly_Bill = Monthly_Bill
        self.Total_Usage_GB = Total_Usage_GB


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Location": [self.Location],
                "Subscription_Length_Months": [self.Subscription_Length_Months],
                "Monthly_Bill": [self.Monthly_Bill],
                "Total_Usage_GB": [self.Total_Usage_GB],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys) from e
