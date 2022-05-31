from ..interfaces import IFileNameNormalizer
from ..interfaces import IIDNormalizer
from ..interfaces import IURLNormalizer
from .base import setUp as configurationSetUp
from .base import tearDown
from doctest import DocTestSuite
from zope.component import queryUtility

import doctest
import unittest


def testIDNormalizer():
    """
    >>> util = queryUtility(IIDNormalizer)
    >>> util
    <plone.i18n.normalizer.IDNormalizer object at ...>

    >>> util.normalize('simpleandsafe')
    'simpleandsafe'

    >>> util.normalize(' Whitespace and capital Letters  ')
    'whitespace-and-capital-letters'

    >>> util.normalize(u">here's another!")
    'heres-another'

    >>> util.normalize(u">>>here'!--s yet another!!!")
    'here-s-yet-another'

    >>> util.normalize("umläut.doc")
    'umlaut-doc'

    >>> from plone.i18n.normalizer import MAX_LENGTH

    >>> testString = u"thissentenceiswaytolongtobecroppedwithoutcuttedbythenormalizemethodbecauseithasnoplacetocrop"
    >>> util.normalize(testString)
    'thissentenceiswaytolongtobecroppedwithoutcuttedbyt'
    >>> len(util.normalize(testString)) == MAX_LENGTH
    True

    >>> testString = u"thissentenceisacropped-by-the-normalize-method-because-it-has-many-places-to-crop"
    >>> util.normalize(testString)
    'thissentenceisacropped-by-the-normalize-method'
    >>> len(util.normalize(testString)) <= MAX_LENGTH
    True

    >>> testString = u"this-sentence-is-way-to-long-but-can-be-cropped-by-the-normalize-method-because-it-has-many-places-to-crop"
    >>> util.normalize(testString)
    'this-sentence-is-way-to-long-but-can-be-cropped-by'
    >>> len(util.normalize(testString)) <= MAX_LENGTH
    True

    >>> util.normalize(u"rest `n` peace")
    'rest-n-peace'

    >>> util.normalize(u"short-hello-version", max_length=10)
    'short'

    >>> util.normalize(u"short-hello-version", max_length=15)
    'short-hello'
    """


def testLocaleAwareIDNormalizer():
    """
      >>> util = queryUtility(IIDNormalizer)
      >>> util
      <plone.i18n.normalizer.IDNormalizer object at ...>

    Register the German file name normalizer as an id normalizer as well, to
    test the locale-aware id normalization logic:

      >>> de_util = queryUtility(IFileNameNormalizer, name='de')
      >>> from zope.component import getSiteManager
      >>> sm = getSiteManager()
      >>> sm.registerUtility(de_util, IIDNormalizer, name='de')

      >>> util.normalize('simpleandsafe', locale='de')
      'simpleandsafe'

      >>> util.normalize('text with umläut', locale='de')
      'text-with-umlaeut'

    Make sure we get the de normalizer as there's no special one for de-DE
    registered.

      >>> util.normalize('text with umläut', locale='de-DE')
      'text-with-umlaeut'

      >>> util.normalize('simpleandsafe', locale='pt-BR')
      'simpleandsafe'

      >>> util.normalize('simpleandsafe', locale='sr@Latn')
      'simpleandsafe'

      >>> util.normalize(u"short-hello-version", locale='de-DE', max_length=10)
      'short'

      >>> util.normalize(u"short-hello-version", locale='de-DE', max_length=15)
      'short-hello'

    Make sure we also handle POSIX-format locale identifiers,
    for backwards-compatibility with an earlier version of plone.i18n.

      >>> util.normalize('text with umläut', locale='de_DE')
      'text-with-umlaeut'

    """


def testFileNameNormalizer():
    """
    >>> util = queryUtility(IFileNameNormalizer)
    >>> util
    <plone.i18n.normalizer.FileNameNormalizer object at ...>

    >>> util.normalize('simpleandsafe')
    'simpleandsafe'

    >>> util.normalize(' Whitespace and capital Letters  ')
    'Whitespace and capital Letters'

    >>> util.normalize(u">here's another!")
    'heres another'

    >>> util.normalize(u">>>here'!--s yet another!!!")
    'here-s yet another'

    >>> util.normalize(u"{[(me too)]}")
    'me too'

    >>> util.normalize("pseudo_filename,pot,#1.doc")
    'pseudo_filename-pot-#1.doc'

    >>> util.normalize("umläut.doc")
    'umlaut.doc'

    >>> len(util.normalize('aa' * 2000))
    1023

    >>> util.normalize(u"rest `n` peace")
    'rest -n- peace'

    >>> util.normalize(u"short-hello-version", max_length=10)
    'short'

    >>> util.normalize(u"_some_cameras_are_evil")
    'some_cameras_are_evil'

    >>> util.normalize(u"____my_new_file")
    'my_new_file'
    """


