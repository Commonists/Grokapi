# -*- coding: utf-8 -*-


class Grok(object):

    """stats.grok.se article statistics."""

    def __init__(self, title, site):
        self.site = site
        self.title = title

    def _make_url(self, year, month):
        """Make the URL to the JSON output of stats.grok.se service."""
        base_url = "http://stats.grok.se/json/"
        return base_url + "{0:s}/{1:d}{2:02d}/{3:s}".format(self.site, year, month, self.title)
