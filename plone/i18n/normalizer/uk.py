from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# Ukrainian character mapping (according to BGN/PCGN romanization system)
mapping = {
    0x0410: "A",
    0x0430: "a",
    0x0411: "B",
    0x0431: "b",
    0x0412: "V",
    0x0432: "v",
    0x0413: "H",
    0x0433: "h",
    0x0490: "G",
    0x0491: "g",
    0x0414: "D",
    0x0434: "d",
    0x0415: "E",
    0x0435: "e",
    0x0404: "YE",
    0x0454: "ye",
    0x0416: "ZH",
    0x0436: "zh",
    0x0417: "Z",
    0x0437: "z",
    0x0418: "Y",
    0x0438: "y",
    0x0406: "I",
    0x0456: "i",
    0x0407: "YI",
    0x0457: "yi",
    0x0419: "Y",
    0x0439: "y",
    0x041A: "K",
    0x043A: "k",
    0x041B: "L",
    0x043B: "l",
    0x041C: "M",
    0x043C: "m",
    0x041D: "N",
    0x043D: "n",
    0x041E: "O",
    0x043E: "o",
    0x041F: "P",
    0x043F: "p",
    0x0420: "R",
    0x0440: "r",
    0x0421: "S",
    0x0441: "s",
    0x0422: "T",
    0x0442: "t",
    0x0423: "U",
    0x0443: "u",
    0x0424: "F",
    0x0444: "f",
    0x0425: "KH",
    0x0445: "kh",
    0x0426: "TS",
    0x0446: "ts",
    0x0427: "CH",
    0x0447: "ch",
    0x0428: "SH",
    0x0448: "sh",
    0x0429: "SHCH",
    0x0449: "shch",
    0x042C: "",
    0x044C: "",
    0x042E: "YU",
    0x044E: "yu",
    0x042F: "YA",
    0x044F: "ya",
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
      >>> norm.normalize(u'\u041f\u043b\u043e\u043d')
      'Plon'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)


normalizer = Normalizer()
