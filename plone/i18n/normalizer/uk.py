# -*- coding: UTF-8 -*-
from plone.i18n.normalizer.base import mapUnicode
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


# Ukrainian character mapping (according to BGN/PCGN romanization system)
mapping = {
    0x0410: u'A',
    0x0430: u'a',
    0x0411: u'B',
    0x0431: u'b',
    0x0412: u'V',
    0x0432: u'v',
    0x0413: u'H',
    0x0433: u'h',
    0x0490: u'G',
    0x0491: u'g',
    0x0414: u'D',
    0x0434: u'd',
    0x0415: u'E',
    0x0435: u'e',
    0x0404: u'YE',
    0x0454: u'ye',
    0x0416: u'ZH',
    0x0436: u'zh',
    0x0417: u'Z',
    0x0437: u'z',
    0x0418: u'Y',
    0x0438: u'y',
    0x0406: u'I',
    0x0456: u'i',
    0x0407: u'YI',
    0x0457: u'yi',
    0x0419: u'Y',
    0x0439: u'y',
    0x041A: u'K',
    0x043A: u'k',
    0x041B: u'L',
    0x043B: u'l',
    0x041C: u'M',
    0x043C: u'm',
    0x041D: u'N',
    0x043D: u'n',
    0x041E: u'O',
    0x043E: u'o',
    0x041F: u'P',
    0x043F: u'p',
    0x0420: u'R',
    0x0440: u'r',
    0x0421: u'S',
    0x0441: u's',
    0x0422: u'T',
    0x0442: u't',
    0x0423: u'U',
    0x0443: u'u',
    0x0424: u'F',
    0x0444: u'f',
    0x0425: u'KH',
    0x0445: u'kh',
    0x0426: u'TS',
    0x0446: u'ts',
    0x0427: u'CH',
    0x0447: u'ch',
    0x0428: u'SH',
    0x0448: u'sh',
    0x0429: u'SHCH',
    0x0449: u'shch',
    0x042C: u'',
    0x044C: u'',
    0x042E: u'YU',
    0x044E: u'yu',
    0x042F: u'YA',
    0x044F: u'ya',
}


@implementer(INormalizer)
class Normalizer(object):
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
