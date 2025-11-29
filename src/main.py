from entities.textnode import TextNode, TextType


def main():
    node = TextNode("test text", TextType.PLAIN, "https://google.com")
    print(node)


if __name__ == "__main__":
    main()

