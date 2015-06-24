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
        pass

    def __repr__(self):
        return '\n'.join([self._bit_numbers(),
                          self._header_footer_line(),
                          self.field_str,
                          self._header_footer_line()])

    def _bit_numbers(self):
        out_str = ' '
        out_str += ' '.join(
            [' ' if i < 10 else str(i/10) for i in range(self.width)])
        out_str += '\n '
        out_str += ' '.join([str(i%10) for i in range(self.width)])
        return out_str

    def _header_footer_line(self):
        return '-'.join('+' * (self.width + 1))
