from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# Russian character mapping
mapping = {
    1081: "i",
    1049: "I",
    1094: "c",
    1062: "C",
    1091: "u",
    1059: "U",
    1082: "k",
    1050: "K",
    1077: "e",
    1045: "E",
    1085: "n",
    1053: "N",
    1075: "g",
    1043: "G",
    1096: "sh",
    1064: "SH",
    1097: "sch",
    1065: "SCH",
    1079: "z",
    1047: "Z",
    1093: "h",
    1061: "H",
    1098: "",
    1066: "",
    1092: "f",
    1060: "F",
    1099: "y",
    1067: "Y",
    1074: "v",
    1042: "V",
    1072: "a",
    1040: "A",
    1087: "p",
    1055: "P",
    1088: "r",
    1056: "R",
    1086: "o",
    1054: "O",
    1083: "l",
    1051: "L",
    1076: "d",
    1044: "D",
    1078: "zh",
    1046: "ZH",
    1101: "e",
    1069: "E",
    1103: "ya",
    1071: "YA",
    1095: "ch",
    1063: "CH",
    1089: "s",
    1057: "S",
    1084: "m",
    1052: "M",
    1080: "i",
    1048: "I",
    1090: "t",
    1058: "T",
    1100: "",
    1068: "",
    1073: "b",
    1041: "B",
    1102: "yu",
    1070: "YU",
    1105: "yo",
    1025: "YO",
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
      'SCH'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        return mapUnicode(text, mapping=mapping)


normalizer = Normalizer()
