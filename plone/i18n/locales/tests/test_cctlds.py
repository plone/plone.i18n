# -*- coding: UTF-8 -*-
"""
    ccTLD tests.
"""

import unittest

import plone.i18n.locales
from plone.i18n.locales.interfaces import ICcTLDInformation

import zope.app.publisher.browser
import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('meta.zcml', zope.app.publisher.browser)()
    XMLConfig('configure.zcml', plone.i18n.locales)()

def testccTLDs():
    """
      >>> util = queryUtility(ICcTLDInformation)
      >>> util
      <plone.i18n.locales.cctld.CcTLDInformation object at ...>

      >>> tlds = util.getAvailableTLDs()
      >>> len(tlds)
      266

      >>> u'nl' in tlds
      True

      >>> tlds = util.getTLDs()
      >>> len(tlds)
      266

      >>> nl = tlds[u'nl']
      >>> nl
      [u'nl']

      >>> be = tlds[u'be']
      >>> be
      [u'nl', u'fr']
    """

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.i18n.locales.cctld'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
