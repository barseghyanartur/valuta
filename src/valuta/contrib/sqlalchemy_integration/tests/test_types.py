from flask_testing import TestCase

import valuta
from valuta.contrib.sqlalchemy_integration.types import ChoiceWithExtras

from valuta_admin import create_app, db

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("SQLAlchemyTestTypesTestCase",)


class SQLAlchemyTestTypesTestCase(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app("config_test.py")

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # ***********************************************************
    # ************************ Tests ****************************
    # ***********************************************************

    def test_choices_with_extras(self):
        c1 = ChoiceWithExtras(
            **{
                "code": valuta.EUR.uid,
                "value": 10000,
            }
        )

        c2 = ChoiceWithExtras(
            **{
                "code": valuta.EUR.uid,
                "value": 10000,
            }
        )
        with self.subTest("Testing class"):
            self.assertEqual(c1, c2)

        with self.subTest("Testing value"):
            self.assertEqual(c1, valuta.EUR.uid)
