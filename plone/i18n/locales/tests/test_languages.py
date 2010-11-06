# -*- coding: UTF-8 -*-
"""
    Languages tests.
"""

import doctest
from doctest import DocTestSuite
import unittest

import plone.i18n.locales
from plone.i18n.locales.interfaces import IContentLanguageAvailability
from plone.i18n.locales.interfaces import IMetadataLanguageAvailability

import zope.app.publisher.browser
import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig


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
      151

      >>> u'de' in languagecodes
      True

      >>> languagecodes = util.getAvailableLanguages(combined=True)
      >>> len(languagecodes)
      377

      >>> u'pt-br' in languagecodes
      True

      >>> languages = util.getLanguages()
      >>> len(languages)
      151

      >>> de = languages[u'de']
      >>> de[u'name']
      u'German'

      >>> de[u'native']
      u'Deutsch'

      >>> de[u'flag']
      u'/++resource++country-flags/de.gif'

      >>> languages = util.getLanguageListing()
      >>> len(languages)
      151

      >>> (u'de', u'German') in languages
      True

      >>> languages = util.getLanguages(combined=True)
      >>> len(languages)
      377

      >>> pt_BR = languages[u'pt-br']
      >>> pt_BR[u'name']
      u'Portuguese (Brazil)'
    """


def testMetadataLanguageAvailability():
    """
      >>> util = queryUtility(IMetadataLanguageAvailability)
      >>> util
      <plone.i18n.locales.languages.MetadataLanguageAvailability object at ...>

      >>> languagecodes = util.getAvailableLanguages()
      >>> len(languagecodes)
      151

      >>> u'de' in languagecodes
      True

      >>> languagecodes = util.getAvailableLanguages(combined=True)
      >>> len(languagecodes)
      377

      >>> u'pt-br' in languagecodes
      True

      >>> languages = util.getLanguages()
      >>> len(languages)
      151

      >>> de = languages[u'de']
      >>> de[u'name']
      u'German'

      >>> de[u'native']
      u'Deutsch'

      >>> de[u'flag']
      u'/++resource++country-flags/de.gif'

      >>> languages = util.getLanguageListing()
      >>> len(languages)
      151

      >>> (u'de', u'German') in languages
      True

      >>> languages = util.getLanguageListing(combined=True)
      >>> len(languages)
      377

      >>> (u'pt-br', u'Portuguese (Brazil)') in languages
      True

      >>> languages = util.getLanguageListing(combined=True)
      >>> len(languages)
      377

      >>> (u'pt-br', u'Portuguese (Brazil)') in languages
      True

      >>> languages = util.getLanguages(combined=True)
      >>> len(languages)
      377

      >>> pt_BR = languages[u'pt-br']
      >>> pt_BR[u'name']
      u'Portuguese (Brazil)'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.i18n.locales.languages'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))
