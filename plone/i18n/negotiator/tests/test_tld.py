# -*- coding: utf-8 -*-
"""
    Negotiator tests.
"""

import unittest

import zope.component
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig

from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite


class TestRequest(dict):

    def __init__(self, host):
        self["HTTP_HOST"] = host


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()


def testTldNegotiator():
    """
      >>> from plone.i18n.negotiator.negotiator import Negotiator
      >>> negotiator = Negotiator()
      >>> from plone.i18n.negotiator.tld import TldLanguage
      >>> negotiator[0] = TldLanguage

      >>> from plone.i18n.locales.interfaces import ICcTLDInformation
      >>> from plone.i18n.locales.interfaces import ILanguageAvailability
      >>> from plone.i18n.locales.cctld import CcTLDInformation
      >>> from plone.i18n.locales.languages import LanguageAvailability

      >>> request = TestRequest('www.plone.de')
      >>> negotiator.getLanguage(('de', ), request) is None
      True

      >>> from zope.component import getSiteManager
      >>> lang_avail = LanguageAvailability()
      >>> cctld = CcTLDInformation()

      >>> sm = getSiteManager()
      >>> sm.registerUtility(lang_avail, provided=ILanguageAvailability)
      >>> sm.registerUtility(cctld, provided=ICcTLDInformation)

      >>> data = [
      ...    (('de', 'en'),  'www.plone.org'),
      ...    (('en', 'fi'), 'www.plone.fi'),
      ...    (('ca', 'pt'), 'www.plone.pt'),
      ...    (('ca', 'pt'), 'www.plone.pt:8081'),
      ... ]

      >>> for langs, host in data:
      ...    request = TestRequest(host)
      ...    negotiator.getLanguage(langs, request)
      'fi'
      'pt'
      'pt'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
