"""
Test Base
"""
import pytest
import unittest

from proj import base


class BaseTest(unittest.TestCase):
    '''Tests for Request'''

    def setUp(self):
        pass

    def test_init(self):
        base.Main('foo', 1)

    def test_run(self):
        main = base.Main('foo', 1)
        self.assertEquals(main.run(), 'foo 1')
        self.assertEquals(main.run(upper=True), 'FOO 1')
