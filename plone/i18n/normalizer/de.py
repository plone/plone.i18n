# -*- coding: UTF-8 -*-

from plone.i18n.interfaces.normalizer import IURLNormalizer
from zope.interface import implements

class URLNormalizer(object):
    """
    This normalizer can normalize any unicode string and returns a URL-safe
    version that only contains of ASCII characters allowed in a URL.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IURLNormalizer, URLNormalizer)
      True
    """
    implements(IURLNormalizer)

    def normalize(self, text, locale=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        text = text.strip().lower()
        text = text.replace(u'\xc4', u'ae')
        text = text.replace(u'\xe4', u'ae')
        return text

urlnormalizer = URLNormalizer()
