from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# Greek character mapping
mapping = {
    902: "A",
    904: "E",
    905: "H",
    906: "I",
    908: "O",
    910: "Y",
    911: "O",
    912: "i",
    913: "A",
    914: "B",
    915: "G",
    916: "D",
    917: "E",
    918: "Z",
    919: "I",
    920: "Th",
    921: "I",
    922: "K",
    923: "L",
    924: "M",
    925: "N",
    926: "Ks",
    927: "O",
    928: "P",
    929: "R",
    931: "S",
    932: "T",
    933: "Y",
    934: "F",
    935: "Ch",
    936: "Ps",
    937: "O",
    938: "I",
    939: "Y",
    940: "a",
    941: "e",
    942: "i",
    943: "i",
    944: "y",
    945: "a",
    946: "b",
    947: "g",
    948: "d",
    949: "e",
    950: "z",
    951: "i",
    952: "th",
    953: "i",
    954: "k",
    955: "l",
    956: "m",
    957: "n",
    958: "ks",
    959: "o",
    960: "p",
    961: "r",
    962: "s",
    963: "s",
    964: "t",
    965: "y",
    966: "f",
    967: "ch",
    968: "ps",
    969: "o",
    970: "i",
    971: "y",
    972: "o",
    973: "y",
    974: "o",
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
      >>> norm.normalize(u'\u03b9')
      'i'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)


normalizer = Normalizer()
