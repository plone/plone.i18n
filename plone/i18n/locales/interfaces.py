from zope.interface import Interface, Attribute
from zope.i18n.interfaces import ILanguageAvailability

class ICountry(Interface):
    """A single country object."""

    code = Attribute('The ISO 3166-1 country code of this country.')

    name = Attribute('The english name of this country.')

    native = Attribute('The native name of this country.')

    flag = Attribute('A path to the flag resource of this country.')


class ILanguage(Interface):
    """A single language object."""

    code = Attribute('The ISO 639-1 language code of this language.')

    name = Attribute('The english name of this language.')

    native = Attribute('The native name of this language.')

    flag = Attribute('A path to a flag resource that can be used to symolize '
                     'this language.')

class ICountryAvailability(Interface):
    """A list of available coutries."""

    def getAvailableCountries():
        """Return a sequence of country tags for available countries.
        """

    def getCountries():
        """Return a sequence of Country objects for available countries.
        """

class IContentLanguageAvailability(ILanguageAvailability):
    """A list of available content languages."""

    def getLanguages():
        """Return a sequence of Language objects for available languages.
        """

class IMetadataLanguageAvailability(ILanguageAvailability):
    """A list of available metadata languages."""

    def getLanguages():
        """Return a sequence of Language objects for available languages.
        """
