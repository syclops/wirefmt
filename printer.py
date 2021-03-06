# Wire format printer
# Author: Steve Matsumoto
# Copyright 2015

class Printer(object):
    """
    Pretty printer for wire format.
    """

    def __init__(self, width):
        self.width = width
        self.field_str = '|'
        self.length = 0

    def add_field(self, name, length):
        """
        Add a named field with a specified length to the record.
        """
        if self.length != 0 and self.length % self.width == 0:
            self.field_str += '\n' + self._full_line() + '\n|'
        self.field_str += '{0:^{width}}'.format(name, width=(length * 2 - 1))
        self.field_str += '|'
        self.length += length

    def __repr__(self):
        return '\n'.join([self._bit_numbers(),
                          self._full_line(),
                          self.field_str,
                          self._footer_line()])

    def _bit_numbers(self):
        out_str = ' '
        out_str += ' '.join(
            [' ' if i < 10 else str(i/10) for i in range(self.width)])
        out_str += '\n '
        out_str += ' '.join([str(i%10) for i in range(self.width)])
        return out_str

    def _full_line(self):
        return '-'.join('+' * (self.width + 1))

    def _footer_line(self):
        if self.length % self.width == 0:
            return self._full_line()
        else:
            return '-'.join('+' * (self.length % self.width + 1))
