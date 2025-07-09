import os
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # read the current data and store its columns
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_dtype = list(map(str, data.dtypes))

            # get the defined schema in the schema.yaml file
            all_schema = self.config.all_schema.keys()
            all_dtypes = self.config.all_schema.values()

            # Initial assumption
            validation_status = True


            # Check dtypes
            if all_dtype != list(all_dtypes):  # ensure both are lists
                validation_status = False
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write(f"Validation status: {validation_status}\n")

            # Check schema
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}\n")

            # Final status write
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Final validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
