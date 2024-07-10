import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
from wine_pred.config.configuration import ConfigurationManager
from wine_pred.constants import *
from wine_pred.utils.common import read_yaml



# def get_model_path(config_filepath = CONFIG_FILE_PATH) -> Path:
#     config_yaml = read_yaml(config_filepath)
#     config = config_yaml.model_evaluation
#     return (config.model_path)

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_training/model.joblib'))

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction