import unittest
from app.models import Quote

class QuoteModelTest(unittest.TestCase):

    def setUp(self):
        self.new_quote = Quote(0,'Ian','Ian is a genius')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))
