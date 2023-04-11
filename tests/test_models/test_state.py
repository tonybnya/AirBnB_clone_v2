#!/usr/bin/python3
""" Unit Tests for state model """
import os
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """ Test class  for state model """

    def __init__(self, *args, **kwargs):
        """ State test class init """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ Testing state name attr """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
