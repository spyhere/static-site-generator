import unittest
from entities.leafnode import LeafNode
from entities.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_a(self):
        child_node = LeafNode("span", "leaf child")
        parent_node = ParentNode("a", [child_node], { "href": "http://localhost:3000" })
        self.assertEqual(parent_node.to_html(), '<a href="http://localhost:3000"><span>leaf child</span></a>')

if __name__ == "__main__":
    unittest.main()

