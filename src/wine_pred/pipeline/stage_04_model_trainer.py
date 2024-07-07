from wine_pred.entity.config_entity import DataTransformationConfig
from wine_pred.config.configuration import ConfigurationManager
from wine_pred.logging.logger import logger
from wine_pred.components.model_trainer import ModelTrainer

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.Train()
            pass
        except Exception as e:
            logger.info('Problem During Model Training Pipeline')
            raise e
