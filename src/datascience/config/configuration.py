from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import (DataIngestionCofig, DataValidationConfig, DataTransformationConfig, ModelTrainingConfig, ModelEvaluationConfig)


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH, schema_filepath = SCHEMA_FILE_PATH):
        
        # read the yaml file stated below
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        # read then extract the dir name from the config file just read
        # this allows us creat the artifacts/ folder (where outputs will be stored)
        create_directories([self.config.artifacts_root])

    def get_data_ingetstion_config(self) -> DataIngestionCofig:

        # get all the config settings in the data_ingestion file in the artifacts folder
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        # return a configured object
        data_ingestion_config=DataIngestionCofig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:

        # get all the config settings in the data_ingestion file in the artifacts folder
        config=self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        # return a configured object
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema,
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:

    
        config=self.config.data_transformation

        create_directories([config.root_dir])

        # return a configured object
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    


    def get_model_trainer_cofig(self) -> ModelTrainingConfig:
        config=self.config.model_training
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN

        # create saved moder dir
        create_directories([config.root_dir])


        model_trainer_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )

        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config=self.config.model_evaluation
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN


        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
            target_column=schema.name,
            mlflow_uri="https://dagshub.com/NiranJosh101/mlops_basic_project.mlflow",
            mlflow_uri_local="http://127.0.0.1:5000"
        )

        return model_evaluation_config
