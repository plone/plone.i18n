import unittest


class BaseTestCase:
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
        from plone.i18n.normalizer.adapters import UserPreferredFileNameNormalizer

        return UserPreferredFileNameNormalizer

    def test_german(self):
        norm = self._makeOne("de")
        self.assertEqual(norm.normalize("simpleandsafe"), "simpleandsafe")

        self.assertEqual(norm.normalize("text with umläut"), "text with umlaeut")

    def test_german_country(self):
        norm = self._makeOne("de-DE")
        self.assertEqual(norm.normalize("simpleandsafe"), "simpleandsafe")

        self.assertEqual(norm.normalize("text with umläut"), "text with umlaeut")

    def test_english(self):
        norm = self._makeOne("en")
        self.assertEqual(norm.normalize("simpleandsafe"), "simpleandsafe")
        self.assertEqual(norm.normalize("text with umläut"), "text with umlaut")

    def test_spanish(self):
        norm = self._makeOne("es")
        self.assertEqual(norm.normalize("simpleandsafe"), "simpleandsafe")
        self.assertEqual(norm.normalize("text with eñe"), "text with ene")


class TestUrlNormalizer(BaseTestCase, unittest.TestCase):
    def _getTargetClass(self):
        from plone.i18n.normalizer.adapters import UserPreferredURLNormalizer

        return UserPreferredURLNormalizer

    def test_german(self):
        norm = self._makeOne("de")
        self.assertEqual(norm.normalize("simpleandsafe"), "simpleandsafe")

        self.assertEqual(norm.normalize("text with umläut"), "text-with-umlaeut")

    def test_german_country(self):
        norm = self._makeOne("de-DE")
        self.assertEqual(norm.normalize("simpleandsafe"), "simpleandsafe")

        self.assertEqual(norm.normalize("text with umläut"), "text-with-umlaeut")

    def test_english(self):
        norm = self._makeOne("en")
        self.assertEqual(norm.normalize("simpleandsafe"), "simpleandsafe")

        self.assertEqual(norm.normalize("text with umläut"), "text-with-umlaut")

    def test_spanish(self):
        norm = self._makeOne("es")
        self.assertEqual(norm.normalize("simpleandsafe"), "simpleandsafe")

        self.assertEqual(norm.normalize("text with eñe"), "text-with-ene")
