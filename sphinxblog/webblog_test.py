import unittest, textwrap, os
from webblog import Webblog

class TestWebblog(unittest.TestCase):

    def setUp(self):
        self.base = os.path.join(
            os.path.realpath(os.path.dirname(__file__)), "fixtures")
        self.blog = Webblog(self.base, "/tmp")

    def test_posts(self):
        self.assertEqual(self.blog.posts(),
            [os.path.join(self.base, "2012", "05", "08", "baz.rst"),
             os.path.join(self.base, "2012", "05", "02", "foo-bar.rst"),
             os.path.join(self.base, "2012", "05", "01", "lorem-ipsum.rst")])

    def test_latest_posts_with_2_posts(self):
        self.assertEqual(self.blog.latest_posts(2),
            [os.path.join(self.base, "2012", "05", "08", "baz.rst"),
             os.path.join(self.base, "2012", "05", "02", "foo-bar.rst")])

    def test_latest_posts_with_1_post(self):
        self.assertEqual(self.blog.latest_posts(1),
            [os.path.join(self.base, "2012", "05", "08", "baz.rst")])

    def test_posts_archive(self):
        self.assertEqual(self.blog.posts_archive(),
            {"2012/05" :
            [os.path.join(self.base, "2012", "05", "08", "baz.rst"),
             os.path.join(self.base, "2012", "05", "02", "foo-bar.rst"),
             os.path.join(self.base, "2012", "05", "01", "lorem-ipsum.rst")]})

if __name__ == '__main__':
    unittest.main()
