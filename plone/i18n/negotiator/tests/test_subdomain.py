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


def testSubdomainNegotiator():
    """
      >>> from plone.i18n.negotiator.negotiator import Negotiator
      >>> negotiator = Negotiator()
      >>> from plone.i18n.negotiator.subdomain import SubdomainLanguage
      >>> negotiator[0] = SubdomainLanguage

      >>> from plone.i18n.locales.interfaces import ICcTLDInformation
      >>> from plone.i18n.locales.interfaces import ILanguageAvailability
      >>> from plone.i18n.locales.cctld import CcTLDInformation
      >>> from plone.i18n.locales.languages import LanguageAvailability

      >>> request = TestRequest('de.plone.org')
      >>> negotiator.getLanguage(('de', ), request) is None
      True

      >>> from zope.component import getSiteManager
      >>> lang_avail = LanguageAvailability()
      >>> cctld = CcTLDInformation()

      >>> sm = getSiteManager()
      >>> sm.registerUtility(lang_avail, ILanguageAvailability)
      >>> sm.registerUtility(cctld, ICcTLDInformation)

      >>> data = [
      ...    (('de', 'en'), None),
      ...    (('de', 'en'), ''),
      ...    (('de', 'en'), 'www.plone.org'),
      ...    (('de', 'en'), 'de.plone.org'),
      ...    (('fi', 'en'), 'fi.plone.org'),
      ...    (('pt', 'en'), 'pt.plone.org:8081'),
      ... ]

      >>> for langs, host in data:
      ...    request = TestRequest(host)
      ...    print negotiator.getLanguage(langs, request)
      None
      None
      None
      de
      fi
      pt
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
