#!/usr/bin/env python

import os, sys, glob
from post import Post

if __name__ == "__main__":
    glob_p = os.path.join("_posts", "*", "*", "*", "*.rst")
    print glob_p
    for post_path in glob.glob(glob_p):
        print Post(post_path).date()
