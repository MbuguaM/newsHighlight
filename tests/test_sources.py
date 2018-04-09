import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):

    """ Test for the sources class """
    def SetUp(self):
        """ creating a cutom function """
        self.new_source = Sources(1, "Mbugua", "Awsomenews", "fakeurl", "disaster")

    # def TearDown(self)
    def test_init(self):
        """ test to see that the source constructor works """

        self.assertEqual(self.new_source.id,1)
        self.assertEqual(self.new_source.name,"Mbugua")
        self.assertEqual(self.new_source.description,"Awsomenews")
        self.assertEqual(self.new_source.url,"fakeurl")
        self.assertEqual(self.new_source.category,"disaster")
    