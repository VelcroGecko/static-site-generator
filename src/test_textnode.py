import unittest


from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff_testtype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is another text node", TextType.TEXT, url="Testurl@testing.com")
        node2 = TextNode("This is another text node", TextType.TEXT,url="Testurl@testing.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()