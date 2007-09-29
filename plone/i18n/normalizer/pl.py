# -*- coding: UTF-8 -*-

from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implements
from plone.i18n.normalizer.base import mapUnicode

# Polish character mapping
mapping = {
    321 : 'L', 322 : 'l',
}

class Normalizer(object):
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(INormalizer, Normalizer)
      True
    """
    implements(INormalizer)

    def normalize(self, text, locale=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)

normalizer = Normalizer()
