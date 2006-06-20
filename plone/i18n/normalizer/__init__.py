from plone.i18n.interfaces.normalizer import IIDNormalizer
from plone.i18n.interfaces.normalizer import IURLNormalizer

from zope.component import queryUtility
from zope.interface import implements

class IDNormalizer(object):
    """
    This normalizer can normalize any unicode string and returns a
    version that only contains of ASCII characters allowed in a typical
    scripting or programming language id, such as CSS class names or Python
    variable names for example.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IIDNormalizer, IDNormalizer)
      True
    """
    implements(IIDNormalizer)

    def normalize(self, text, locale=None):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt_BR', 'sr@Latn' or 'de'
        """
        if locale is not None:
            # Try to get a normalizer for the locale
            util = queryUtility(IDNormalizer, name=locale)
            parts = locale.split('_')
            if util is None and len(parts) > 1:
                # Try to get a normalizer for the base language if we asked
                # for one for a language/country combination and found none
                util = queryUtility(IDNormalizer, name=parts[0])
            if util is not None:
                return util.normalize(text, locale=locale)

        text = text.strip().lower().replace(' ', '-')
        return text


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
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt_BR', 'sr@Latn' or 'de'
        """
        if locale is not None:
            # Try to get a normalizer for the locale
            util = queryUtility(IURLNormalizer, name=locale)
            parts = locale.split('_')
            if util is None and len(parts) > 1:
                # Try to get a normalizer for the base language if we asked
                # for one for a language/country combination and found none
                util = queryUtility(IURLNormalizer, name=parts[0])
            if util is not None:
                return util.normalize(text, locale=locale)

        text = text.strip().lower()
        return text

idnormalizer = IDNormalizer()
urlnormalizer = URLNormalizer()
