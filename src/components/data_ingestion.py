import os
import sys
from src.exceptional import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')
        try:
            # Read dataset from the correct path
            data_path = os.path.join('notebook', 'data', 'stud.csv')
            
            # ACTUALLY READ THE CSV FILE
            df = pd.read_csv(data_path)
            
            # Now log after reading
            logging.info('Successfully read the dataset as dataframe')
            logging.info(f'Dataset shape: {df.shape}')
            logging.info(f'Dataset columns: {list(df.columns)}')

            # Create artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            logging.info('Created artifacts directory')

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f'Saved raw data to {self.ingestion_config.raw_data_path}')

            # Train test split
            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info(f'Saved train data to {self.ingestion_config.train_data_path}')
            logging.info(f'Train set shape: {train_set.shape}')

            # Save test data
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f'Saved test data to {self.ingestion_config.test_data_path}')
            logging.info(f'Test set shape: {test_set.shape}')

            logging.info('Ingestion of the data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.error(f'Error occurred in data ingestion: {str(e)}')
            raise CustomException(e, sys)

if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
    print('\n' + '='*60)
    print('DATA INGESTION COMPLETED SUCCESSFULLY!')
    print('='*60)
    print(f' Train data saved at: {train_data}')
    print(f' Test data saved at: {test_data}')
    print('='*60 + '\n')
