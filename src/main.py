import sys
from os_manipulations import generate_pages_recursive, remove_dir, create_dir, copy_dir_to_target


def main(basepath: str):
    target_dir = "public" if basepath == "/" else "docs"
    remove_dir(target_dir)
    create_dir(target_dir)
    copy_dir_to_target("static", target_dir)
    generate_pages_recursive("content", target_dir, "template.html", basepath)

if __name__ == "__main__":
    basepath = "/"
    if 1 in sys.argv:
        basepath = sys.argv[1]
    main(basepath)

