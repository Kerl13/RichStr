from unittest import TestCase

from richstr.models import RichStr, RichStrList


class SimpleTest(TestCase):
    class Example(RichStr):
        TEMPLATE = "{a} / {b}"

        def __init__(self, a, b):
            self.a = a
            self.b = b

    def test_str(self):
        printable = self.Example(a=42, b=13)
        self.assertEqual(str(printable), "42 / 13")


class ListTest(TestCase):
    class Example(RichStrList):
        TEMPLATE = "({a}:{b})"
        SEPARATOR = ", "

    def test_str(self):
        printable = self.Example([
            {'a': 42, 'b': 13},
            {'a': 0, 'b': '_'},
        ])
        self.assertEqual(str(printable), "(42:13), (0:_)")
