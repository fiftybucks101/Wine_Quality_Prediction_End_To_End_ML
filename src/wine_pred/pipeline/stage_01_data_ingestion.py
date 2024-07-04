from wine_pred.entity.config_entity import DataIngestionConfig
from wine_pred.config.configuration import ConfigurationManager
from wine_pred.logging.logger import logger
from wine_pred.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

# if __name__ == '__main__':
#     try:
#         logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logger.exception(e)
#         raise e