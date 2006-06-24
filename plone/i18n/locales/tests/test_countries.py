# -*- coding: UTF-8 -*-
"""
    Country tests.
"""

import unittest

import plone.i18n.locales
from plone.i18n.locales.interfaces import ICountry
from plone.i18n.locales.countries import Country

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

def testCountry():
    """
      >>> br = Country(u'BR', u'Brazil',
      ...              flag='/@@/country-flags/br.gif')
      >>> br.code
      u'BR'
      >>> br.name
      u'Brazil'
      >>> br.flag
      '/@@/country-flags/br.gif'
    """

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.i18n.locales.countries'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
