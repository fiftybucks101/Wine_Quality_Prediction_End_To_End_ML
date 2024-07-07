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

    def data_train_test_split(self):

        df = pd.read_csv(self.config.data_path)
        df = df.iloc[:,0:-1]
        train, test = train_test_split(df,test_size=0.25)

        columns_name = df.columns
        
        train_df = pd.DataFrame(data=train,columns=columns_name)
        test_df = pd.DataFrame(data=test,columns=columns_name)

        train_path = os.path.join(self.config.root_dir,"train.csv")
        test_path = os.path.join(self.config.root_dir,"test.csv")

        train.to_csv(train_path, index=False)
        test.to_csv(test_path, index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)