from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# German character mapping
#
# Special characters:
#     8222: German left double quotation mark
#     8220: German right double quotation mark
#     8218: German left single quotation mark
#     8216: German right single quotation mark
#     8211: en dash '-'
#      167: paragraph character
#     8364: Euro sign

mapping = {
    196: "AE",
    198: "AE",
    214: "OE",
    220: "UE",
    223: "ss",
    224: "a",
    228: "ae",
    230: "ae",
    246: "oe",
    252: "ue",
    8222: "-",
    8220: "-",
    8218: "-",
    8216: "-",
    8211: "-",
    167: "-",
    8364: "euro",
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
      >>> norm.normalize(u'\xe4')
      'ae'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)


normalizer = Normalizer()
