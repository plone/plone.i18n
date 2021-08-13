from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# Portuguese character mapping
mapping = {
    192: "A",
    193: "A",
    194: "A",
    195: "A",
    201: "E",
    202: "E",
    205: "I",
    211: "O",
    212: "O",
    213: "O",
    218: "U",
    220: "U",
    199: "C",
    224: "a",
    225: "a",
    226: "a",
    227: "a",
    233: "e",
    234: "e",
    237: "i",
    243: "o",
    244: "o",
    245: "o",
    250: "u",
    252: "u",
    231: "c",
}


@implementer(INormalizer)
class Normalizer:
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
