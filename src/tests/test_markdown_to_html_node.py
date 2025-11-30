import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_with_empty_document(self):
        try:
            markdown_to_html_node("")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)

    def test_with_different_blocks(self):
        md = """
# Title

## Subtitle

This is just a paragraph. Bla bla bla.
Quick red fox jumped over lazy dog.
        """
        res = markdown_to_html_node(md)
        expected = "<div><h1>Title</h1><h2>Subtitle</h2><p>This is just a paragraph. Bla bla bla. Quick red fox jumped over lazy dog.</p></div>"
        self.assertEqual(expected, res.to_html())

    def test_multiple_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        res = markdown_to_html_node(md)
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(expected, res.to_html())

    def test_with_paragraph_with_code(self):
        md = """
Here is some TS code: `type SomeType = Record<string, Record<string, number[]>>`
        """
        res = markdown_to_html_node(md)
        expected = "<div><p>Here is some TS code: <code>type SomeType = Record<string, Record<string, number[]>></code></p></div>"
        self.assertEqual(expected, res.to_html())

    def test_with_code_block(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        res = markdown_to_html_node(md)
        expected = """<div><pre><code>This is text that _should_ remain
the **same** even with inline stuff</code></pre></div>"""
        self.assertEqual(expected, res.to_html())

    def test_with_unordered_lists(self):
        md = """
# Title

Things you had to do:

- succeed in math
- become a quant
- forget about everything
        """
        res = markdown_to_html_node(md)
        expected = "<div><h1>Title</h1><p>Things you had to do:</p><ul><li>succeed in math</li><li>become a quant</li><li>forget about everything</li></ul></div>"
        self.assertEqual(expected, res.to_html())

    def test_with_ordered_list(self):
        md = """
1. Don't cry!
2. Don't run!
3. Stay calm!
        """
        res = markdown_to_html_node(md)
        expected = "<div><ol><li>Don't cry!</li><li>Don't run!</li><li>Stay calm!</li></ol></div>"
        self.assertEqual(expected, res.to_html())

