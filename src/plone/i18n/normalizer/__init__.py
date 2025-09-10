from .base import baseNormalize
from .interfaces import IFileNameNormalizer
from .interfaces import IIDNormalizer
from .interfaces import IURLNormalizer
from zope.component import queryUtility
from zope.interface import implementer

import re


# Define and compile static regexes
FILENAME_REGEX = re.compile(r"^(.+)\.(\w{,4})$")
IGNORE_REGEX = re.compile(r"['\"]")
NON_WORD_REGEX = re.compile(r"[\W\-]+")
DANGEROUS_CHARS_REGEX = re.compile(r"[!$%&()*+,/:;<=>?@\\^{|}\[\]~`]+")
URL_DANGEROUS_CHARS_REGEX = re.compile(r"[!#$%&()*+,/:;<=>?@\\^{|}\[\]~`]+")
MULTIPLE_DASHES_REGEX = re.compile(r"\-+")
EXTRA_DASHES_REGEX = re.compile(r"(^\-+)|(\-+$)")
UNDERSCORE_START_REGEX = re.compile(r"(^_+)(.*)$")
LOCALE_SPLIT_REGEX = re.compile(r"[_-]")
# Define static constraints
MAX_LENGTH = 50
MAX_FILENAME_LENGTH = 1023
MAX_URL_LENGTH = 255


def cropName(base, maxLength=MAX_LENGTH):
    baseLength = len(base)

    index = baseLength
    while index > maxLength:
        index = base.rfind("-", 0, index)

    if index == -1 and baseLength > maxLength:
        base = base[:maxLength]

    elif index > 0:
        base = base[:index]

    return base


@implementer(IIDNormalizer)
class IDNormalizer:
    """
    This normalizer can normalize any unicode string and returns a
    version that only contains of ASCII characters allowed in a typical
    scripting or programming language id, such as CSS class names or Python
    variable names for example.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IIDNormalizer, IDNormalizer)
      True
    """

    def normalize(self, text, locale=None, max_length=MAX_LENGTH):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt-BR', 'sr@Latn' or 'de'
        """
        if locale is not None:
            # Try to get a normalizer for the locale
            util = queryUtility(IIDNormalizer, name=locale)
            parts = LOCALE_SPLIT_REGEX.split(locale)
            if util is None and len(parts) > 1:
                # Try to get a normalizer for the base language if we asked
                # for one for a language/country combination and found none
                util = queryUtility(IIDNormalizer, name=parts[0])
            # be defensive: if queryUtility() returns an instance of the same
            # normalizer class as this one, we'll loop forever until
            # "RuntimeError: maximum recursion depth exceeded" (ticket #11630)
            if util is not None and util.__class__ is not self.__class__:
                text = util.normalize(text, locale=locale)

        text = baseNormalize(text)

        # lowercase text
        text = text.lower()

        text = IGNORE_REGEX.sub("", text)
        text = NON_WORD_REGEX.sub("-", text)
        text = MULTIPLE_DASHES_REGEX.sub("-", text)
        text = EXTRA_DASHES_REGEX.sub("", text)

        return cropName(text, maxLength=max_length)


@implementer(IFileNameNormalizer)
class FileNameNormalizer:
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters allowed in a file name.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IFileNameNormalizer, FileNameNormalizer)
      True
    """

    def normalize(self, text, locale=None, max_length=MAX_FILENAME_LENGTH):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt-BR', 'sr@Latn' or 'de'
        """
        if locale is not None:
            # Try to get a normalizer for the locale
            util = queryUtility(IFileNameNormalizer, name=locale)
            parts = LOCALE_SPLIT_REGEX.split(locale)
            if util is None and len(parts) > 1:
                # Try to get a normalizer for the base language if we asked
                # for one for a language/country combination and found none
                util = queryUtility(IFileNameNormalizer, name=parts[0])
            # be defensive: if queryUtility() returns an instance of the same
            # normalizer class as this one, we'll loop forever until
            # "RuntimeError: maximum recursion depth exceeded" (ticket #11630)
            if util is not None and util.__class__ is not self.__class__:
                text = util.normalize(text, locale=locale)

        # Preserve filename extensions
        text = baseNormalize(text)

        # Remove any leading underscores
        m = UNDERSCORE_START_REGEX.match(text)
        if m is not None:
            text = m.groups()[1]

        base = text
        ext = ""

        m = FILENAME_REGEX.match(text)
        if m is not None:
            base = m.groups()[0]
            ext = m.groups()[1]

        base = IGNORE_REGEX.sub("", base)
        base = DANGEROUS_CHARS_REGEX.sub("-", base)
        base = EXTRA_DASHES_REGEX.sub("", base)
        base = MULTIPLE_DASHES_REGEX.sub("-", base)

        base = cropName(base, maxLength=max_length)

        if ext != "":
            base = base + "." + ext

        return base


@implementer(IURLNormalizer)
class URLNormalizer:
    """
    This normalizer can normalize any unicode string and returns a URL-safe
    version that only contains of ASCII characters allowed in a URL.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IURLNormalizer, URLNormalizer)
      True
    """

    def normalize(self, text, locale=None, max_length=MAX_URL_LENGTH):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt-BR', 'sr@Latn' or 'de'
        """
        if locale is not None:
            # Try to get a normalizer for the locale
            util = queryUtility(IURLNormalizer, name=locale)
            parts = LOCALE_SPLIT_REGEX.split(locale)
            if util is None and len(parts) > 1:
                # Try to get a normalizer for the base language if we asked
                # for one for a language/country combination and found none
                util = queryUtility(IURLNormalizer, name=parts[0])
            # be defensive: if queryUtility() returns an instance of the same
            # normalizer class as this one, we'll loop forever until
            # "RuntimeError: maximum recursion depth exceeded" (ticket #11630)
            if util is not None and util.__class__ is not self.__class__:
                text = util.normalize(text, locale=locale)

        text = baseNormalize(text)

        # Remove any leading underscores
        m = UNDERSCORE_START_REGEX.match(text)
        if m is not None:
            text = m.groups()[1]

        # lowercase text
        base = text.lower()
        ext = ""

        m = FILENAME_REGEX.match(base)
        if m is not None:
            base = m.groups()[0]
            ext = m.groups()[1]

        base = IGNORE_REGEX.sub("", base)
        base = NON_WORD_REGEX.sub("-", base)
        base = URL_DANGEROUS_CHARS_REGEX.sub("-", base)
        base = EXTRA_DASHES_REGEX.sub("", base)
        base = MULTIPLE_DASHES_REGEX.sub("-", base)

        base = cropName(base, maxLength=max_length)

        if ext != "":
            base = base + "." + ext

        return base


idnormalizer = IDNormalizer()
filenamenormalizer = FileNameNormalizer()
urlnormalizer = URLNormalizer()
