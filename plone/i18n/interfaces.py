# -*- coding: utf-8 -*-
from zope.interface import Attribute
from zope.interface import Interface


class ILanguageUtility(Interface):
    """Marker interface for the portal_languages tool.
    """


class INegotiateLanguage(Interface):
    """Result of language negotiation
    """
    language = Attribute('Language to use')
    default_language = Attribute('Default language')
    language_list = Attribute('List of language preferences in order')
