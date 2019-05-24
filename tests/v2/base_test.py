import unittest
import os

from app import parcel_app
from app.api.v2.models.database import Database


class BaseTest(unittest.TestCase):
    """Class to setup the app and tear down the data model."""

    def setUp(self):
        """Set up the app for testing."""

        Database().destroy_table()
        Database().create_table()
        self.app = parcel_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Tear down the data models after the tests run."""

        self.app_context.push()
        Database().destroy_table()
