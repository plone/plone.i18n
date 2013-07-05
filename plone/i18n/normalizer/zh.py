# -*- coding: UTF-8 -*-
#  Author      : Feather.et.ELF <andelf@139.com> 
#  Created     : Fri Oct  8 22:11:04 2010 by Feather.et.ELF 
#  Copyright   : Feather Workshop (c) 2010 
#  Description : A zope.i18n normalizer for zh 
#  History     : 2013/07/04 porting into plone.i18n, penguin

from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implements
from plone.i18n.normalizer.base import baseNormalize

# Chinese character pinyin mapping
from .pinyin import PinYinDict as mapping

def zh_normalizer(text, mapping=()):
    """
    Convert Chinese to pinyin, add '-' between Chinese and English word.
    Original by andelf, enhanced by penguin
    """
    res = []
    word = u'' # handle english words
    preIsWord = False
    preIsPinyin = False
    for ch in text:
        ordinal = ord(ch)
        # latin word
        if ordinal< 127 and ch.isalnum():
            word += ch
            continue
        elif word:
            if preIsWord or preIsPinyin:
                res.append(u'-')
                preIsPinyin = False
            res.append(word)
            word = u''
            preIsWord = True
        # Pin yin
        if ordinal in mapping:
            if preIsWord:
                res.append(u'-')
                preIsWord = False
            res.append(mapping.get(ordinal) or ch)
            preIsPinyin = True
        else:
            # Normal char: comma, minus, etc
            res.append(ch)
            preIsWord = False
            preIsPinyin = False

    res.append(word)
    return  u''.join(res)

class Normalizer(object):
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let's make sure that this implementation actually fulfills the API.

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(INormalizer, Normalizer)
    True
    """
    implements(INormalizer)

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        mapped = zh_normalizer(text, mapping=mapping)

        return baseNormalize(mapped)

normalizer = Normalizer()
