# -*- coding: UTF-8 -*-

import unittest


class TestInterfaces(unittest.TestCase):
    def test_interface(self):
        from plone.i18n.locales.interfaces import ILanguageAvailability
        from plone.i18n.locales.languages import LanguageAvailability
        from zope.interface.verify import verifyClass

        self.assert_(verifyClass(ILanguageAvailability, LanguageAvailability))


class TestDeprecatedLanguages(unittest.TestCase):
    def test_deprecated(self):
        # make sure we retain deprecated language codes, as we don't
        # want to break existing content based on it
        from plone.i18n.locales.languages import _languagelist

        self.assertIn(u"mo", _languagelist)
        self.assertIn(u"sh", _languagelist)


class BaseTestCase(object):
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
        self.assertIn(u"de", languagecodes)
        self.assertNotIn(u"pt-br", languagecodes)

    def test_get_available_combined(self):
        util = self._makeOne()
        languagecodes = util.getAvailableLanguages(combined=True)
        self.assertTrue(len(languagecodes) > 300)
        self.assertIn(u"de", languagecodes)
        self.assertIn(u"pt-br", languagecodes)

    def test_get_languages(self):
        util = self._makeOne()
        languages = util.getLanguages()
        self.assertTrue(len(languages) > 100)
        self.assertIn(u"de", languages)
        self.assertNotIn(u"pt-br", languages)
        de = languages[u"de"]
        self.assertEqual(de[u"name"], u"German")
        self.assertEqual(de[u"native"], u"Deutsch")
        self.assertEqual(de[u"flag"], u"/++resource++country-flags/de.gif")

    def test_get_languages_combined(self):
        util = self._makeOne()
        languages = util.getLanguages(combined=True)
        self.assertTrue(len(languages) > 300)
        self.assertIn(u"de", languages)
        self.assertIn(u"pt-br", languages)
        self.assertEqual(languages[u"de"][u"name"], u"German")
        self.assertEqual(languages[u"pt-br"][u"name"], u"Portuguese (Brazil)")

    def test_get_language_listing(self):
        util = self._makeOne()
        languages = util.getLanguageListing()
        self.assertTrue(len(languages) > 100)
        self.assertIn((u"de", u"German"), languages)


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
