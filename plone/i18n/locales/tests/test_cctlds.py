# -*- coding: UTF-8 -*-

import unittest

from plone.i18n.locales.interfaces import ICcTLDInformation

from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig


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


class TestCCTLD(unittest.TestCase):

    def setUp(self):
        configurationSetUp()

    def tearDown(self):
        tearDown()

    def _makeOne(self):
        return queryUtility(ICcTLDInformation)

    def test_interface(self):
        from zope.interface.verify import verifyClass
        from plone.i18n.locales.cctld import CcTLDInformation
        self.assert_(verifyClass(ICcTLDInformation, CcTLDInformation))

    def test_get_available(self):
        util = self._makeOne()
        tlds = util.getAvailableTLDs()
        self.assertEquals(len(tlds), 266)
        self.assert_(u'nl' in tlds)

    def test_get(self):
        util = self._makeOne()
        tlds = util.getTLDs()
        self.assertEquals(len(tlds), 266)

    def test_get_languages_for(self):
        util = self._makeOne()
        self.assertEquals(util.getLanguagesForTLD(u'nl'), [u'nl'])
        self.assertEquals(util.getLanguagesForTLD(u'be'), [u'nl', u'fr'])
