import os, glob
from post import Post

class Webblog(object):
    def __init__(self, base_path, render_base_path):
        self.__base_path = base_path
        self.__render_base_path = render_base_path

    def render_posts(self):
        for post_path in self.posts():
            post = Post(post_path)
            post.render_to_base_path(os.path.realpath(self.__render_base_path))

    def render_latest_posts(self, limit):
        accu = ''
        for post_path in self.latest_posts(limit):
            post = Post(post_path)
            accu += post.render("short-post")

        output = open(os.path.join(
            self.__render_base_path, "latest_posts.rst"), "w")
        output.write(accu)
        output.close()

    def posts(self):
        return glob.glob(os.path.join(
            os.path.realpath(self.__base_path), "*", "*", "*", "*.rst"))

    def latest_posts(self, limit):
        return self.posts()[-limit:]
