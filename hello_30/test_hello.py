""" simple test """

import unittest

from hello import hello

class TestHello(unittest.TestCase):
    """simple test"""
    
    def test_world(self):
        """simple test"""
        self.assertEqual(hello('world'), "hello world")
 
    def test_world_with_unicode(self):
        """simple test with unicode"""
        self.assertEqual(hello(u'world'), u"hello world")
