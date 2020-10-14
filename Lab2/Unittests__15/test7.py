import unittest
from Metaclass__7 import Creator, Vehicle, Star

class TestMetaclass(unittest.TestCase):
    def setUp(self) -> None:
        self.attrs = {'color': 'white', 'doors': 5, 'wheels': 4, 'places': 5,
                      'class': 'sedan', 'tires': 'belshina', 'rudder': 'left', 'airbag': 2}
        self.attrs2 = {'name': None, 'temperature': 0, 'massEarth': 1, 'volumeEarth': 1}

    def test_Mets(self):
        def compare_dict(d1, d2):
            for para in d1.items():
                if para not in d2.items():
                    return False
            return True
        self.assertTrue(compare_dict(self.attrs, Vehicle.__dict__), "Проверить аттрс")
        self.assertTrue(compare_dict(self.attrs2, Star.__dict__), "Проверить аттрс")