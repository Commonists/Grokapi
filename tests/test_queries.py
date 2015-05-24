#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Unit tests for traffic statistics stuff."""

import unittest
import grokapi.queries


class TestGrok(unittest.TestCase):

    """Test Traffic class."""

    def test_make_url(self):
        """Test _make_url()."""
        grok = grokapi.queries.Grok('France', 'fr')
        result = grok._make_url(2013, 01)
        expected = 'http://stats.grok.se/json/fr/201301/France'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
