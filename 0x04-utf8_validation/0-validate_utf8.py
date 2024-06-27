#!/usr/bin/python3
""" Defines `validUTF8` function """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    try:
        bytes(data).decode('utf8')
        return True
    except (ValueError, UnicodeDecodeError):
        return False
