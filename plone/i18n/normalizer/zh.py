# -*- coding: UTF-8 -*-

from zope.interface import implementer

from plone.i18n.normalizer.interfaces import INormalizer
from plone.i18n.normalizer.base import baseNormalize
#from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.pinyin import mapping


def mapUnicode(text, mapping=()):
    """
    This method is used for replacement of special characters found in a
    mapping before baseNormalize is applied.
    """
    res = []
    word = u''
    for ch in text:
        ordinal = ord(ch)
        # split english word
        if ordinal < 128:
            word += ch
            continue
        elif word and not word.isspace():
            res.append(word.strip())
            word = u''

        if ordinal in mapping:
            # try to apply custom mappings
            res.append(mapping.get(ordinal).strip())
        else:
            # else leave untouched
            res.append(ch)
    else:
        if word and not word.isspace():
            res.append(word.strip())
    # always apply base normalization
    return baseNormalize(u'-'.join(res))


@implementer(INormalizer)
class Normalizer(object):
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let's make sure that this implementation actually fulfills the API.

      #Pass the verify ``verifyClass`` has a bug, fixed in zope.interface 4.0.5
      #>>> from zope.interface.verify import verifyClass
      #>>> verifyClass(Normalizer, INormalizer)
      #True

      >>> norm = Normalizer()
      >>> text = unicode('简繁漢字', 'utf-8')
      >>> norm.normalize(text)
      'jian-fan-han-zi'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)

normalizer = Normalizer()
