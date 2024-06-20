from htmlnode import HTMLNode

import unittest

test_node1= HTMLNode("<a>", "test text 12", ["Some", "list", "of", "nodes"], {"A":"Dict", "Composed":"of", "different":"stuff"})
test_node2= HTMLNode("<a>")

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        html_propos = test_node2.props_to_html()
        print(html_propos)

if __name__ == "__main__":
    unittest.main()


print(test_node2)