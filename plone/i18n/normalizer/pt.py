# -*- coding: UTF-8 -*-
from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# Portuguese character mapping
mapping = {
    192: u'A',
    193: u'A',
    194: u'A',
    195: u'A',
    201: u'E',
    202: u'E',
    205: u'I',
    211: u'O',
    212: u'O',
    213: u'O',
    218: u'U',
    220: u'U',
    199: u'C',
    224: u'a',
    225: u'a',
    226: u'a',
    227: u'a',
    233: u'e',
    234: u'e',
    237: u'i',
    243: u'o',
    244: u'o',
    245: u'o',
    250: u'u',
    252: u'u',
    231: u'c',
}


@implementer(INormalizer)
class Normalizer(object):
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(INormalizer, Normalizer)
      True

      >>> norm = Normalizer()
      >>> norm.normalize(u'\xe3')
      'ã'
      >>> norm.normalize(u'\xea')
      'ê'
      >>> norm.normalize(u'\xf5')
      'õ'
      >>> norm.normalize(u'\xe7')
      'ç'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)


normalizer = Normalizer()
