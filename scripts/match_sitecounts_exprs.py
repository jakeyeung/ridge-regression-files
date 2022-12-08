#!/usr/bin/env python
'''
DESCRIPTION

    Match sitecounts and expression matrices so that they have same rows, force number of
    genes in expressed matrix to match number of genes in sitecounts. Write new sitecounts
    and expression to output file

FOR HELP

    python match_sitecounts_exprs.py --help

AUTHOR:      Jake Yeung (jake.yeung@epfl.ch)
LAB:         Computational Systems Biology Lab (http://naef-lab.epfl.ch)
CREATED ON:  2015-06-17
LAST CHANGE: see git log
LICENSE:     MIT License (see: http://opensource.org/licenses/MIT)
'''

import sys, argparse


def main():
    parser = argparse.ArgumentParser(description='Match sitecounts and expression matrices so that they have same rows, force number of ')
    parser.add_argument('sitecount', metavar='SITECOUNTS',
                        help='Path to sitecount matrix')
    parser.add_argument('expression', metavar='EXPRESSION',
                        help='Path to expression matrix')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Suppress some print statements')
    args = parser.parse_args()

    # store command line arguments for reproducibility
    CMD_INPUTS = ' '.join(['python'] + sys.argv)    # easy printing later
    # store argparse inputs for reproducibility / debugging purposes
    args_dic = vars(args)
    ARG_INPUTS = ['%s=%s' % (key, val) for key, val in args_dic.iteritems()]
    ARG_INPUTS = ' '.join(ARG_INPUTS)

    # Print arguments supplied by user
    if not args.quiet:
        print('Command line inputs:')
        print(CMD_INPUTS)
        print ('Argparse variables:')
        print(ARG_INPUTS)



if __name__ == '__main__':
    main()
