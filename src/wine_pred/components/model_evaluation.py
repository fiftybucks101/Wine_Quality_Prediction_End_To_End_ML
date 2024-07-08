from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
from wine_pred.constants import *
import numpy as  np
from wine_pred.logging.logger import logger
from wine_pred.utils.common import load_bin, save_json
import joblib
import json
from wine_pred.entity.config_entity import ModelEvaluationConfig



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def metrics(self):

        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        target_column = self.config.name

        X_train = train_df.drop([target_column], axis=1)
        X_test = test_df.drop([target_column],axis=1)
        y_train = train_df[target_column]
        y_test = test_df[target_column]

        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        train_json = {
            'RMSE': np.sqrt(mean_squared_error(y_train,y_train_pred)),
            'MAE': mean_absolute_error(y_train,y_train_pred),
            'R2 Score': r2_score(y_train,y_train_pred)
        }

        test_json = {
            'RMSE': np.sqrt(mean_squared_error(y_test,y_test_pred)),
            'MAE': mean_absolute_error(y_test,y_test_pred),
            'R2 Score': r2_score(y_test,y_test_pred)
        }

        train_path = 'artifacts/model_evaluation/train_mertics.json'
        test_path = 'artifacts/model_evaluation/test_mertics.json'

        with open(train_path, 'w') as f:
            json.dump(train_json, f)

        with open(test_path, 'w') as f:
            json.dump(test_json, f)

        logger.info('Train & Test Metrics Json file saved sucessfully.')
       
        