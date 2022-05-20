from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import bbb
from plone.app.testing import FunctionalTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


# XXX: testing with dependency indirection!

class PloneI18nLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Needed to have ILanguage adapter for dx
        import plone.app.multilingual
        import plone.i18n

        self.loadZCML(package=plone.i18n)
        self.loadZCML(package=plone.app.multilingual)


PLT_FIXTURE = PloneI18nLayer()
PLT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLT_FIXTURE,), name="Plonei18nTestCase:Functional"
)


class TestCase(bbb.PloneTestCase):
    """Simple test case"""

    layer = PLT_FUNCTIONAL_TESTING


class FunctionalTestCase(TestCase):
    """Simple test case for functional tests"""
