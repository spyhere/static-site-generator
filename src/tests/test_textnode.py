import unittest
from entities.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def should_not_eq(self):
        node = TextNode("Node 1", TextType.PLAIN)
        node2 = TextNode("Node 2", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def should_accept_url(self):
        url = "http://localhost:3000"
        node_without_url = TextNode("Node without url", TextType.PLAIN)
        node_with_url = TextNode("Node with url", TextType.PLAIN, url)
        self.assertNotIn(url, str(node_without_url))
        self.assertIn(url, str(node_with_url))


if __name__ == "__main__":
    unittest.main()

