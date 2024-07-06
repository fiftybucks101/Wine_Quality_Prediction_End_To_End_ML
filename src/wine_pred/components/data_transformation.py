from wine_pred.logging.logger import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import QuantileTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from wine_pred.entity.config_entity import DataTransformationConfig
import os



class DataTransformation:
    def __init__ (self, config: DataTransformationConfig):
        self.config = config
        self.log_columns = ['fixed acidity', 'volatile acidity','residual sugar', 'citric acid', 'chlorides', 'sulphates', 'free sulfur dioxide', 'total sulfur dioxide', 'alcohol']

    def data_transformation(self):
        preprocessor = ColumnTransformer(
            transformers=[
            ('quantile', QuantileTransformer(output_distribution='normal'), self.log_columns),
            ],
        remainder='passthrough')

        df = pd.read_csv(self.config.data_path)
        df_transformed = preprocessor.fit_transform(df)
    
        # Convert the transformed array back to a DataFrame
        df_transformed = pd.DataFrame(df_transformed, columns=df.columns)
    
        return df_transformed
        
    def data_train_test_split(self):

        train, test = train_test_split(self.data_transformation(),test_size=0.25)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)