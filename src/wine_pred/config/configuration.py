from wine_pred.constants import *
from wine_pred.utils.common import read_yaml, create_directories 
from wine_pred.entity.config_entity import DataValidationConfig
from wine_pred.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
from wine_pred.constants import *

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            unziped_data_dir=config.unziped_data_dir,
            all_schema=schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = self.config.model_trainer
        params = self.params.Random_Forest_Regressor
        schema =  self.schema.TARGET_COLUMN

        print("Model Trainer Config:", config)  # Debugging print
        print("Params:", params)  # Debugging print
        print("Schema:", schema)  # Debugging print

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            TARGET_COLUMN=schema.name,
            max_depth=params.max_depth,
            max_features=params.max_features,
            min_samples_split=params.min_samples_split,
            n_estimators=params.n_estimators)
        
        return model_trainer_config
    




        


        