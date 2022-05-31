from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.i18n.interfaces import ILanguageSchema
from plone.i18n.tests import base
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import ILanguage
from zope.component import getUtility


class LanguageNegotiationTestCase(base.FunctionalTestCase):
    def afterSetUp(self):
        self.basic_auth = f"{TEST_USER_NAME}:{TEST_USER_PASSWORD}"
        self.portal_path = self.portal.absolute_url(1)
        self.tool = getToolByName(self.portal, "portal_languages")
        self.settings = getUtility(IRegistry).forInterface(
            ILanguageSchema, prefix="plone"
        )
        self.settings.always_show_selector = 1
        self.settings.set_cookie_always = 1

    def checkLanguage(self, response, language):
        self.assertEqual(response.getStatus(), 200)
        cookie = response.getCookie("I18N_LANGUAGE")["value"]
        self.assertEqual(cookie, language)


class TestDefaultLanguageNegotiation(LanguageNegotiationTestCase):
    def testLanguageNegotiation(self):
        # Once PLT is installed only English is allowed as a language
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_ACCEPT_LANGUAGE": "pt"},
            handle_errors=False,
        )
        self.checkLanguage(response, "en")


class TestNoCombinedLanguageNegotiation(LanguageNegotiationTestCase):
    def afterSetUp(self):
        LanguageNegotiationTestCase.afterSetUp(self)
        # set some allowed languages and make sure we don't use combined
        # language codes
        self.settings.available_languages = ["en", "pt", "de"]
        self.settings.use_request_negotiation = 1
        self.settings.use_combined_language_codes = 0
        self.settings.display_flags = 0

    def testLanguageNegotiation(self):

        # Test simple supported codes
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_ACCEPT_LANGUAGE": "pt"},
            handle_errors=False,
        )
        self.checkLanguage(response, "pt")

        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_ACCEPT_LANGUAGE": "de"},
            handle_errors=False,
        )
        self.checkLanguage(response, "de")

        # Test combined unsupported codes, should fall back
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_ACCEPT_LANGUAGE": "pt-br"},
            handle_errors=False,
        )
        self.checkLanguage(response, "pt")


class TestCombinedLanguageNegotiation(LanguageNegotiationTestCase):
    def afterSetUp(self):
        LanguageNegotiationTestCase.afterSetUp(self)
        setRoles(self.layer["portal"], TEST_USER_ID, ["Contributor"])
        # set some allowed languages and make sure we don't use combined
        # language codes
        self.settings.use_combined_language_codes = True
        self.settings.available_languages = ["en", "pt", "de", "pt-br"]
        self.settings.use_request_negotiation = True
        self.settings.display_flags = 0

    def testLanguageNegotiation(self):

        # Test simple supported codes
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_ACCEPT_LANGUAGE": "pt"},
            handle_errors=False,
        )
        self.checkLanguage(response, "pt")

        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_ACCEPT_LANGUAGE": "de"},
            handle_errors=False,
        )
        self.checkLanguage(response, "de")

        # Test combined supported codes
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_ACCEPT_LANGUAGE": "pt-br"},
            handle_errors=False,
        )
        self.checkLanguage(response, "pt-br")

        # Test combined unsupported codes, should fall back
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_ACCEPT_LANGUAGE": "de-de"},
            handle_errors=False,
        )
        self.checkLanguage(response, "de")


