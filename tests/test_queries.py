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

    def test_make_url_latest(self):
        """test make_url_latest()."""
        grok = grokapi.queries.Grok('France', 'fr')
        result = grok._make_url_latest(90)
        expected = 'http://stats.grok.se/json/fr/latest90/France'
        self.assertEqual(result, expected)

    def test_make_url_latest_with_wrong_value(self):
        """test make_url_latest() with a wrong value should raise a ValueError Exception."""
        grok = grokapi.queries.Grok('France', 'fr')
        with self.assertRaises(ValueError):
            grok._make_url_latest(42)


if __name__ == '__main__':
    unittest.main()
