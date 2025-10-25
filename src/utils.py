import sys
import os
import pandas as pd
import numpy as np
import dill #Used to serialize (save) Python objects to files.
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path , exist_ok=True)

        with open(file_path , "wb") as file_obj:
            dill.dump(obj, file_obj) #Serializes (converts) the Python object into bytes and writes it to the file
            #serialization: Converts Python objects (which exist in memory) into a format that can be stored on disk

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train , y_train , X_test , y_test , models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para , cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            # model.fit(X_train , y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train , y_train_pred)

            test_model_score = r2_score(y_test , y_test_pred)

            report[list(models.keys())[i]] = test_model_score #This will form a dictionary with keys as the model name and r2 score as value
        
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
    

