import unittest
from leafnode import LeafNode


class TextLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click!", { "href": "http://localhost:3000" })
        self.assertEqual(node.to_html(), '<a href="http://localhost:3000">Click!</a>')

    def test_leaf_no_value_err(self):
        try:
            node = LeafNode("p", "")
            node.to_html()
        except ValueError as e:
            self.assertIsInstance(e, ValueError)

    def test_leaf_no_tag(self):
        node = LeafNode("", "raw value without tag")
        self.assertEqual(node.to_html(), "raw value without tag")
        

