from .base import mapUnicode
from .interfaces import INormalizer
from zope.interface import implementer


# Bulgarian character mapping
mapping = {
    1040: "A",
    1041: "B",
    1042: "V",
    1043: "G",
    1044: "D",
    1045: "E",
    1046: "ZH",
    1047: "Z",
    1048: "I",
    1049: "Y",
    1050: "K",
    1051: "L",
    1052: "M",
    1053: "N",
    1054: "O",
    1055: "P",
    1056: "R",
    1057: "S",
    1058: "T",
    1059: "U",
    1060: "F",
    1061: "H",
    1062: "TS",
    1063: "CH",
    1064: "SH",
    1065: "SHT",
    1066: "A",
    1068: "Y",
    1070: "YU",
    1071: "YA",
    1072: "a",
    1073: "b",
    1074: "v",
    1075: "g",
    1076: "d",
    1077: "e",
    1078: "zh",
    1079: "z",
    1080: "i",
    1081: "y",
    1082: "k",
    1083: "l",
    1084: "m",
    1085: "n",
    1086: "o",
    1087: "p",
    1088: "r",
    1089: "s",
    1090: "t",
    1091: "u",
    1092: "f",
    1093: "h",
    1094: "ts",
    1095: "ch",
    1096: "sh",
    1097: "sht",
    1098: "a",
    1100: "y",
    1102: "yu",
    1103: "ya",
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
      >>> norm.normalize(u'\u0429')
      'SHT'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)


normalizer = Normalizer()
