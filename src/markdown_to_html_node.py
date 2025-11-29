from entities.htmlnode import HTMLNode
from entities.parentnode import ParentNode
from utils import BlockType, block_to_block_type, block_type_to_html_node, markdown_to_blocks, text_node_to_html_node, text_to_textnodes


def markdown_to_html_node(document: str) -> ParentNode:
    children: list[HTMLNode] = []
    for block in markdown_to_blocks(document):
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            paragraph_children: list[HTMLNode] = list(map(lambda it: text_node_to_html_node(it), text_to_textnodes(block)))
            children.append(ParentNode("p", paragraph_children))
        else:
            block = block.replace("\n", "")
            children.append(block_type_to_html_node(block, block_type))
    return ParentNode("div", children)

