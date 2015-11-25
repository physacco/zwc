# encoding: utf-8

"""A simple Chinese word count utility."""

import re
import six

__version__ = '0.2.0'

def zwc(string):
    """Count non-blank characters in a unicode string.
    The fullwidth space character (　) is also ignored.
    e.g. zwc(u'樂土樂土　爰得我所') => 8
    """
    if not isinstance(string, six.text_type):
        raise TypeError('zwc requires a unicode string')

    # remove blank characters
    visible_chars = re.sub(r'\s+', '', string, flags=re.UNICODE)

    return len(visible_chars)
