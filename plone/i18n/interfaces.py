from zope.interface import Interface, Attribute


class ILanguageUtility(Interface):
    """Marker interface for the portal_languages tool.
    """


class INegotiateLanguage(Interface):
    """Result of language negotiation
    """
    language = Attribute('Language to use')
    default_language = Attribute('Default language')
    language_list = Attribute('List of language preferences in order')
