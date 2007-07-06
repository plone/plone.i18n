# -*- coding: UTF-8 -*-
"""
    Negotiator tests.
"""

import unittest

import zope.component
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.i18n.interfaces import IUserPreferredLanguages
from zope.interface import implements

from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.i18n.negotiator.negotiator import Negotiator


class Env(object):
    implements(IUserPreferredLanguages)

    def __init__(self, langs=()):
        self.langs = langs

    def getPreferredLanguages(self):
        return self.langs


class TestRequest(dict):

    def __init__(self, languages):
        self["HTTP_ACCEPT_LANGUAGE"] = languages


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()


def testDefaultNegotiator():
    """
      >>> negotiator = Negotiator()

      >>> _cases = (
      ...    (('ca-es',), ('ca_ES', ), 'ca_ES'),
      ...    (('en','de'), ('en','de','fr'),  'en'),
      ...    (('en'),      ('it','de','fr'),  None),
      ...    (('pt-br','de'), ('pt_BR','de','fr'),  'pt_BR'),
      ...    (('pt-br','en'), ('pt', 'en', 'fr'),  'pt'),
      ...    (('pt-br','en-us', 'de'), ('de', 'en', 'fr'),  'en'),
      ...    )

      >>> for user_pref_langs, obj_langs, expected in _cases:
      ...     env = Env(user_pref_langs)
      ...     negotiator.getLanguage(obj_langs, env) is None
      True
      True
      True
      True
      True
      True
    """


def testBrowserNegotiator():
    """
      >>> negotiator = Negotiator()
      >>> from zope.publisher.browser import BrowserLanguages
      >>> negotiator[0] = BrowserLanguages

      >>> data = [
      ...    (('da', 'en'),  ('da, en, pt')),
      ...    (('en-us', 'da'), ('da, en;q=.9, en-gb;q=1.0, en-us')),
      ...    (('en', 'pt-br'), ('pt_BR; q=0.6, pt_PT; q = .7, en-gb')),
      ...    (('en-gb', 'en-us'), ('en-us, en_GB;q=0.9, en, pt_BR; q=1.0')),
      ...    (('ro', 'fr'), ('ro,en-us;q=0.8,es;q=0.5,fr;q=0.3')),
      ...    (('es', 'ro'), ('ro,en-us;q=0,es;q=0.5,fr;q=0,ru;q=1,it'))
      ...    ]

      >>> for langs, req in data:
      ...    request = TestRequest(req)
      ...    negotiator.getLanguage(langs, request)
      'da'
      'da'
      'en'
      'en-us'
      'ro'
      'ro'
    """


def testAvailableLanguagesBrowserNegotiator():
    """
      >>> negotiator = Negotiator()
      >>> from zope.publisher.browser import BrowserLanguages
      >>> negotiator[0] = BrowserLanguages

      >>> from plone.i18n.locales.interfaces import IContentLanguageAvailability
      >>> from plone.i18n.locales.languages import LanguageAvailability

      >>> from zope.component import getSiteManager
      >>> lang_avail = LanguageAvailability()

      >>> sm = getSiteManager()
      >>> sm.registerUtility(lang_avail, provided=IContentLanguageAvailability)

      >>> data = [
      ...    (('xy', ),  ('da, en, pt')),
      ...    (('xy', ), ('da, en;q=.9, en-gb;q=1.0, en-us')),
      ...    (('xy', ), ('pt_BR; q=0.6, pt_PT; q = .7, en-gb')),
      ... ]

      >>> for langs, req in data:
      ...    request = TestRequest(req)
      ...    negotiator.getLanguage(langs, request)
      'da'
      'da'
      'en'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