def testLocaleAwareFileNameNormalizer():
    """
      >>> util = queryUtility(IFileNameNormalizer)
      >>> util
      <plone.i18n.normalizer.FileNameNormalizer object at ...>

      >>> util.normalize('simpleandsafe', locale='de')
      'simpleandsafe'

      >>> util.normalize('text with umläut', locale='de')
      'text with umlaeut'

    Make sure we get the de normalizer as there's no special one for de-DE
    registered.

      >>> util.normalize('text with umläut', locale='de-DE')
      'text with umlaeut'

      >>> util.normalize('simpleandsafe', locale='pt-BR')
      'simpleandsafe'

      >>> util.normalize('simpleandsafe', locale='sr@Latn')
      'simpleandsafe'

      >>> util.normalize(u"short-hello-version", locale='de-DE', max_length=10)
      'short'

      >>> util.normalize(u"_some_cameras_are_evil")
      'some_cameras_are_evil'

    Make sure we also handle POSIX-format locale identifiers,
    for backwards-compatibility with an earlier version of plone.i18n.

      >>> util.normalize('text with umläut', locale='de_DE')
      'text with umlaeut'

    """


def testURLNormalizer():
    """
    >>> util = queryUtility(IURLNormalizer)
    >>> util
    <plone.i18n.normalizer.URLNormalizer object at ...>

    >>> util.normalize('simpleandsafe')
    'simpleandsafe'

    >>> util.normalize(' Whitespace and capital Letters  ')
    'whitespace-and-capital-letters'

    >>> util.normalize(u">here's another!")
    'heres-another'

    >>> util.normalize(u">>>here'!--s yet another!!!")
    'here-s-yet-another'

    >>> util.normalize(u"Doe, Joe")
    'doe-joe'

    >>> util.normalize("umläut.doc")
    'umlaut.doc'

    >>> util.normalize('quote "this"!')
    'quote-this'

    >>> util.normalize("quote 'this'!")
    'quote-this'

    >>> util.normalize("I'm not a FILE.txt")
    'im-not-a-file.txt'

    >>> util.normalize("I'm a big file.TXT")
    'im-a-big-file.txt'

    >>> util.normalize(u"rest `n` peace")
    'rest-n-peace'

    >>> len(util.normalize('aa' * 2000))
    255

    >>> util.normalize(u"short-hello-version", max_length=10)
    'short'

    Leading underscores are forbidden by zope, so this
    normalizer should strip it
    >>> util.normalize('_awesome.txt')
    'awesome.txt'
    """


def testLocaleAwareURLNormalizer():
    """
      >>> util = queryUtility(IURLNormalizer)
      >>> util
      <plone.i18n.normalizer.URLNormalizer object at ...>

      >>> util.normalize('simpleandsafe', locale='de')
      'simpleandsafe'

      >>> util.normalize('text with umläut', locale='de')
      'text-with-umlaeut'

    Make sure we get the de normalizer as there's no special one for de-DE
    registered.

      >>> util.normalize('text with umläut', locale='de-DE')
      'text-with-umlaeut'

      >>> util.normalize('simpleandsafe', locale='pt-BR')
      'simpleandsafe'

      >>> util.normalize('simpleandsafe', locale='sr@Latn')
      'simpleandsafe'

      >>> util.normalize(u"short-hello-version", locale='de-DE', max_length=10)
      'short'

    Make sure we also handle POSIX-format locale identifiers,
    for backwards-compatibility with an earlier version of plone.i18n.

      >>> util.normalize('text with umläut', locale='de_DE')
      'text-with-umlaeut'

    """


def test_suite():
    return unittest.TestSuite(
        (
            DocTestSuite("plone.i18n.normalizer"),
            DocTestSuite("plone.i18n.normalizer.base"),
            DocTestSuite("plone.i18n.normalizer.de"),
            DocTestSuite("plone.i18n.normalizer.el"),
            DocTestSuite("plone.i18n.normalizer.fr"),
            DocTestSuite("plone.i18n.normalizer.ja"),
            DocTestSuite("plone.i18n.normalizer.pl"),
            DocTestSuite("plone.i18n.normalizer.ru"),
            DocTestSuite("plone.i18n.normalizer.tr"),
            DocTestSuite("plone.i18n.normalizer.bg"),
            DocTestSuite("plone.i18n.normalizer.uk"),
            DocTestSuite("plone.i18n.normalizer.es"),
            DocTestSuite(
                setUp=configurationSetUp,
                tearDown=tearDown,
                optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
            ),
        )
    )
