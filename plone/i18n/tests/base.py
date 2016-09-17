from plone.app import testing
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import bbb
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class PloneI18nLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        import plone.i18n
        # Needed to have ILanguage adapter for dx
        import plone.app.multilingual
        self.loadZCML(package=plone.i18n)
        self.loadZCML(package=plone.app.multilingual)

PLT_FIXTURE = PloneI18nLayer()
PLT_FUNCTIONAL_TESTING = testing.FunctionalTesting(
    bases=(PLT_FIXTURE, ), name='Plonei18nTestCase:Functional')


class TestCase(bbb.PloneTestCase):
    """Simple test case
    """
    layer = PLT_FUNCTIONAL_TESTING


class FunctionalTestCase(TestCase):
    """Simple test case for functional tests
    """
