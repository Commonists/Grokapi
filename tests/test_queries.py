#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Unit tests for traffic statistics stuff."""

import unittest
import grokapi.queries


class TestGrok(unittest.TestCase):

    """Test Traffic class."""

    def test_make_url(self):
        """Test _make_url()."""
        grok = grokapi.queries.Grok('fr')
        result = grok._make_url('France', 2013, 01)
        expected = 'http://stats.grok.se/json/fr/201301/France'
        self.assertEqual(result, expected)

    def test_make_url_latest(self):
        """test make_url_latest()."""
        grok = grokapi.queries.Grok('fr')
        result = grok._make_url_latest('France', 90)
        expected = 'http://stats.grok.se/json/fr/latest90/France'
        self.assertEqual(result, expected)

    def test_make_url_latest_with_wrong_value(self):
        """test make_url_latest() with a wrong value should raise a ValueError Exception."""
        grok = grokapi.queries.Grok('fr')
        with self.assertRaises(ValueError):
            grok._make_url_latest('France', 42)


class TestGrokOnline(unittest.TestCase):

    def test_get_latest_views(self):
        grok = grokapi.queries.Grok('fr')
        result = grok.get_latest_views('France', 90)
        self.assertIn(u'month', result)
        self.assertIn(u'rank', result)
        self.assertIn(u'daily_views', result)
        self.assertEquals(result[u'month'], u'latest90')
        self.assertIsInstance(result[u'rank'], int)
        self.assertIsInstance(result[u'daily_views'], dict)

    def test_get_views_for_month(self):
        grok = grokapi.queries.Grok('fr')
        title = 'France'
        result = grok.get_views_for_month(title, 2015, 1)
        self.assertIn(u'project', result)
        self.assertIn(u'title', result)
        self.assertEquals(result[u'title'], title)
        self.assertIn(u'daily_views', result)
        self.assertIsInstance(result[u'daily_views'], dict)


if __name__ == '__main__':
    unittest.main()
