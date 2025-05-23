import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(tag="h1", value="This is an html node", props=test_props)
        expected_result =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)
