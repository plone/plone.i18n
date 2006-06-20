# -*- coding: UTF-8 -*-
"""
    Normalizer tests.
"""

import unittest

import plone.i18n
from plone.i18n.interfaces.normalizer import IIDNormalizer
from plone.i18n.interfaces.normalizer import IURLNormalizer

import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', plone.i18n)()

def testIDNormalizer():
    """
      >>> util = queryUtility(IIDNormalizer)
      >>> util
      <plone.i18n.normalizer.IDNormalizer object at ...>

      >>> util.normalize(u'simpleandsafe')
      u'simpleandsafe'

      >>> util.normalize(u' Whitespace and capital Letters  ')
      u'whitespace-and-capital-letters'
    """

def testURLNormalizer():
    """
      >>> util = queryUtility(IURLNormalizer)
      >>> util
      <plone.i18n.normalizer.URLNormalizer object at ...>
      
      >>> util.normalize(u'simpleandsafe')
      u'simpleandsafe'

      >>> util.normalize(u' Whitespace and capital Letters  ')
      u'whitespace and capital letters'
    """

def testLocaleAwareURLNormalizer():
    """
      >>> util = queryUtility(IURLNormalizer)
      >>> util
      <plone.i18n.normalizer.URLNormalizer object at ...>

      >>> util.normalize(u'simpleandsafe', locale='de')
      u'simpleandsafe'

      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de')
      u'text with umlaeut'

    Make sure we get the de normalizer as there's no special one for de_DE
    registered.
       
      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de_DE')
      u'text with umlaeut'

      >>> util.normalize(u'simpleandsafe', locale='pt_BR')
      u'simpleandsafe'

      >>> util.normalize(u'simpleandsafe', locale='sr@Latn')
      u'simpleandsafe'
    """

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.i18n.normalizer'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
