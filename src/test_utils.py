import unittest
from utils import text_node_to_html_node
from textnode import TextNode, TextType


mock_img_url = "http://localhost:3000"
class TestUtils(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()

