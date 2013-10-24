# encoding: utf-8

"""A simple Chinese word count utility."""

import re

__version__ = '0.1.0'

def zwc(string):
    """Count non-blank characters in a unicode string.
    The fullwidth space character (　) is also ignored.
    e.g. zwc(u'樂土樂土　爰得我所') => 8
    """
    if not isinstance(string, unicode):
        raise TypeError('zwc requires a unicode string')

    # remove blank characters
    visible_chars = re.sub(ur'[\s\u3000]+', '', string)

    return len(visible_chars)
