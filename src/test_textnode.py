import unittest

from textnode import TextNode

test_nodes =[
    TextNode("couleur", "italic"),
    TextNode("couleur", "bold", "404"),
    TextNode("fruit", "reg"),
    TextNode("fruit", "reg", " 404"),
    TextNode("fruit", "reg", " 404"),
]

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(test_nodes[0], test_nodes[0])

    def test_print(self):
        for node in test_nodes:
            self.assertEqual(str(node), f"Textnode({node.text}, {node.text_type}, {node.url})")

if __name__ == "__main__":
    unittest.main()