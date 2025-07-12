import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlflow.models.signature import infer_signature
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories,save_json #save json added to save metrics



os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/NiranJosh101/mlops_basic_project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="NiranJosh101"
os.environ["MLFLOW_TRACKING_PASSWORD"]="2b6e0a1d2f111da7d122794576fe6e2cd171cd65"




class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config=config

    
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mse = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mse, r2

    

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[self.config.target_column]

        
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_experiment("ElasticNet_Model_Tracking")

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            rmse, mae, r2 = self.eval_metrics(test_y, predicted_qualities)

            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Save locally
            model_path = os.path.join(self.config.root_dir, "model.joblib")
            joblib.dump(model, model_path)

            # Log model manually as artifact
            mlflow.log_artifact(local_path=model_path, artifact_path="model")