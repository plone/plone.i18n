import unittest


class TestInterfaces(unittest.TestCase):
    def test_interface(self):
        from plone.i18n.locales.interfaces import ILanguageAvailability
        from plone.i18n.locales.languages import LanguageAvailability
        from zope.interface.verify import verifyClass

        self.assertTrue(verifyClass(ILanguageAvailability, LanguageAvailability))


class TestDeprecatedLanguages(unittest.TestCase):
    def test_deprecated(self):
        # make sure we retain deprecated language codes, as we don't
        # want to break existing content based on it
        from plone.i18n.locales.languages import _languagelist

        self.assertIn("mo", _languagelist)
        self.assertIn("sh", _languagelist)


class BaseTestCase:
    def setUp(self):
        from .base import setUp

        setUp()

    def tearDown(self):
        from .base import tearDown

        tearDown()

    def _makeOne(self):
        raise NotImplementedError

    def _verify(self, interface, klass):
        from zope.interface.verify import verifyClass

        return verifyClass(interface, klass)

    def test_get_available(self):
        util = self._makeOne()
        languagecodes = util.getAvailableLanguages()
        self.assertTrue(len(languagecodes) > 100)
        self.assertIn("de", languagecodes)
        self.assertNotIn("pt-br", languagecodes)

    def test_get_available_combined(self):
        util = self._makeOne()
        languagecodes = util.getAvailableLanguages(combined=True)
        self.assertTrue(len(languagecodes) > 300)
        self.assertIn("de", languagecodes)
        self.assertIn("pt-br", languagecodes)

    def test_get_languages(self):
        util = self._makeOne()
        languages = util.getLanguages()
        self.assertTrue(len(languages) > 100)
        self.assertIn("de", languages)
        self.assertNotIn("pt-br", languages)
        de = languages["de"]
        self.assertEqual(de["name"], "German")
        self.assertEqual(de["native"], "Deutsch")
        self.assertEqual(de["flag"], "countryflag/de")

    def test_get_languages_combined(self):
        util = self._makeOne()
        languages = util.getLanguages(combined=True)
        self.assertTrue(len(languages) > 300)
        self.assertIn("de", languages)
        self.assertIn("pt-br", languages)
        self.assertEqual(languages["de"]["name"], "German")
        self.assertEqual(languages["pt-br"]["name"], "Portuguese (Brazil)")

    def test_get_language_listing(self):
        util = self._makeOne()
        languages = util.getLanguageListing()
        self.assertTrue(len(languages) > 100)
        self.assertIn(("de", "German"), languages)


class TestContentLanguageAvailability(BaseTestCase, unittest.TestCase):
    def _makeOne(self):
        from plone.i18n.locales.interfaces import IContentLanguageAvailability
        from zope.component import queryUtility

        return queryUtility(IContentLanguageAvailability)

    def test_interface(self):
        from plone.i18n.locales.interfaces import IContentLanguageAvailability
        from plone.i18n.locales.languages import ContentLanguageAvailability

        self.assertTrue(
            self._verify(IContentLanguageAvailability, ContentLanguageAvailability)
        )


class TestMetadataLanguageAvailability(BaseTestCase, unittest.TestCase):
    def _makeOne(self):
        from plone.i18n.locales.interfaces import IMetadataLanguageAvailability
        from zope.component import queryUtility

        return queryUtility(IMetadataLanguageAvailability)

    def test_interface(self):
        from plone.i18n.locales.interfaces import IMetadataLanguageAvailability
        from plone.i18n.locales.languages import MetadataLanguageAvailability

        self.assertTrue(
            self._verify(IMetadataLanguageAvailability, MetadataLanguageAvailability)
        )
