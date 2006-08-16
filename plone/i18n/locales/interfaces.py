from zope.interface import Interface
from zope.i18n.interfaces import ILanguageAvailability

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

class IModifiableLanguageAvailability(ILanguageAvailability):
    """A modifiable list of available languages."""

    def setAvailableLanguages(languages):
        """Set a list of available language tags.
        """

class IModifiableCountryAvailability(ICountryAvailability):
    """A modifiable list of available countries."""

    def setAvailableCountries(countries):
        """Set a list of available country tags.
        """
