from os_manipulations import remove_dir, create_dir, copy_dir_to_target


def main():
    remove_dir("public")
    create_dir("public")
    copy_dir_to_target("static", "public")


if __name__ == "__main__":
    main()

