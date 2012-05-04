import unittest
import textwrap
from post import Post

class TestPost(unittest.TestCase):

    def setUp(self):
        self.post = Post("sphinxblog/fixtures/2012/05/01/lorem-ipsum.rst")

    def test_date(self):
        self.assertEqual(self.post.date, "01/05/2012")

    def test_title(self):
        self.assertEqual(self.post.title, "Lorem ipsum")

    def test_author(self):
        self.assertEqual(self.post.author, "pigoz")

    def test_abstract(self):
        self.assertEqual(self.post.abstract,
                ("Lorem ipsum dolor sit amet,\n"
                 "consectetur adipisici elit,\nsed eiusmod tempor"))

    def test_body(self):
        self.assertEqual(self.post.body, "test")

    def test_path_component(self):
        self.assertEqual(self.post.path_component,
                         "2012/05/01/lorem-ipsum.rst")

    def test_date_key(self):
        self.assertEqual(self.post.date_key, "2012/05")

    def test_url(self):
        self.assertEqual(self.post.url,
                         "/2012/05/01/lorem-ipsum")

if __name__ == '__main__':
    unittest.main()
