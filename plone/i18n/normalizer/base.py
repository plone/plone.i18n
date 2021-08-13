from unidecode import unidecode

import string


# On OpenBSD string.whitespace has a non-standard implementation
# See http://dev.plone.org/plone/ticket/4704 for details
whitespace = "".join([c for c in string.whitespace if ord(c) < 128])
allowed = string.ascii_letters + string.digits + string.punctuation + whitespace


def mapUnicode(text, mapping=()):
    """
    This method is used for replacement of special characters found in a
    mapping before baseNormalize is applied.
    """
    res = ""
    for ch in text:
        ordinal = ord(ch)
        if ordinal in mapping:
            # try to apply custom mappings
            res += mapping.get(ordinal)
        else:
            # else leave untouched
            res += ch
    # always apply base normalization
    return baseNormalize(res)


def baseNormalize(text):
    """
    This method is used for normalization of unicode characters to the base
    ASCII letters.
    Output is a native string with only ASCII letters, digits, punctuation
    and whitespace characters. Case is preserved.

      >>> baseNormalize(123)
      '123'

      >>> baseNormalize(u'a\u0fff')
      'a'

      >>> baseNormalize(u"foo\N{LATIN CAPITAL LETTER I WITH CARON}")
      'fooI'

      >>> baseNormalize(u"\u5317\u4EB0")
      'Bei Jing'
    """
    if not isinstance(text, str):
        # This most surely ends up in something the user does not expect
        # to see. But at least it does not break.
        text = repr(text)
    text = unidecode(text).strip()
    return "".join(filter(lambda c: c in allowed, text))
