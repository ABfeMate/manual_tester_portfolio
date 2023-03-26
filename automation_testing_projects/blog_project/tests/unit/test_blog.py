from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        """test create blog functionality"""
        b = Blog("Test", "Test Author")

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        """test repr functionality"""
        b = Blog("Test", "Test Author")
        b2 = Blog("My Day", "Rolf")

        self.assertEqual(b.__repr__(), "Test by Test Author (0 posts)")
        self.assertEqual(b2.__repr__(), "My Day by Rolf (0 posts)")

    def test_repr_multiple_posts(self):
        """test repr functionality for multiple posts"""
        b = Blog("Test", "Test Author")
        b.posts = ["test"]
        b2 = Blog("My Day", "Rolf")
        b2.posts = ["test", "another"]

        self.assertEqual(b.__repr__(), "Test by Test Author (1 post)")
        self.assertEqual(b2.__repr__(), "My Day by Rolf (2 posts)")


test_blog = BlogTest()
print(dir(test_blog))
methods = [attr for attr in dir(test_blog) if callable(getattr(test_blog, attr))]

# use len() to count the number of methods
num_methods = len(methods)

print(num_methods) # output: 3
