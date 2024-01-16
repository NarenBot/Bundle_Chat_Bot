import os
import sys
import pandas as pd
import numpy as np
import dill
import yaml

from src.exception import CustomException
from src.logger import logging
import warnings

warnings.filterwarnings("ignore")


def save_object(obj, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            dill.dump(obj=obj, file=file)
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file:
            return dill.load(file=file)
    except Exception as e:
        raise CustomException(e, sys)


def load_yaml(file_path):
    try:
        with open(file_path) as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise CustomException(e, sys)
