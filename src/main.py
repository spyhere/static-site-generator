from os_manipulations import generate_pages_recursive, remove_dir, create_dir, copy_dir_to_target


def main():
    remove_dir("public")
    create_dir("public")
    copy_dir_to_target("static", "public")
    generate_pages_recursive("content", "public", "template.html")

if __name__ == "__main__":
    main()

