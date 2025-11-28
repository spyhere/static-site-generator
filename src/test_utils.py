import unittest
from utils import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_node_to_html_node
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

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_link_extraction(self):
        res = extract_markdown_links(f"Here is my [link]({mock_img_url}) in the text")
        self.assertListEqual([("link", mock_img_url)], res)

    def test_multiple_links_extraction(self):
        res = extract_markdown_links(f"1st link: [first]({mock_img_url}), 2nd link: [second]({mock_img_url})")
        self.assertListEqual([("first", mock_img_url), ("second", mock_img_url)], res)

    def test_to_extract_only_links(self):
        res = extract_markdown_links(f"link: [link]({mock_img_url}), image: ![image]({mock_img_url})")
        self.assertListEqual([("link", mock_img_url)], res)

class TestSplitNodesImage(unittest.TestCase):
    def test_multiple_images_extraction(self):
        nodes = [TextNode(f"This is image ![image1]({mock_img_url}) and this is image ![image2]({mock_img_url}) together!", TextType.TEXT)]
        res = split_nodes_image(nodes)
        expected = [
            TextNode("This is image ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, mock_img_url),
            TextNode(" and this is image ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, mock_img_url),
            TextNode(" together!", TextType.TEXT)
        ]
        self.assertListEqual(expected, res)

    def test_no_images_extraction(self):
        nodes = [TextNode("There is no images here.", TextType.TEXT)]
        res = split_nodes_image(nodes)
        self.assertListEqual(nodes, res)

class TestSplitNodesLink(unittest.TestCase):
    def test_multiple_links_extraction(self):
        nodes = [TextNode(f"This is [link1]({mock_img_url}) and [link2]({mock_img_url}) to press.", TextType.TEXT)]
        res = split_nodes_link(nodes)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("link1", TextType.LINK, mock_img_url),
            TextNode(" and ", TextType.TEXT),
            TextNode("link2", TextType.LINK, mock_img_url),
            TextNode(" to press.", TextType.TEXT)
        ]
        self.assertListEqual(expected, res)

    def test_no_links_extraction(self):
        nodes = [TextNode("There is no links here.", TextType.TEXT)]
        res = split_nodes_link(nodes)
        self.assertListEqual(nodes, res)

if __name__ == "__main__":
    unittest.main()

