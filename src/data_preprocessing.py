# Import libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import logging
import os

# Create the logs directory
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

# log configurations
logger = logging.getLogger("Data Preprocessing")
logger.setLevel('DEBUG')

# Create a file handler
log_file_path = os.path.join(logs_dir, "data_preprocessing.log")
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)






# Seprate the Categorical features from data 
def categorical_features(data:pd.DataFrame):
    try:
        categorical_features = [feature for feature in data.columns if data[feature].dtypes == 'O']

        return categorical_features
    except Exception as e:
        logger.error(f"Error Fetching the Categorical features from data  : {e}")
        raise e

# preprocessing the features in the data 

def preprocess_data(data: pd.DataFrame):
    """
    Preprocesses the DataFrame by encoding the target column, removing duplicates, and transforming the text column.
    """
    try:
        # Get categorical features by calling the function
        cat_features = categorical_features(data)
        
        # encode the categorical data into numerical 
        label_encoder = LabelEncoder()
        for feature in cat_features:
            data[feature] = label_encoder.fit_transform(data[feature])
        
        logger.debug('Successfully Encoded the Categorical features into Numerical')
        
        # Remove duplicate rows
        data = data.drop_duplicates(keep='first')
        logger.debug('Duplicates removed')

        return data

    except Exception as e:
        logger.error(f"Error during data preprocessing, Encoding, Remove duplicate: {e}")
        raise e



def main():
    try:
        # Fetch the data from data/clean_data
        train_data = pd.read_csv('./data/clean_data/train.csv')
        test_data = pd.read_csv('./data/clean_data/test.csv')
        logger.debug('Data loaded properly')

        # Transform the data
        train_processed_data = preprocess_data(train_data)
        test_processed_data = preprocess_data(test_data)

        # Store the data inside data/processed
        data_path = os.path.join("./data", "interim")
        os.makedirs(data_path, exist_ok=True)
        
        train_processed_data.to_csv(os.path.join(data_path, "train_processed.csv"), index=False)
        test_processed_data.to_csv(os.path.join(data_path, "test_processed.csv"), index=False)
        
        logger.debug('Processed data saved to %s', data_path)
    except FileNotFoundError as e:
        logger.error('File not found: %s', e)
    except pd.errors.EmptyDataError as e:
        logger.error('No data: %s', e)
    except Exception as e:
        logger.error('Failed to complete the data transformation process: %s', e)
        raise

if __name__ == "__main__":
    main()