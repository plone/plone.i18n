# -*- coding: UTF-8 -*-
"""
    Country tests.
"""

import doctest
from doctest import DocTestSuite
import unittest

import plone.i18n.locales
from plone.i18n.locales.interfaces import ICountryAvailability

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


def testAvailableCountries():
    """
      >>> util = queryUtility(ICountryAvailability)
      >>> util
      <plone.i18n.locales.countries.CountryAvailability object at ...>

      >>> countrycodes = util.getAvailableCountries()
      >>> len(countrycodes)
      243

      >>> u'de' in countrycodes
      True

      >>> countries = util.getCountries()
      >>> len(countries)
      243

      >>> de = countries[u'de']
      >>> de[u'name']
      u'Germany'

      >>> de[u'flag']
      u'/++resource++country-flags/de.gif'

      >>> countries = util.getCountryListing()
      >>> len(countries)
      243

      >>> (u'de', u'Germany') in countries
      True
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.i18n.locales.countries'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))
