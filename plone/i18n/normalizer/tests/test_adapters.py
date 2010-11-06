# -*- coding: utf-8 -*-

import unittest


class BaseTestCase(object):

    def setUp(self):
        from .base import setUp
        setUp()

    def tearDown(self):
        from .base import tearDown
        tearDown()

    def _getTargetClass(self):
        raise NotImplementedError

    def _makeOne(self, lang):
        from zope.publisher.browser import TestRequest
        request = TestRequest(environ=dict(HTTP_ACCEPT_LANGUAGE=lang))
        return self._getTargetClass()(request)


class TestFileNameNormalizer(BaseTestCase, unittest.TestCase):

    def _getTargetClass(self):
        from plone.i18n.normalizer.adapters import \
            UserPreferredFileNameNormalizer
        return UserPreferredFileNameNormalizer

    def test_german(self):
        norm = self._makeOne('de')
        self.assertEquals(norm.normalize(u'simpleandsafe'),
                          u'simpleandsafe')

        self.assertEquals(norm.normalize(u'text with umläut'),
                          u'text with umlaeut')

    def test_english(self):
        norm = self._makeOne('en')
        self.assertEquals(norm.normalize(u'simpleandsafe'),
                          u'simpleandsafe')

        self.assertEquals(norm.normalize(u'text with umläut'),
                          u'text with umlaut')


class TestUrlNormalizer(BaseTestCase, unittest.TestCase):

    def _getTargetClass(self):
        from plone.i18n.normalizer.adapters import UserPreferredURLNormalizer
        return UserPreferredURLNormalizer

    def test_german(self):
        norm = self._makeOne('de')
        self.assertEquals(norm.normalize(u'simpleandsafe'),
                          u'simpleandsafe')

        self.assertEquals(norm.normalize(u'text with umläut'),
                          u'text-with-umlaeut')

    def test_english(self):
        norm = self._makeOne('en')
        self.assertEquals(norm.normalize(u'simpleandsafe'),
                          u'simpleandsafe')

        self.assertEquals(norm.normalize(u'text with umläut'),
                          u'text-with-umlaut')
