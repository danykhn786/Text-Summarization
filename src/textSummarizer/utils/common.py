import os 
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations 
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file  and returns 

    Args:
    path_to_yaml (Path): path to the yaml file

    Raises:
    ValueError: if yaml is empty 
    e: empty file 

    Returns:
    ConfigBox: config box type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list , verbose=True):
    """
    Create a list of directories

    Args:
    path_to_directories (list): list of path of directories 
    ignore_log(bool,optional): ignore if multiple directories is to be created. Default is False.
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully")


@ensure_annotations
def get_size(path:Path) -> str:
    """
    Gets Size in KB

    Args: 
    path (Path): path to the file

    Returns:
    str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)

    return f"~{size_in_kb} KB"

