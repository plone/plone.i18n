from zope.i18n.interfaces import ILanguageAvailability as IBaseLanguageAvailability
from zope.interface import Interface


class ICcTLDInformation(Interface):
    """A list of country code top level domains their relevant languages."""

    def getAvailableTLDs():
        """Return a sequence of country code top level domains."""

    def getTLDs():
        """Return a sequence of ccTLDs and their languages."""

    def getLanguagesForTLD(tld):
        """Return the relevant languages for a top level domain."""


class ICountryAvailability(Interface):
    """A list of available coutries."""

    def getAvailableCountries():
        """Return a sequence of country tags for available countries."""

    def getCountries():
        """Return a sequence of Country objects for available countries."""

    def getCountryListing():
        """Return a sequence of country code and country name tuples."""


class ILanguageAvailability(IBaseLanguageAvailability):
    """A list of available languages."""

    def getLanguages(combined=False):
        """Return a sequence of Language objects for available languages."""

    def getLanguageListing(combined=False):
        """Return a sequence of language code and language name tuples."""


class IContentLanguageAvailability(ILanguageAvailability):
    """A list of available content languages."""


class IMetadataLanguageAvailability(ILanguageAvailability):
    """A list of available metadata languages."""


class IModifiableLanguageAvailability(ILanguageAvailability):
    """A modifiable list of available languages."""

    def setAvailableLanguages(languages, combined=False):
        """Set a list of available language tags."""


class IModifiableCountryAvailability(ICountryAvailability):
    """A modifiable list of available countries."""

    def setAvailableCountries(countries):
        """Set a list of available country tags."""
