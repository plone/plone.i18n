# -*- coding: UTF-8 -*-

import unittest

from plone.i18n.locales.interfaces import IContentLanguageAvailability
from plone.i18n.locales.interfaces import ILanguageAvailability
from plone.i18n.locales.interfaces import IMetadataLanguageAvailability

from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.interface.verify import verifyClass


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


class BaseTest(object):

    def setUp(self):
        configurationSetUp()

    def tearDown(self):
        tearDown()

    def _makeOne(self):
        raise NotImplementedError

    def test_get_available(self):
        util = self._makeOne()
        languagecodes = util.getAvailableLanguages()
        self.assertEquals(len(languagecodes), 151)
        self.assertTrue(u'de' in languagecodes)
        self.assertFalse(u'pt-br' in languagecodes)

    def test_get_available_combined(self):
        util = self._makeOne()
        languagecodes = util.getAvailableLanguages(combined=True)
        self.assertEquals(len(languagecodes), 377)
        self.assertTrue(u'de' in languagecodes)
        self.assertTrue(u'pt-br' in languagecodes)

    def test_get_languages(self):
        util = self._makeOne()
        languages = util.getLanguages()
        self.assertEquals(len(languages), 151)
        self.assertTrue(u'de' in languages)
        self.assertFalse(u'pt-br' in languages)
        de = languages[u'de']
        self.assertEquals(de[u'name'], u'German')
        self.assertEquals(de[u'native'], u'Deutsch')
        self.assertEquals(de[u'flag'], u'/++resource++country-flags/de.gif')

    def test_get_languages_combined(self):
        util = self._makeOne()
        languages = util.getLanguages(combined=True)
        self.assertEquals(len(languages), 377)
        self.assertTrue(u'de' in languages)
        self.assertTrue(u'pt-br' in languages)
        self.assertEquals(languages[u'de'][u'name'], u'German')
        self.assertEquals(languages[u'pt-br'][u'name'], u'Portuguese (Brazil)')

    def test_get_language_listing(self):
        util = self._makeOne()
        languages = util.getLanguageListing()
        self.assertEquals(len(languages), 151)
        self.assertTrue((u'de', u'German') in languages)


class TestContentLanguageAvailability(BaseTest, unittest.TestCase):

    def _makeOne(self):
        return queryUtility(IContentLanguageAvailability)

    def test_interface(self):
        from plone.i18n.locales.languages import ContentLanguageAvailability
        self.assert_(verifyClass(IContentLanguageAvailability,
                                 ContentLanguageAvailability))


class TestMetadataLanguageAvailability(BaseTest, unittest.TestCase):

    def _makeOne(self):
        return queryUtility(IMetadataLanguageAvailability)

    def test_interface(self):
        from plone.i18n.locales.languages import MetadataLanguageAvailability
        self.assert_(verifyClass(IMetadataLanguageAvailability,
                                 MetadataLanguageAvailability))


class TestInterfaces(unittest.TestCase):

    def test_interface(self):
        from plone.i18n.locales.languages import LanguageAvailability
        self.assert_(verifyClass(ILanguageAvailability, LanguageAvailability))
