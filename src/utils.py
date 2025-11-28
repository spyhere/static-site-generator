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

