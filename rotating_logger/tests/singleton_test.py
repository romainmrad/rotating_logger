import unittest
from unittest import TestCase
from rotating_logger.src.singleton import singleton


class SingletonTest(TestCase):
    def setUp(self):
        @singleton
        class SomeClass(object):
            pass

        @singleton
        class SomeOtherClass(object):
            pass

        self.instance = SomeClass()
        self.other_instance = SomeOtherClass()

    def tearDown(self):
        del self.instance, self.other_instance

    def test_singleton(self):
        self.assertEqual(self.instance, self.instance)


if __name__ == '__main__':
    unittest.main()
