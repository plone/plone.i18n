import unittest


class TestCCTLD(unittest.TestCase):
    def setUp(self):
        from .base import setUp

        setUp()

    def tearDown(self):
        from .base import tearDown

        tearDown()

    def _makeOne(self):
        from plone.i18n.locales.interfaces import ICcTLDInformation
        from zope.component import queryUtility

        return queryUtility(ICcTLDInformation)

    def test_interface(self):
        from plone.i18n.locales.cctld import CcTLDInformation
        from plone.i18n.locales.interfaces import ICcTLDInformation
        from zope.interface.verify import verifyClass

        self.assertTrue(verifyClass(ICcTLDInformation, CcTLDInformation))

    def test_get_available(self):
        util = self._makeOne()
        tlds = util.getAvailableTLDs()
        self.assertTrue(len(tlds) > 200)
        self.assertIn("nl", tlds)

    def test_get(self):
        util = self._makeOne()
        tlds = util.getTLDs()
        self.assertTrue(len(tlds) > 200)

    def test_get_languages_for(self):
        util = self._makeOne()
        self.assertEqual(util.getLanguagesForTLD("nl"), ["nl"])
        self.assertEqual(util.getLanguagesForTLD("be"), ["nl", "fr"])
