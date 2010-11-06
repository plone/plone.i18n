# -*- coding: UTF-8 -*-

import unittest

from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig

from plone.i18n.locales.interfaces import ICountryAvailability


def configurationSetUp():
    setUp()
    import zope.component
    XMLConfig('meta.zcml', zope.component)()

    # BBB Zope 2.12
    try:
        import zope.browserresource
        XMLConfig('meta.zcml', zope.browserresource)()
    except ImportError:
        import zope.app.publisher.browser
        XMLConfig('meta.zcml', zope.app.publisher.browser)()

    import plone.i18n.locales
    XMLConfig('configure.zcml', plone.i18n.locales)()


class TestAvailableCountries(unittest.TestCase):

    def setUp(self):
        configurationSetUp()

    def tearDown(self):
        tearDown()

    def _makeOne(self):
        return queryUtility(ICountryAvailability)

    def test_interface(self):
        from zope.interface.verify import verifyClass
        from plone.i18n.locales.countries import CountryAvailability
        self.assert_(verifyClass(ICountryAvailability, CountryAvailability))

    def test_get_available(self):
        util = self._makeOne()
        countrycodes = util.getAvailableCountries()
        self.assertEquals(len(countrycodes), 243)
        self.assert_(u'de' in countrycodes)

    def test_get_countries(self):
        util = self._makeOne()
        countries = util.getCountries()
        self.assertEquals(len(countries), 243)
        self.assert_(u'de' in countries)
        de = countries[u'de']
        self.assertEquals(de[u'name'], u'Germany')
        self.assertEquals(de[u'flag'], u'/++resource++country-flags/de.gif')

    def test_get_country_listing(self):
        util = self._makeOne()
        countries = util.getCountryListing()
        self.assertEquals(len(countries), 243)
        self.assertTrue((u'de', u'Germany') in countries)
