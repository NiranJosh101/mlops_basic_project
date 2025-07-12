from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evalution import ModelEvaluation
from src.datascience import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass


    def initiate_model_eval(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlflow()