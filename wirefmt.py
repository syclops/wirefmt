# Wire format pretty printer
# Author: Steve Matsumoto
# Copyright 2015

import argparse

def printNums(width):
    print ''.join([' ' + (' ' if i < 10 else str(i/10)) for i in range(width)])
    print ''.join([' ' + str(i % 10) for i in range(width)])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--width', type=int, choices=[16, 32],
                        default=32,
                        help='width of the format in bits (default: 32)')
    args = parser.parse_args()
    printNums(args.width)

if __name__ == '__main__':
    main()
