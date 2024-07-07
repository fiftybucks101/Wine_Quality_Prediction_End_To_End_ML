from wine_pred.logging.logger import logger
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import QuantileTransformer
from sklearn.ensemble import RandomForestRegressor
import joblib
from wine_pred.entity.config_entity import ModelTrainerConfig
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        self.log_columns = ['fixed acidity', 'volatile acidity','residual sugar', 'citric acid', 'chlorides', 'sulphates', 'free sulfur dioxide', 'total sulfur dioxide', 'alcohol']
        logger.info('Constructor Initialized')

    def Train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        logger.info('Train Dataset Read Done')
        preprocessor = ColumnTransformer(
            transformers=[
                ('quantile', QuantileTransformer(output_distribution='normal'), self.log_columns),
            ],
            remainder='passthrough' )
        
        
        X_train = train_data.drop([self.config.TARGET_COLUMN], axis=1)
        y_train = train_data[[self.config.TARGET_COLUMN]]

        pipeline = Pipeline(
        steps=[
            ('Preprocessor', preprocessor),
            ('Random Forest Reg', RandomForestRegressor(random_state=42,
                                                        max_depth=self.config.max_depth,
                                                        max_features=self.config.max_features,
                                                        min_samples_split=self.config.min_samples_split,
                                                        n_estimators=self.config.n_estimators))
        ] )

        pipeline.fit(X_train,y_train)
        logger.info('Object Training Done')

        model_path = os.path.join(self.config.root_dir,self.config.model_name)
        joblib.dump(pipeline, model_path)

        logger.info(f'Model Object saved at {model_path}')
        