from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.i18n.interfaces import ILanguageSchema
from plone.i18n.interfaces import ILanguageUtility
from plone.i18n.tests import base
from plone.registry.interfaces import IRegistry
from Products.CMFCore.interfaces import IDublinCore
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.utils import getToolInterface
from zope.component import getUtility
from zope.interface import alsoProvides


class TestLanguageTool(base.TestCase):
    def afterSetUp(self):
        self.ltool = getToolByName(self.portal, "portal_languages")
        setRoles(self.layer["portal"], TEST_USER_ID, ["Contributor"])
        self.settings = getUtility(IRegistry).forInterface(
            ILanguageSchema, prefix="plone"
        )

    def testLanguageSettings(self):
        defaultLanguage = "de"
        supportedLanguages = ["en", "de", "no"]
        self.settings.default_language = defaultLanguage
        self.settings.available_languages = supportedLanguages
        self.settings.use_combined_language_codes = False
        self.assertEqual(self.ltool.getDefaultLanguage(), defaultLanguage)
        self.assertEqual(self.ltool.getSupportedLanguages(), supportedLanguages)

    def testSupportedLanguages(self):
        defaultLanguage = "de"
        supportedLanguages = ["en", "de", "no"]
        self.settings.available_languages = supportedLanguages
        self.settings.default_language = defaultLanguage
        self.assertEqual(self.ltool.getSupportedLanguages(), supportedLanguages)

        self.ltool.removeSupportedLanguages(supportedLanguages)
        self.assertEqual(self.ltool.getSupportedLanguages(), [])

        for lang in supportedLanguages:
            self.ltool.addSupportedLanguage(lang)
        self.assertEqual(self.ltool.getSupportedLanguages(), supportedLanguages)

    def testDefaultLanguage(self):
        supportedLanguages = ["de", "no"]
        self.settings.available_languages = supportedLanguages
        self.ltool.setDefaultLanguage("no")
        self.assertEqual(self.ltool.getSupportedLanguages(), supportedLanguages)
        self.assertEqual(self.ltool.getDefaultLanguage(), "no")

        # default not in supported languages, should set to first supported
        self.ltool.setDefaultLanguage("nl")

        self.assertEqual(self.ltool.getSupportedLanguages(), supportedLanguages)
        self.assertEqual(self.ltool.getDefaultLanguage(), "de")

    def testAvailableLanguage(self):
        defaultLanguage = "de"
        supportedLanguages = ["en", "de", "no"]
        self.settings.available_languages = supportedLanguages
        self.ltool.setDefaultLanguage(defaultLanguage)
        availableLanguages = self.ltool.getAvailableLanguageInformation()
        for lang in availableLanguages:
            if lang in supportedLanguages:
                self.assertTrue(availableLanguages[lang]["selected"])

    def testGetContentLanguage(self):
        # tests for issue #11263
        defaultLanguage = "de"
        supportedLanguages = ["en", "de", "no"]
        self.settings.available_languages = supportedLanguages
        self.ltool.setDefaultLanguage(defaultLanguage)
        request = self.layer["request"]
        request.path = ["doc"]
        self.layer["portal"].invokeFactory("Document", "doc")
        content = self.layer["portal"]["doc"]
        content.setLanguage("de")
        alsoProvides(content, IDublinCore)
        self.ltool.getContentLanguage(request)
        self.assertEqual(self.ltool.getContentLanguage(request), "de")
        request.path = ["view", "foo.jpg", "doc"]
        self.assertEqual(self.ltool.getContentLanguage(request), "de")
        request.path = ["foo.jpg", "doc"]
        self.assertIsNone(self.ltool.getContentLanguage(request))
        request.path = ["foo", "portal_catalog"]
        self.assertIsNone(self.ltool.getContentLanguage(request))

    def testRegisterInterface(self):
        iface = getToolInterface("portal_languages")
        self.assertEqual(iface, ILanguageUtility)
