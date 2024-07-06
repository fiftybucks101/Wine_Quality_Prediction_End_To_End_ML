from wine_pred.entity.config_entity import DataTransformationConfig
from wine_pred.config.configuration import ConfigurationManager
from wine_pred.logging.logger import logger
from wine_pred.components.data_transformation import DataTransformation

STAGE_NAME = "Data Ingestion Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.data_transformation()
            data_transformation.data_train_test_split()
        except Exception as e:
            logger.info(e)
            raise e