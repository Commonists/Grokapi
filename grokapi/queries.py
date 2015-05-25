# -*- coding: utf-8 -*-

import requests


BASE_URL = "http://stats.grok.se/json/"


class Grok(object):

    """stats.grok.se page statistics."""

    def __init__(self, site):
        self.site = site

    def _make_url(self, page, year, month):
        """Make the URL to the JSON output of stats.grok.se service."""
        return BASE_URL + "{0:s}/{1:d}{2:02d}/{3:s}".format(self.site, year, month, page)

    def _make_url_latest(self, page, latest):
        """Make URL to the JSON output of stats.grok.se service for lastest traffic.

        Args:
            latest (int): 30, 60 or 90
        """
        if latest not in [30, 60, 90]:
            raise ValueError("Expected 30, 60 or 90 instead of %s" % (latest))

        return BASE_URL + "{0:s}/latest{1:d}/{2:s}".format(self.site, latest, page)

    def get_latest_views(self, page, latest):
        """Return amount of views from the getlatest days.

        Args:
            page (wikipage): article on which we are querying stats.
            latest (int): amount of days we are going to fetch
                values must be 30, 60, or 90
        """
        url = self._make_url_latest(page, latest)
        result = requests.get(url).json()
        return result

    def get_views_for_month(self, page, year, month):
        url = self._make_url(page, year, month)
        result = requests.get(url).json()
        return result
