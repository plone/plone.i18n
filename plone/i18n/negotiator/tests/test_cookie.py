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

    def __init__(self, cookie):
        self.cookies = {}
        self.cookies['I18N_LANGUAGE'] = cookie


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()


def testCookieNegotiator():
    """
      >>> from plone.i18n.negotiator.negotiator import Negotiator
      >>> negotiator = Negotiator()
      >>> from plone.i18n.negotiator.cookie import CookieLanguage
      >>> negotiator[0] = CookieLanguage

      >>> from plone.i18n.locales.interfaces import ILanguageAvailability
      >>> from plone.i18n.locales.languages import LanguageAvailability

      >>> from zope.component import getSiteManager
      >>> lang_avail = LanguageAvailability()

      >>> sm = getSiteManager()
      >>> sm.registerUtility(lang_avail, provided=ILanguageAvailability)

      >>> data = [
      ...    (('de', 'en'),  'de'),
      ...    (('en', 'fi'), 'fi'),
      ...    (('ca', 'pt'), 'pt_BR'),
      ... ]

      >>> for langs, cookie in data:
      ...    request = TestRequest(cookie)
      ...    negotiator.getLanguage(langs, request)
      'de'
      'fi'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
