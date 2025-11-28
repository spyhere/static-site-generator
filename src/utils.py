import re
from constants import MD_IMAGE_ALL_REGEXP, MD_IMAGE_GROUPED_REGEXP, MD_LINK_ALL_REGEXP, MD_LINK_GROUPED_REGEXP
from leafnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(node: TextNode) -> LeafNode:
    match node.text_type:
        case TextType.TEXT:
            return LeafNode(value=node.text)
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.LINK:
            return LeafNode("a", node.text, { "href": node.url })
        case TextType.IMAGE:
            return LeafNode("img", props={ "src": node.url, "alt": node.text })
        case _:
            return LeafNode(value=node.text)

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    res = []
    for node in old_nodes:
        text, curr_text_type = node.text, node.text_type
        for idx, it in enumerate(text.split(delimiter)):
            if idx % 2 == 0:
                res.append(TextNode(it, curr_text_type))
            else:
                res.append(TextNode(it, text_type))
    return res

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(MD_IMAGE_GROUPED_REGEXP, text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(MD_LINK_GROUPED_REGEXP, text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    res: list[TextNode] = []
    for node in old_nodes:
        text, curr_text_type = node.text, node.text_type
        extracted_images = extract_markdown_images(text)
        for idx, it in enumerate(re.split(MD_IMAGE_ALL_REGEXP, text)):
            res.append(TextNode(it, curr_text_type))
            if idx < len(extracted_images):
                alt, url = extracted_images[idx]
                res.append(TextNode(alt, TextType.IMAGE, url))
    return res


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    res: list[TextNode] = []
    for node in old_nodes:
        text, curr_text_type = node.text, node.text_type
        extracted_links = extract_markdown_links(text)
        for idx, it in enumerate(re.split(MD_LINK_ALL_REGEXP, text)):
            res.append(TextNode(it, curr_text_type))
            if idx < len(extracted_links):
                link_text, url = extracted_links[idx]
                res.append(TextNode(link_text, TextType.LINK, url))
    return res

