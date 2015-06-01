# -*- coding: utf-8 -*-
import sys
from queries import Grok


def print_monthly_views(site, pages, year, month):
    grok = Grok(site)
    for page in pages:
        result = grok.get_views_for_month(page, year, month)
        print result['daily_views']


def _make_parser():
    from argparse import ArgumentParser
    description = 'Extract traffic statistics of Wikipedia articles.'
    parser = ArgumentParser(description=description)
    parser.add_argument("-l", "--lang",
                        type=str,
                        dest="lang",
                        default="en",
                        required=False,
                        help="Language code for Wikipedia")
    parser.add_argument("-y", "--year",
                        type=int,
                        dest="year",
                        required=False,
                        help="Year")
    parser.add_argument("-m", "--month",
                        type=int,
                        dest="month",
                        required=False,
                        help="Month")
    parser.add_argument("page", nargs='*',
                        metavar="PAGE",
                        help='A list of pages')
    return parser


def _parse_args(args):
    parser = _make_parser()
    return parser.parse_args(args)


def main():
    """Main entry-point."""
    args = _parse_args(sys.argv)
    print_monthly_views(args.lang, args.page, args.year, args.month)


if __name__ == '__main__':
    main()
