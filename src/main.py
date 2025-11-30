import sys
from os_manipulations import generate_pages_recursive, remove_dir, create_dir, copy_dir_to_target


def main(basepath: str = "/"):
    remove_dir("docs")
    create_dir("docs")
    copy_dir_to_target("static", "docs")
    generate_pages_recursive("content", "docs", "template.html", basepath)

if __name__ == "__main__":
    main(sys.argv[0])

