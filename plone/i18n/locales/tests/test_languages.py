# -*- coding: UTF-8 -*-

import unittest


class TestInterfaces(unittest.TestCase):

    def test_interface(self):
        from zope.interface.verify import verifyClass
        from plone.i18n.locales.interfaces import ILanguageAvailability
        from plone.i18n.locales.languages import LanguageAvailability
        self.assert_(verifyClass(ILanguageAvailability, LanguageAvailability))


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
        self.assertTrue(u'de' in languagecodes)
        self.assertFalse(u'pt-br' in languagecodes)

    def test_get_available_combined(self):
        util = self._makeOne()
        languagecodes = util.getAvailableLanguages(combined=True)
        self.assertTrue(len(languagecodes) > 300)
        self.assertTrue(u'de' in languagecodes)
        self.assertTrue(u'pt-br' in languagecodes)

    def test_get_languages(self):
        util = self._makeOne()
        languages = util.getLanguages()
        self.assertTrue(len(languages) > 100)
        self.assertTrue(u'de' in languages)
        self.assertFalse(u'pt-br' in languages)
        de = languages[u'de']
        self.assertEquals(de[u'name'], u'German')
        self.assertEquals(de[u'native'], u'Deutsch')
        self.assertEquals(de[u'flag'], u'/++resource++country-flags/de.gif')

    def test_get_languages_combined(self):
        util = self._makeOne()
        languages = util.getLanguages(combined=True)
        self.assertTrue(len(languages) > 300)
        self.assertTrue(u'de' in languages)
        self.assertTrue(u'pt-br' in languages)
        self.assertEquals(languages[u'de'][u'name'], u'German')
        self.assertEquals(languages[u'pt-br'][u'name'], u'Portuguese (Brazil)')

    def test_get_language_listing(self):
        util = self._makeOne()
        languages = util.getLanguageListing()
        self.assertTrue(len(languages) > 100)
        self.assertTrue((u'de', u'German') in languages)


class TestContentLanguageAvailability(BaseTestCase, unittest.TestCase):

    def _makeOne(self):
        from zope.component import queryUtility
        from plone.i18n.locales.interfaces import IContentLanguageAvailability
        return queryUtility(IContentLanguageAvailability)

    def test_interface(self):
        from plone.i18n.locales.interfaces import IContentLanguageAvailability
        from plone.i18n.locales.languages import ContentLanguageAvailability
        self.assert_(self._verify(IContentLanguageAvailability,
                                  ContentLanguageAvailability))


class TestMetadataLanguageAvailability(BaseTestCase, unittest.TestCase):

    def _makeOne(self):
        from zope.component import queryUtility
        from plone.i18n.locales.interfaces import IMetadataLanguageAvailability
        return queryUtility(IMetadataLanguageAvailability)

    def test_interface(self):
        from plone.i18n.locales.interfaces import IMetadataLanguageAvailability
        from plone.i18n.locales.languages import MetadataLanguageAvailability
        self.assert_(self._verify(IMetadataLanguageAvailability,
                                  MetadataLanguageAvailability))
