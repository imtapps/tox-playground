import unittest
import django

try:
    from django.utils.crypto import constant_time_compare
except ImportError:
    def constant_time_compare(val1, val2):
        if len(val1) != len(val2):
            return False
        result = 0
        for x, y in zip(val1, val2):
            result |= ord(x) ^ ord(y)
        return result == 0


class MyTests(unittest.TestCase):

    def test_django_constant_time_compare(self):
        self.assertTrue(constant_time_compare('asdf', 'asdf'))

    def test_string_substitution(self):
        self.assertEqual("123", "{0}{1}{2}".format(1, 2, 3))

