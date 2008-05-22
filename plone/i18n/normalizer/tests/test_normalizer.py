# -*- coding: utf-8 -*-
"""
    Normalizer tests.
"""

import unittest

import plone.i18n.normalizer
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.i18n.normalizer.interfaces import IFileNameNormalizer
from plone.i18n.normalizer.interfaces import IURLNormalizer

import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', plone.i18n.normalizer)()


def testIDNormalizer():
    """
      >>> util = queryUtility(IIDNormalizer)
      >>> util
      <plone.i18n.normalizer.IDNormalizer object at ...>

      >>> util.normalize(u'simpleandsafe')
      'simpleandsafe'

      >>> util.normalize(u' Whitespace and capital Letters  ')
      'whitespace-and-capital-letters'

      >>> util.normalize(u">here's another!")
      'heres-another'

      >>> util.normalize(u">>>here'!--s yet another!!!")
      'here-s-yet-another'

      >>> util.normalize(unicode("umläut.doc", 'utf-8'))
      'umlaut.doc'

      >>> from plone.i18n.normalizer import MAX_LENGTH
      
      >>> testString = u"thissentenceiswaytolongtobecroppedwithoutcuttedbythenormalizemethodbecauseithasnoplacetocrop"
      >>> util.normalize(testString)
      'thissentenceiswaytolongtobecroppedwithoutcuttedbyt'
      >>> len(util.normalize(testString)) == MAX_LENGTH
      True

      >>> testString = u"thissentenceisacropped-by-the-normalize-method-because-it-has-many-places-to-crop"
      >>> util.normalize(testString)
      'thissentenceisacropped-by-the-normalize-method'
      >>> len(util.normalize(testString)) <= MAX_LENGTH
      True

      >>> testString = u"this-sentence-is-way-to-long-but-can-be-cropped-by-the-normalize-method-because-it-has-many-places-to-crop"
      >>> util.normalize(testString)
      'this-sentence-is-way-to-long-but-can-be-cropped-by'
      >>> len(util.normalize(testString)) <= MAX_LENGTH
      True

      >>> util.normalize(unicode("rest `n` peace", 'utf-8'))
      'rest-n-peace'
    """


def testLocaleAwareIDNormalizer():
    """
      >>> util = queryUtility(IIDNormalizer)
      >>> util
      <plone.i18n.normalizer.IDNormalizer object at ...>

    Register the German file name normalizer as an id normalizer as well, to
    test the locale-aware id normalization logic:

      >>> de_util = queryUtility(IFileNameNormalizer, name='de')
      >>> sm = zope.component.getGlobalSiteManager()
      >>> sm.registerUtility(de_util, IIDNormalizer, name='de')

      >>> util.normalize(u'simpleandsafe', locale='de')
      'simpleandsafe'

      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de')
      'text-with-umlaeut'

    Make sure we get the de normalizer as there's no special one for de_DE
    registered.
       
      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de_DE')
      'text-with-umlaeut'

      >>> util.normalize(u'simpleandsafe', locale='pt_BR')
      'simpleandsafe'

      >>> util.normalize(u'simpleandsafe', locale='sr@Latn')
      'simpleandsafe'
    """


def testFileNameNormalizer():
    """
      >>> util = queryUtility(IFileNameNormalizer)
      >>> util
      <plone.i18n.normalizer.FileNameNormalizer object at ...>
      
      >>> util.normalize(u'simpleandsafe')
      'simpleandsafe'

      >>> util.normalize(u' Whitespace and capital Letters  ')
      'Whitespace and capital Letters'

      >>> util.normalize(u">here's another!")
      'heres another'

      >>> util.normalize(u">>>here'!--s yet another!!!")
      'here-s yet another'

      >>> util.normalize(u"{[(me too)]}")
      'me too'

      >>> util.normalize("pseudo_filename,pot.doc")
      'pseudo-filename-pot.doc'

      >>> util.normalize(unicode("umläut.doc", 'utf-8'))
      'umlaut.doc'

      >>> len(util.normalize(u'aa-' * 2000))
      1022

      >>> util.normalize(unicode("rest `n` peace", 'utf-8'))
      'rest -n- peace'
    """


def testLocaleAwareFileNameNormalizer():
    """
      >>> util = queryUtility(IFileNameNormalizer)
      >>> util
      <plone.i18n.normalizer.FileNameNormalizer object at ...>

      >>> util.normalize(u'simpleandsafe', locale='de')
      'simpleandsafe'

      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de')
      'text with umlaeut'

    Make sure we get the de normalizer as there's no special one for de_DE
    registered.
       
      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de_DE')
      'text with umlaeut'

      >>> util.normalize(u'simpleandsafe', locale='pt_BR')
      'simpleandsafe'

      >>> util.normalize(u'simpleandsafe', locale='sr@Latn')
      'simpleandsafe'
    """


def testURLNormalizer():
    """
      >>> util = queryUtility(IURLNormalizer)
      >>> util
      <plone.i18n.normalizer.URLNormalizer object at ...>
      
      >>> util.normalize(u'simpleandsafe')
      'simpleandsafe'

      >>> util.normalize(u' Whitespace and capital Letters  ')
      'whitespace-and-capital-letters'

      >>> util.normalize(u">here's another!")
      'heres-another'

      >>> util.normalize(u">>>here'!--s yet another!!!")
      'here-s-yet-another'

      >>> util.normalize(u"Doe, Joe")
      'doe-joe'

      >>> util.normalize(unicode("umläut.doc", 'utf-8'))
      'umlaut.doc'

      >>> util.normalize('quote "this"!')
      'quote-this'

      >>> util.normalize("quote 'this'!")
      'quote-this'

      >>> util.normalize("I'm not a FILE.txt")
      'im-not-a-file.txt'

      >>> util.normalize("I'm a big file.TXT")
      'im-a-big-file.txt'

      >>> util.normalize(unicode("rest `n` peace", 'utf-8'))
      'rest-n-peace'
    """


def testLocaleAwareURLNormalizer():
    """
      >>> util = queryUtility(IURLNormalizer)
      >>> util
      <plone.i18n.normalizer.URLNormalizer object at ...>

      >>> util.normalize(u'simpleandsafe', locale='de')
      'simpleandsafe'

      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de')
      'text-with-umlaeut'

    Make sure we get the de normalizer as there's no special one for de_DE
    registered.
       
      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de_DE')
      'text-with-umlaeut'

      >>> util.normalize(u'simpleandsafe', locale='pt_BR')
      'simpleandsafe'

      >>> util.normalize(u'simpleandsafe', locale='sr@Latn')
      'simpleandsafe'
    """

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.i18n.normalizer'),
        DocTestSuite('plone.i18n.normalizer.base'),
        DocTestSuite('plone.i18n.normalizer.de'),
        DocTestSuite('plone.i18n.normalizer.el'),
        DocTestSuite('plone.i18n.normalizer.pl'),
        DocTestSuite('plone.i18n.normalizer.ru'),
        DocTestSuite('plone.i18n.normalizer.tr'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
