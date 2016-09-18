# -*- coding: UTF-8 -*-

from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# Spanish character mapping
mapping = {
    192: u'A', 193: u'A',
    200: u'E', 201: u'E',
    204: u'I', 205: u'I',
    210: u'O', 211: u'O',
    217: u'U', 218: u'U', 220: u'U',
    209: u'N',
    199: u'C',
    224: u'a', 225: u'a',
    232: u'e', 233: u'e',
    236: u'i', 237: u'i',
    242: u'o', 243: u'o',
    249: u'u', 250: u'u',
    241: u'n',
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
      >>> norm.normalize(u'\xf1')
      'n'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)


normalizer = Normalizer()
