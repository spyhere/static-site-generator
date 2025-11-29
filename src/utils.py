import re
from constants import MD_IMAGE_ALL_REGEXP, MD_IMAGE_GROUPED_REGEXP, MD_LINK_ALL_REGEXP, MD_LINK_GROUPED_REGEXP
from enums import BlockType
from entities.htmlnode import HTMLNode
from entities.leafnode import LeafNode
from entities.parentnode import ParentNode
from entities.textnode import TextNode, TextType


def logging(msg: str):
    def inside(func):
        def wrapper(*args, **kwargs):
            msg_parsed = ""
            msg_splitted = msg.split("$")
            for idx, it in enumerate(msg_splitted):
                msg_parsed += it
                if idx < len(msg_splitted) - 1:
                    msg_parsed += args[idx]
            res = func(*args, **kwargs)
            print(msg_parsed)
            return res
        return wrapper
    return inside

def block_type_to_html_node(document: str, type: BlockType) -> HTMLNode:
    match type:
        case BlockType.HEADING:
            hash_amounts = document.count("#")
            return LeafNode(f"h{hash_amounts}", document.replace("#", "").strip())
        case BlockType.CODE:
            return ParentNode("pre", [LeafNode("code", document.replace("```", ""))])
        case BlockType.QUOTE:
            return LeafNode("quote", document)
        case BlockType.UNORDERED_LIST:
            children: list[HTMLNode] = []
            for it in document.split("-"):
                stripped = it.strip()
                if not stripped:
                    continue
                local_children: list[HTMLNode] = list(map(lambda it: text_node_to_html_node(it), text_to_textnodes(stripped)))
                children.append(ParentNode("li", local_children))
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            children: list[HTMLNode] = []
            for it in re.split(r"\d\.", document):
                stripped = it.strip()
                if not stripped:
                    continue
                local_children = list(map(lambda it: text_node_to_html_node(it), text_to_textnodes(stripped)))
                children.append(ParentNode("li", local_children))
            return ParentNode("ol", children)
        case BlockType.PARAGRAPH:
            return LeafNode(value=document)

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
        text, orig_text_type, orig_url = node.text, node.text_type, node.url
        extracted_images = extract_markdown_images(text)
        for idx, it in enumerate(re.split(MD_IMAGE_ALL_REGEXP, text)):
            if it: # Do not add empty string that can appear at the end of list
                res.append(TextNode(it, orig_text_type, orig_url))
            if (idx < len(extracted_images)):
                alt, url = extracted_images[idx]
                res.append(TextNode(alt, TextType.IMAGE, url))
    return res


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    res: list[TextNode] = []
    for node in old_nodes:
        text, curr_text_type, curr_url = node.text, node.text_type, node.url
        extracted_links = extract_markdown_links(text)
        for idx, it in enumerate(re.split(MD_LINK_ALL_REGEXP, text)):
            if it: # Do not add empty string that can appear at the end of list
                res.append(TextNode(it, curr_text_type, curr_url))
            if idx < len(extracted_links):
                link_text, url = extracted_links[idx]
                res.append(TextNode(link_text, TextType.LINK, url))
    return res

def text_to_textnodes(document: str) -> list[TextNode]:
    res = split_nodes_delimiter([TextNode(document, TextType.TEXT)], "**", TextType.BOLD)
    res = split_nodes_delimiter(res, "_", TextType.ITALIC)
    res = split_nodes_delimiter(res, "`", TextType.CODE)
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    return res

def markdown_to_blocks(document: str) -> list[str]:
    res: list[str] = []
    for it in document.split("\n\n"):
        if it:
            res.append(it.strip())
    return res

def block_to_block_type(document: str) -> BlockType:
    stripped = document.strip()
    if stripped.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if stripped.startswith("```") and stripped.endswith("```"):
        return BlockType.CODE
    splitted_multiline = stripped.split("\n")
    if len(splitted_multiline) > 0:
        if len(list(filter(lambda it: it.startswith(">"), splitted_multiline))) == len(splitted_multiline):
            return BlockType.QUOTE
        if len(list(filter(lambda it: it.startswith("-"), splitted_multiline))) == len(splitted_multiline):
            return BlockType.UNORDERED_LIST
        if len(list(filter(lambda  it: it[1].startswith(str(it[0] + 1)), enumerate(splitted_multiline)))) == len(splitted_multiline):
            return BlockType.ORDERED_LIST
        return BlockType.PARAGRAPH
    return BlockType.PARAGRAPH

