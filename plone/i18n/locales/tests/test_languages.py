# -*- coding: UTF-8 -*-
"""
    Languages tests.
"""

import unittest

import plone.i18n.locales
from plone.i18n.locales.interfaces import ILanguage
from plone.i18n.locales.languages import Language

import zope.app.component
import zope.app.publisher.browser

from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.app.component)()
    XMLConfig('meta.zcml', zope.app.publisher.browser)()
    XMLConfig('configure.zcml', plone.i18n.locales)()

def testLanguage():
    """
      >>> en = Language(u'en', u'English', native=u'English',
      ...               flag='/@@/country-flags/en.gif')
      >>> en.code
      u'en'
      >>> en.name
      u'English'
      >>> en.native
      u'English'
      >>> en.flag
      '/@@/country-flags/en.gif'

      >>> pt_BR = Language(u'pt-br', u'Brazilian Portuguese',
      ...                  native=unicode('Português (Brasil)', 'utf-8'),
      ...                  flag='/@@/country-flags/br.gif')
      >>> pt_BR.code
      u'pt-br'
      >>> pt_BR.native == u'Portugu\xeas (Brasil)'
      True
      >>> pt_BR.flag
      '/@@/country-flags/br.gif'
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
