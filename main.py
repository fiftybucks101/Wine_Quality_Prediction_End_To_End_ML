from wine_pred.config.configuration import ConfigurationManager
from wine_pred.logging.logger import logger
from wine_pred.components.data_ingestion import DataIngestion
from wine_pred.components.data_validation import DataValidation

STAGE_NAME = "Data Ingestion Stage"
try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(data_validation_config)
    data_validation.validate_all_columns()
except Exception as e:
    logger.exception(e)
    raise e