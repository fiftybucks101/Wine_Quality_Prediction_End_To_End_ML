from wine_pred.entity.config_entity import DataTransformationConfig
from wine_pred.config.configuration import ConfigurationManager
from wine_pred.logging.logger import logger
from wine_pred.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open("artifacts\data_validation\status.txt", 'r') as f:
                status = f.read().split(" ")[-1]
            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformations = DataTransformation(data_transformation_config)
                data_transformations.data_train_test_split()
            else:
                raise Exception('Data schema is not valid.')
        except Exception as e:
            logger.info(e)
            raise e