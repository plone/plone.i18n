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

    def __init__(self, pathlist):
        self["TraversalRequestNameStack"] = pathlist


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()


def testPathNegotiator():
    """
      >>> from plone.i18n.negotiator.negotiator import Negotiator
      >>> negotiator = Negotiator()
      >>> from plone.i18n.negotiator.path import PathLanguage
      >>> negotiator[0] = PathLanguage

      >>> from plone.i18n.locales.interfaces import ILanguageAvailability
      >>> from plone.i18n.locales.languages import LanguageAvailability

      >>> from zope.component import getSiteManager
      >>> lang_avail = LanguageAvailability()

      >>> sm = getSiteManager()
      >>> sm.registerUtility(lang_avail, provided=ILanguageAvailability)

      >>> data = [
      ...    (('de', 'en'),  ['portal', 'de', 'folder', 'object']),
      ...    (('en', 'fi'), ['portal', 'en-us', 'fi', 'folder', 'object']),
      ...    (('ca', 'pt'), ['portal', 'ca', 'folder', 'object']),
      ... ]

      >>> for langs, path in data:
      ...    request = TestRequest(path)
      ...    negotiator.getLanguage(langs, request)
      'de'
      'fi'
      'ca'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
