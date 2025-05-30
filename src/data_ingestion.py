import pandas as pd
from sklearn.model_selection import train_test_split
import logging
import os

# Create the logs directory
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

# log configurations
logger = logging.getLogger("Data Ingestion")
logger.setLevel('DEBUG')

# Create a file handler
log_file_path = os.path.join(logs_dir, "data_ingestion.log")
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


# Create a function that load data from datafiles
def load_data(file_path):
    """
    Load data from a CSV file
    """
    try:
        data = pd.read_csv(file_path)
        logger.debug(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        raise e

# Create a function that preprocess the data
def preprocess_data(data):
    """
    Preprocess the data
    """
    try:
        # remove the duplicate rows
        data = data.drop_duplicates()
        logger.debug("Duplicate rows removed successfully")

        # remove the missing values
        data = data.dropna()
        logger.debug("Missing values removed successfully")
        
        return data  # Return the processed data
    except Exception as e:
        logger.error(f"Error preprocess the data: {e}")
        raise  # Re-raise the exception to handle it in the main function

# Create a functio to save data into directory
def save_data(train_data: pd.DataFrame,test_data: pd.DataFrame,data_path: str):
    """Save the test and train datasets

    """
    try:
        clean_data_path = os.path.join(data_path,'clean_data')
        os.makedirs(clean_data_path, exist_ok=True)
        train_data.to_csv(os.path.join(clean_data_path, "train.csv"), index=False)
        test_data.to_csv(os.path.join(clean_data_path, "test.csv"), index=False)
        logger.debug("Train and Test saved to %s",clean_data_path)
    except Exception as e:
        logger.error("Unexpected error Occurred while in saving the data: %s",e)
        raise

def main():
    try:
        test_size =0.2
        data_path = 'data\Raw\diabetes.csv'
        df = load_data(data_path)
        preprocessed_data = preprocess_data(df)
        train_data ,test_data = train_test_split(preprocessed_data,test_size=test_size,random_state=2)
        save_data(train_data,test_data,'./data')
    except Exception as e:
        logger.error("Failed to Complete the Data ingestion process: %s",e)
        raise

if __name__ == '__main__':
    main()
