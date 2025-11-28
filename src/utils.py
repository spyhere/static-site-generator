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
