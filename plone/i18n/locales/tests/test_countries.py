# -*- coding: UTF-8 -*-

import unittest


class TestAvailableCountries(unittest.TestCase):
    def setUp(self):
        from .base import setUp

        setUp()

    def tearDown(self):
        from .base import tearDown

        tearDown()

    def _makeOne(self):
        from zope.component import queryUtility
        from plone.i18n.locales.interfaces import ICountryAvailability

        return queryUtility(ICountryAvailability)

    def test_interface(self):
        from zope.interface.verify import verifyClass
        from plone.i18n.locales.interfaces import ICountryAvailability
        from plone.i18n.locales.countries import CountryAvailability

        self.assertTrue(verifyClass(ICountryAvailability, CountryAvailability))

    def test_get_available(self):
        util = self._makeOne()
        countrycodes = util.getAvailableCountries()
        self.assertTrue(len(countrycodes) > 200)
        self.assertIn(u"de", countrycodes)

    def test_get_countries(self):
        util = self._makeOne()
        countries = util.getCountries()
        self.assertTrue(len(countries) > 200)
        self.assert_(u"de" in countries)
        de = countries[u"de"]
        self.assertEqual(de[u"name"], u"Germany")
        self.assertEqual(de[u"flag"], u"/++resource++country-flags/de.gif")

    def test_get_country_listing(self):
        util = self._makeOne()
        countries = util.getCountryListing()
        self.assertTrue(len(countries) > 200)
        self.assertIn((u"de", u"Germany"), countries)

    def test_reservations(self):
        # our list has historically contained some reservations, which
        # aren't part of the official list. We retain those, to avoid
        # breaking content based on these
        from plone.i18n.locales.countries import _countrylist

        self.assertIn(u"an", _countrylist)
        self.assertIn(u"cs", _countrylist)
