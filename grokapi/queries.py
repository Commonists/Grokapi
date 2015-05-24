# -*- coding: utf-8 -*-

BASE_URL = "http://stats.grok.se/json/"


class Grok(object):

    """stats.grok.se article statistics."""

    def __init__(self, title, site):
        self.site = site
        self.title = title

    def _make_url(self, year, month):
        """Make the URL to the JSON output of stats.grok.se service."""
        return BASE_URL + "{0:s}/{1:d}{2:02d}/{3:s}".format(self.site, year, month, self.title)

    def _make_url_latest(self, latest):
        """Make URL to the JSON output of stats.grok.se service for lastest traffic.

        Args:
            latest (int): 30, 60 or 90
        """
        if latest not in [30, 60, 90]:
            raise ValueError("Expected 30, 60 or 90 instead of %s" % (latest))

        return BASE_URL + "{0:s}/latest{1:d}/{2:s}".format(self.site, latest, self.title)
