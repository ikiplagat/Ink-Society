import unittest
from app.models import Post

class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.new_post = Post()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))


