#!/usr/bin/env python
import unittest

import grokapi.cli


class ArgumentParserTestCase(unittest.TestCase):

    def test_parser_good_argument(self):
        """Test that grokapi correctly parses arguments."""
        input_args = [
            '--lang', 'fr', '--year', '2014', '--month', '01',
            'A', 'B', 'C'
        ]
        args = grokapi.cli._parse_args(input_args)
        print args
        self.assertEqual(args.lang, 'fr')
        self.assertEqual(args.year, 2014)
        self.assertEqual(args.month, 1)
        self.assertEqual(args.page, ['A', 'B', 'C'])


if __name__ == '__main__':
    unittest.main()
