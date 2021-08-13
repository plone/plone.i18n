from plone.i18n.normalizer.base import allowed
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


MAX_LENGTH = 6

TABLE = "abcdefghijklmnopqrstuvwxyz0123456789"
TABLE_LEN = len(TABLE)


def _gethashed(obj, n):
    num = hash(obj) % (TABLE_LEN ** n)
    while True:
        d, m = divmod(num, TABLE_LEN)
        num = d
        yield TABLE[m]
        if d == 0:
            return


def ja_normalize(text, max_length=MAX_LENGTH):
    """
    This function is normalize for Japanese.
    exchange from unicode string to hash and base64 string.
    """
    text = text.strip()
    if all(s in allowed for s in text):
        exchanged = text
    else:
        exchanged = "".join(_gethashed(text, max_length))
    return exchanged


@implementer(INormalizer)
class Normalizer:
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(INormalizer, Normalizer)
      True

    Strings that contain only ASCII characters are returned decoded.

      >>> norm = Normalizer()
      >>> text = u"test page"
      >>> norm.normalize(text)
      'test page'

    Text that contains non-ASCII characters are normalized.

      >>> norm = Normalizer()
      >>> text = u"公開テストページ"
      >>> normalized = norm.normalize(text)
      >>> all(s in allowed for s in normalized)
      True

    We expect the default length of 6.
    Report the normalized value in case of failure.

      >>> 5 <= len(normalized) <= 6 or (len(normalized), normalized)
      True

    The max_length argument is respected.
      >>> normalized = norm.normalize(text, max_length=8)
      >>> 7 <= len(normalized) <= 8 or (len(normalized), normalized)
      True
    """

    def normalize(self, text, locale=None, max_length=MAX_LENGTH):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return ja_normalize(text, max_length=max_length)


normalizer = Normalizer()
