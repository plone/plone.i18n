import unittest


class TestAvailableCountries(unittest.TestCase):
    def setUp(self):
        from .base import setUp

        setUp()

    def tearDown(self):
        from .base import tearDown

        tearDown()

    def _makeOne(self):
        from plone.i18n.locales.interfaces import ICountryAvailability
        from zope.component import queryUtility

        return queryUtility(ICountryAvailability)

    def test_interface(self):
        from plone.i18n.locales.countries import CountryAvailability
        from plone.i18n.locales.interfaces import ICountryAvailability
        from zope.interface.verify import verifyClass

        self.assertTrue(verifyClass(ICountryAvailability, CountryAvailability))

    def test_get_available(self):
        util = self._makeOne()
        countrycodes = util.getAvailableCountries()
        self.assertTrue(len(countrycodes) > 200)
        self.assertIn("de", countrycodes)

    def test_get_countries(self):
        util = self._makeOne()
        countries = util.getCountries()
        self.assertTrue(len(countries) > 200)
        self.assertIn("de", countries)
        de = countries["de"]
        self.assertEqual(de["name"], "Germany")
        self.assertEqual(de["flag"], "countryflag/de")

    def test_get_country_listing(self):
        util = self._makeOne()
        countries = util.getCountryListing()
        self.assertTrue(len(countries) > 200)
        self.assertIn(("de", "Germany"), countries)

    def test_reservations(self):
        # our list has historically contained some reservations, which
        # aren't part of the official list. We retain those, to avoid
        # breaking content based on these
        from plone.i18n.locales.countries import _countrylist

        self.assertIn("an", _countrylist)
        self.assertIn("cs", _countrylist)
