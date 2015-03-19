from plone.app.testing import bbb
from plone.app import testing
from plone.testing import z2


class PloneTestCaseFixture(bbb.PloneTestCaseFixture):

    defaultBases = (bbb.PTC_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        import plone.i18n
        self.loadZCML(package=plone.i18n)

PLT_FIXTURE = PloneTestCaseFixture()
PLT_FUNCTIONAL_TESTING = testing.FunctionalTesting(
    bases=(PLT_FIXTURE, ), name='Plonei18nTestCase:Functional')


class TestCase(bbb.PloneTestCase):
    """Simple test case
    """
    layer = PLT_FUNCTIONAL_TESTING


class FunctionalTestCase(TestCase):
    """Simple test case for functional tests
    """