class TestContentLanguageNegotiation(LanguageNegotiationTestCase):
    def afterSetUp(self):
        LanguageNegotiationTestCase.afterSetUp(self)
        setRoles(self.layer["portal"], TEST_USER_ID, ["Contributor"])
        self.settings.available_languages = ["en", "nl", "fr"]
        self.settings.use_content_negotiation = 1
        self.settings.display_flags = 0
        registry = getUtility(IRegistry)
        # disable cooking of assets because this gives unwanted
        # sideeffects in the request handling
        registry["plone.resources.development"] = True

    def testContentObject(self):
        self.layer["portal"].invokeFactory("Document", "doc")
        doc = self.layer["portal"].doc
        ILanguage(doc).set_language("nl")
        self.assertEqual(doc.Language(), "nl")
        docpath = "/".join(doc.getPhysicalPath())
        response = self.publish(
            docpath,
            self.basic_auth,
            env={"PATH_INFO": docpath},
            handle_errors=False,
        )
        self.checkLanguage(response, "nl")

    def testContentObjectVHMPortal(self):
        adding = self.app.manage_addProduct["SiteAccess"]
        adding.manage_addVirtualHostMonster("VHM")
        vhmBasePath = (
            "/VirtualHostBase/http/example.org:80/{}/"
            "VirtualHostRoot/".format(self.portal.getId())
        )
        self.layer["portal"].invokeFactory("Folder", "sub")
        sub = self.layer["portal"]["sub"]
        sub.setLanguage("nl")
        sub.invokeFactory("Document", "doc")
        doc = sub.doc
        doc.setLanguage("nl")
        self.assertEqual(doc.Language(), "nl")
        docpath = "/".join(self.portal.portal_url.getRelativeContentPath(doc))
        response = self.publish(
            vhmBasePath + docpath, self.basic_auth, handle_errors=False
        )
        self.checkLanguage(response, "nl")

    def testContentObjectVHMPortalVHSubpath(self):
        adding = self.app.manage_addProduct["SiteAccess"]
        adding.manage_addVirtualHostMonster("VHM")
        vhmBasePath = (
            "/VirtualHostBase/http/example.org:80/{}/VirtualHostRoot/"
            "_vh_one/_vh_two/".format(self.portal.getId())
        )

        self.layer["portal"].invokeFactory("Folder", "sub")
        sub = self.layer["portal"]["sub"]
        sub.setLanguage("nl")
        sub.invokeFactory("Document", "doc")
        doc = sub.doc
        doc.setLanguage("nl")
        self.assertEqual(doc.Language(), "nl")
        docpath = "/".join(self.portal.portal_url.getRelativeContentPath(doc))
        response = self.publish(
            vhmBasePath + docpath,
            self.basic_auth,
            handle_errors=False,
        )
        self.checkLanguage(response, "nl")

    def testContentObjectVHMFolder(self):
        adding = self.app.manage_addProduct["SiteAccess"]
        adding.manage_addVirtualHostMonster("VHM")

        folder_path = "/".join(self.layer["portal"].getPhysicalPath())
        vhmBasePath = "/VirtualHostBase/http/example.org:80{}/VirtualHostRoot/".format(
            folder_path
        )
        self.layer["portal"].invokeFactory("Folder", "sub")
        sub = self.layer["portal"]["sub"]
        sub.setLanguage("nl")
        sub.invokeFactory("Document", "doc")
        doc = sub.doc
        doc.setLanguage("nl")
        self.assertEqual(doc.Language(), "nl")
        docpath = "/".join(doc.getPhysicalPath())
        docpath = docpath[len(folder_path) + 1 :]

        response = self.publish(
            vhmBasePath + docpath,
            self.basic_auth,
            env={"diazo.off": "1"},
            handle_errors=False,
        )
        self.checkLanguage(response, "nl")


class TestCcTLDLanguageNegotiation(LanguageNegotiationTestCase):
    def afterSetUp(self):
        LanguageNegotiationTestCase.afterSetUp(self)
        # setRoles(self.layer['portal'], TEST_USER_ID, ['Contributor'])
        self.settings.available_languages = ["en", "nl", "fr"]
        self.settings.use_cctld_negotiation = 1
        self.settings.display_flags = 0

    def testSimpleHostname(self):
        # For a simple hostname without ccTLD the canonical language is used
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "localhost"},
            handle_errors=False,
        )
        self.checkLanguage(response, "en")

    def testIPAddress(self):
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "127.0.0.1"},
            handle_errors=False,
        )
        self.checkLanguage(response, "en")

    def testDutchDomain(self):
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "plone.nl"},
            handle_errors=False,
        )
        self.checkLanguage(response, "nl")

    def testAcceptedLanguages(self):
        # Brazil uses Portugese, which is not in the accepted languages list
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "plone.br"},
            handle_errors=False,
        )
        self.checkLanguage(response, "en")

    def testMultiLingualCountries(self):
        # Some countries refuse to pick a single language. Belgium
        # uses both Dutch and French, with a preference for Dutch.

        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "plone.be"},
            handle_errors=False,
        )
        self.checkLanguage(response, "nl")

        # If we stop allowing Dutch we should now fall back to French
        self.settings.available_languages = ["en", "fr"]
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "plone.be"},
            handle_errors=False,
        )
        self.checkLanguage(response, "fr")


class TestSubdomainLanguageNegotiation(LanguageNegotiationTestCase):
    def afterSetUp(self):
        LanguageNegotiationTestCase.afterSetUp(self)
        self.settings.available_languages = ["en", "nl", "fr"]
        self.settings.use_subdomain_negotiation = 1
        self.settings.display_flags = 0

    def testSimpleHostname(self):
        # For a simple hostname without ccTLD the canonical language is used
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "localhost"},
            handle_errors=False,
        )
        self.checkLanguage(response, "en")

    def testIPAddress(self):
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "127.0.0.1"},
            handle_errors=False,
        )
        self.checkLanguage(response, "en")

    def testDutchDomain(self):
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "nl.plone.org"},
            handle_errors=False,
        )
        self.checkLanguage(response, "nl")

    def testAcceptedLanguages(self):
        # Brazil uses Portugese, which is not in the accepted languages list
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "br.plone.org"},
            handle_errors=False,
        )
        self.checkLanguage(response, "en")

    def testMultiLingualCountries(self):
        # Some countries refuse to pick a single language. Belgium
        # uses both Dutch and French, with a preference for Dutch.

        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "be.plone.org"},
            handle_errors=False,
        )
        self.checkLanguage(response, "nl")

        # If we stop allowing Dutch we should now fall back to French
        self.settings.available_languages = ["en", "fr"]
        response = self.publish(
            self.portal_path,
            self.basic_auth,
            env={"HTTP_HOST": "be.plone.org"},
            handle_errors=False,
        )
        self.checkLanguage(response, "fr")
