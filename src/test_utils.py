import unittest
from utils import extract_markdown_images, split_nodes_delimiter, text_node_to_html_node
from textnode import TextNode, TextType


mock_img_url = "http://localhost:3000"
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("visit here", TextType.LINK, mock_img_url)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        assert html_node.props
        self.assertDictEqual(html_node.props, { "href": mock_img_url })

    def test_image(self):
        node = TextNode("default image", TextType.IMAGE, mock_img_url)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        assert html_node.props
        self.assertDictEqual(html_node.props, { "src": mock_img_url, "alt": "default image" })

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_empty_nodes(self):
        res = split_nodes_delimiter([], "`", TextType.TEXT)
        self.assertListEqual(res, [])

    def test_code_block(self):
        node_list = [TextNode("This is my `code snipet` example", TextType.TEXT)]
        res = split_nodes_delimiter(node_list, "`", TextType.CODE)
        expected = [
            TextNode("This is my ", TextType.TEXT),
            TextNode("code snipet", TextType.CODE),
            TextNode(" example", TextType.TEXT)
        ]
        self.assertListEqual(res, expected)

class TestExtractMarkdownImages(unittest.TestCase):
    def test_image_extraction(self):
        res = extract_markdown_images(f"Here is the image of my ![some alt text]({mock_img_url}) avatar")
        self.assertListEqual([("some alt text", mock_img_url)], res)

    def test_multiple_images_extraction(self):
        res = extract_markdown_images(f"1st image: ![first]({mock_img_url}) and 2nd image: ![second]({mock_img_url})")
        self.assertListEqual([("first", mock_img_url), ("second", mock_img_url)], res)

if __name__ == "__main__":
    unittest.main()

