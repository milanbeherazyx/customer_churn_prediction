import os
import sys
from typing import Generator, List, Tuple

from dataclasses import dataclass
import numpy as np
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import recall_score
from src.churn.constants import *

from src.churn.exception import CustomException
from src.churn.logger import logging

from src.churn.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'Naive Bayes' : GaussianNB(),
            }
            params = {
                'Naive Bayes': {
                   'priors': [None],
                   'var_smoothing': [1e-07],
                },

            }

            model_report: dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                                                 models=models, param=params)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.5:
                error_message = "No best model found"
                error_detail = f"The best model score ({best_model_score}) is below the threshold (0.5)."
                logging.error(f"{error_message}: {error_detail}")
                raise CustomException(error_message, error_detail)

            logging.info("Best found model on both training and testing dataset")

            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)

            predicted = best_model.predict(X_test)
            return recall_score(y_test, predicted)
        except Exception as e:
            error_message = "An error occurred during model training"
            error_detail = str(e)
            logging.error(f"{error_message}: {error_detail}")
            raise CustomException(error_message, error_detail) from e
