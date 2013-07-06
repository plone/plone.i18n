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

    def test_german_country(self):
        norm = self._makeOne('de-DE')
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

    def test_spanish(self):
        norm = self._makeOne('es')
        self.assertEquals(norm.normalize(u'simpleandsafe'),
                          'simpleandsafe')
        self.assertEquals(norm.normalize(u'text with eñe'),
                          u'text with ene')


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

    def test_german_country(self):
        norm = self._makeOne('de-DE')
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

    def test_spanish(self):
        norm = self._makeOne('es')
        self.assertEquals(norm.normalize(u'simpleandsafe'),
                          u'simpleandsafe')

        self.assertEquals(norm.normalize(u'text with eñe'),
                          u'text-with-ene')

    def test_chinese(self):
        norm = self._makeOne('zh')
        self.assertEquals(norm.normalize(u'中国汉字'),
                          u'zhong-guo-han-zi')

        self.assertEquals(norm.normalize(u'english + 简体'),
                          u'english-jian-ti')

    def test_chinese_tw(self):
        norm = self._makeOne('zh-tw')
        self.assertEquals(norm.normalize(u'正體中文'),
                          u'zheng-ti-zhong-wen')

        self.assertEquals(norm.normalize(u'english + 正體'),
                          u'english-zheng-ti')
