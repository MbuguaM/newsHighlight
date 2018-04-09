import unittest
from app.models import Article


class SourcesTest(unittest.TestCase):

    """ Test for the sources class """
    def SetUp(self):
        """ creating a cutom function """
        self.new_article = Article("Mbugua", "Munga", "Civilization to savages","Brief Description", "12:20:13")

    # def TearDown(self)
    def test_init(self):
        """ test to see that the source constructor works """

        self.assertEqual(self.new_article.source_name,1)
        self.assertEqual(self.new_article.author,"Mbugua")
        self.assertEqual(self.new_article.title,"Awsomenews")
        self.assertEqual(self.new_article.description,"fakeurl")
        self.assertEqual(self.new_article.published_at,"disaster")
    