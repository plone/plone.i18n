# -*- coding: UTF-8 -*-

import unittest


class TestCCTLD(unittest.TestCase):

    def setUp(self):
        from .base import setUp
        setUp()

    def tearDown(self):
        from .base import tearDown
        tearDown()

    def _makeOne(self):
        from plone.i18n.locales.interfaces import ICcTLDInformation
        from zope.component import queryUtility
        return queryUtility(ICcTLDInformation)

    def test_interface(self):
        from zope.interface.verify import verifyClass
        from plone.i18n.locales.interfaces import ICcTLDInformation
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
