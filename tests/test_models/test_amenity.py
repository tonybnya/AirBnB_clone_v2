#!/usr/bin/python3
""" Unit Tests for amenity model """
import os
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class AestAmenity(TestBaseModel):
    """ Test class for amenity model """

    def __init__(self, *args, **kwargs):
        """ Init the test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
