from os_manipulations import generate_page, remove_dir, create_dir, copy_dir_to_target


def main():
    remove_dir("public")
    create_dir("public")
    copy_dir_to_target("static", "public")

    generate_page("content/index.md", "public/index.html", "template.html")

if __name__ == "__main__":
    main()

