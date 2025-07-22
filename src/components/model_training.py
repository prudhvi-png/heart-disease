from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from logger import logging
from exception import CustomException
import os,sys
from dataclasses import dataclass
from sklearn.metrics import accuracy_score,recall_score
from utils import save_object,save_info

@dataclass
class ModelTrainingConfig:
    model_obj_path = os.path.join("models","model.pkl")
    outputs_file_path = os.path.join("outputs","outputs.txt")


class ModelTraining:
    def __init__(self)->None:
        self.model_training_config = ModelTrainingConfig()
    
    def evaluate_model(self,true,predicted):
        try:

            accu = accuracy_score(true,predicted)
            recall = recall_score(true,predicted)
            return accu,recall
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_model_training(self,train_df,test_df):
        try:

            x_train,y_train,x_test,y_test = (train_df[:,:-1],train_df[:,-1],test_df[:,:-1],test_df[:,-1])

            models = {
                "logistic_Regression" : LogisticRegression(),
                "Knn" : KNeighborsClassifier(),
                "RFC" : RandomForestClassifier(),
                "Ada" : AdaBoostClassifier(),
                "GradientBoost" : GradientBoostingClassifier(),
                "svc" : SVC(),
                "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss')}
            best_score = 0
            best_model = None

            for name,model in models.items():
                model.fit(x_train,y_train)

                y_test_pred = model.predict(x_test)
                accu,recall = self.evaluate_model(y_test,y_test_pred)
                if accu > best_score:
                    best_score = accu
                    best_model = model

            save_object(
                self.model_training_config.model_obj_path,
                obj=best_model
            )

            save_info(
                self.model_training_config.outputs_file_path,
                model=best_model,
                score=best_score
            )
            
            return (best_score*100,
                    best_model)

        
        except Exception as e:
            raise CustomException(e,sys)



