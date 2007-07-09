from zope.component import queryUtility
from zope.i18n.interfaces import INegotiator
from zope.i18n.negotiator import normalize_langs
from zope.interface import implements

from persistent.list import PersistentList

from plone.i18n.locales.interfaces import IContentLanguageAvailability
from plone.i18n.negotiator.default import DefaultLanguage
from plone.i18n.negotiator.interfaces import ILanguageFallback


class Negotiator(PersistentList):

    implements(INegotiator)

    def __init__(self):
        super(Negotiator, self).__init__()
        self.append(DefaultLanguage)

    def getLanguage(self, langs, request):
        # langs are the available languages from the translation domains
        userlangs = []

        for plugin_registration in self:
            plugin = plugin_registration(request)
            userlangs = plugin.getPreferredLanguages()
            # Stop once we got a result from a plugin
            if userlangs is not None:
                break

        if userlangs is None:
            return None

        # Restrict the languages based on site-wide policy
        allowed = queryUtility(IContentLanguageAvailability)
        if allowed is not None:
            langs = [str(lang) for lang in allowed.getAvailableLanguages()]

        langs = normalize_langs(langs)
        fallback = queryUtility(ILanguageFallback)

        for lang in userlangs:
            if lang in langs:
                return langs.get(lang)

            # If the user asked for a specific variation, but we don't
            # have it available we may serve the most generic one,
            # according to the spec (eg: user asks for ('en-us',
            # 'de'), but we don't have 'en-us', then 'en' is preferred
            # to 'de').
            if fallback is not None:
                fallbacks = fallback.fallback(lang)
                for fb in fallbacks:
                    if fb in langs:
                        return fb

        return None
