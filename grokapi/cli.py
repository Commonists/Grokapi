# -*- coding: utf-8 -*-

from queries import Grok


def print_monthly_views(site, pages, year, month):
    grok = Grok(site)
    for page in pages:
        result = grok.get_views_for_month(page, year, month)
        print result['daily_views']


def main():
    """ main script. """
    from argparse import ArgumentParser
    description = 'Extract traffic statistics of Wikipedia articles.'
    parser = ArgumentParser(description=description)
    parser.add_argument("-l", "--lang",
                        type=str,
                        dest="lang",
                        default="en",
                        required=True,
                        help="Language code for Wikipedia")
    parser.add_argument("-y", "--year",
                        type=int,
                        dest="year",
                        default="en",
                        required=True,
                        help="Year")
    parser.add_argument("-m", "--month",
                        type=int,
                        dest="month",
                        default="en",
                        required=True,
                        help="Month")
    parser.add_argument("page", nargs='*',
                        metavar="PAGE",
                        help='A list of pages')
    args = parser.parse_args()
    print_monthly_views(args.lang, args.page, args.year, args.month)

if __name__ == '__main__':
    main()
