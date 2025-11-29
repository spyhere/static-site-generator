import sys
import os
import shutil
from utils import logging


@logging("Successfuly deleted $/ directory")
def remove_dir(dir_path: str):
    try:
        res = shutil.rmtree(dir_path)
        if res is not None:
            print(f"Warning: {res}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

@logging("Successfuly created $/ directory")
def create_dir(dir_path: str):
    try:
        os.mkdir(dir_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

@logging("Successfuly copied $/ to $/")
def copy_dir_to_target(origin_path: str, target_path: str):
    for it in os.listdir(origin_path):
        curr_path = os.path.join(origin_path, it)
        if os.path.isfile(curr_path):
            shutil.copy(curr_path, target_path)
        else:
            new_target_path = os.path.join(target_path, it)
            os.mkdir(new_target_path)
            copy_dir_to_target(curr_path, new_target_path)

