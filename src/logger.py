import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #This will be the file name
logs_folder = os.path.join(os.getcwd(),"logs") #This will be our file path 
os.makedirs(logs_folder , exist_ok=True) #exist_ok will continue make the folder even it still exists without giving any error

LOG_FILE_PATH = os.path.join(logs_folder,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")