from zope.interface import Interface


class ILanguageFallback(Interface):

    def fallback(language):
        """
        Returns a tuple of potential fallback languages for a passed in
        language code.
        """
