# -*- coding: UTF-8 -*-
"""
    Languages tests.
"""

import unittest

import plone.i18n.locales
from plone.i18n.locales.interfaces import IContentLanguageAvailability
from plone.i18n.locales.interfaces import IMetadataLanguageAvailability

import zope.app.publisher.browser
import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('meta.zcml', zope.app.publisher.browser)()
    XMLConfig('configure.zcml', plone.i18n.locales)()

def testContentLanguageAvailability():
    """
      >>> util = queryUtility(IContentLanguageAvailability)
      >>> util
      <plone.i18n.locales.languages.ContentLanguageAvailability object at ...>

      >>> languagecodes = util.getAvailableLanguages()
      >>> len(languagecodes)
      147

      >>> 'de' in languagecodes
      True

      >>> languages = util.getLanguages()
      >>> len(languages)
      147

      >>> de = languages['de']
      >>> de['name']
      'German'

      >>> de['native']
      'Deutsch'

      >>> de['flag']
      '/@@/country-flags/de.gif'
    """

def testMetadataLanguageAvailability():
    """
      >>> util = queryUtility(IMetadataLanguageAvailability)
      >>> util
      <plone.i18n.locales.languages.MetadataLanguageAvailability object at ...>

      >>> languagecodes = util.getAvailableLanguages()
      >>> len(languagecodes)
      147

      >>> 'de' in languagecodes
      True

      >>> languages = util.getLanguages()
      >>> len(languages)
      147

      >>> de = languages['de']
      >>> de['name']
      'German'

      >>> de['native']
      'Deutsch'

      >>> de['flag']
      '/@@/country-flags/de.gif'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.i18n.locales.languages'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
