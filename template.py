import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# project_name = "cnnClassifier"

list_of_files = [
    # ".github/workflows/.gitkeep",       #will create main.yml file here that will do CI/CD but you can't create an empty folder so keeping this file as temp
    # f"src/{project_name}/__init__.py",  #constructor file to host this folder as a package
    # f"src/{project_name}/components/__init__.py",
    # f"src/{project_name}/utils/__init__.py",
    # f"src/{project_name}/config/__init__.py",
    # f"src/{project_name}/config/configuration.py",
    # f"src/{project_name}/pipeline/__init__.py",
    # f"src/{project_name}/entity/__init__.py",
    # f"src/{project_name}/constants/__init__.py",
    # "config/config.yaml",
    # "dvc.yaml",
    # "params.yaml",
    # "requirements.txt",
    # "setup.py",
    # "research/trials.ipynb",
    # "templates/index.html",

    "Xray/__init__.py",
    "Xray/cloud_storage/__init__.py",
    "Xray/cloud_storage/s3_operation.py",
    "Xray/components/__init__.py",
    "Xray/components/data_ingestion.py",
    "Xray/components/data_transformation.py",
    "Xray/components/data_transformation.py",
    "Xray/components/model_training.py",
    "Xray/components/model_evaluation.py",
    "Xray/components/model_pusher.py",          #push model in realtime to s3 bucket
    "Xray/entity/__init__.py",                  #for configuration
    "Xray/entity/config_entity.py",
    "Xray/entity/artifact_entity.py",
    "Xray/pipeline/__init__.py",
    "Xray/pipeline/training_pipeline.py",
    "logger.py",
    "exception.py",
    "requirements.txt",
    "setup.py",
    ".github/workflows/main.yaml",              #to write main configuration
    ".github/workflows/ci.yaml",
    "test/unittest/__init__.py",
    "test/integrationtest/__init__.py",
    "bentofile.yaml"

]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
