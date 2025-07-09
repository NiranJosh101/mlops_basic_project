import os
import sys
import logging


logging_str="[%(asctime)s: %(levelname)s: %(message)s]"

## create folder name
log_dir="log"

## create the folder
os.makedirs(log_dir,exist_ok=True)

## create logging path
log_filepath=os.path.join(log_dir,"logging.log")





logging.basicConfig(
    level=logging.INFO,
    format=logging_str,


    ## determines where the log messages go
    handlers=[
        logging.FileHandler(log_filepath),

        ## print logs in console
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("datascienceproject")