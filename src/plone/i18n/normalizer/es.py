from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# Spanish character mapping
mapping = {
    192: "A",
    193: "A",
    200: "E",
    201: "E",
    204: "I",
    205: "I",
    210: "O",
    211: "O",
    217: "U",
    218: "U",
    220: "U",
    209: "N",
    199: "C",
    224: "a",
    225: "a",
    232: "e",
    233: "e",
    236: "i",
    237: "i",
    242: "o",
    243: "o",
    249: "u",
    250: "u",
    241: "n",
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
      >>> norm.normalize(u'\xf1')
      'n'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)


normalizer = Normalizer()
