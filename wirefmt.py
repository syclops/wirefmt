# Wire format pretty printer
# Author: Steve Matsumoto
# Copyright 2015

import argparse
import fileinput

from printer import Printer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--width', type=int, choices=[16, 32],
                        default=32,
                        help='width of the format in bits (default: 32)')
    parser.add_argument('file', help='Path of field specification file')
    args = parser.parse_args()
    p = Printer(args.width)
    for line in fileinput.input(args.file):
        [name, length] = line.strip().split()
        p.add_field(name, length)
    print p

if __name__ == '__main__':
    main()
