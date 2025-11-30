import sys
import re
import os
import shutil
from markdown_to_html_node import markdown_to_html_node
from utils import extract_title, logging


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

@logging("Read $")
def read_file(path: str):
    try:
        content = None
        with open(path, "r") as f:
            content = f.read()
            return content
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

@logging("Wrote at $")
def write_file(path: str, content: str):
    dir_path = "/".join(path.split("/")[:-1]) + "/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    try:
        with open(path, "w") as f:
            f.write(content)
    except Exception as e:
        print(f"Error: {e}")

@logging("Generated page from $ to $ using $")
def generate_page(from_path: str, dest_path: str, template_path:str, basepath: str):
    from_path_content = read_file(from_path)
    template_path_content = read_file(template_path)

    html_content = markdown_to_html_node(from_path_content).to_html()
    html_title = extract_title(from_path_content) 
    new_content = template_path_content.replace("{{ Title }}", html_title).replace("{{ Content }}", html_content)
    new_content = new_content.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    write_file(dest_path, new_content)

def generate_pages_recursive(dir_path_content: str, dir_path_dest: str, template_path: str, basepath: str):
    for it in os.listdir(dir_path_content):
        curr_path_content = os.path.join(dir_path_content, it)
        curr_path_dest = os.path.join(dir_path_dest, it)
        if os.path.isfile(curr_path_content):
            generate_page(curr_path_content, re.sub(r"\.\w+$", ".html", curr_path_dest), template_path, basepath)
        else:
            generate_pages_recursive(curr_path_content, curr_path_dest, template_path, basepath)

