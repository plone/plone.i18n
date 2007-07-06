from zope.component import queryUtility

from zope.i18n.interfaces import ILanguageAvailability
from zope.i18n.interfaces import INegotiator
from zope.i18n.negotiator import normalize_langs

from zope.interface import implements

from persistent.list import PersistentList

from plone.i18n.negotiator.default import DefaultLanguage


class Negotiator(PersistentList):

    implements(INegotiator)

    def __init__(self):
        super(Negotiator, self).__init__()
        self.append(DefaultLanguage)

    def getLanguage(self, langs, request):
        # langs are the available translation domains

        plugin = self[0](request)
        userlangs = plugin.getPreferredLanguages()

        # Restrict the languages based on site-wide policy
        available = queryUtility(ILanguageAvailability)
        if available is not None:
            langs = available.getAvailableLanguages()

        langs = normalize_langs(langs)

        for lang in userlangs:
            if lang in langs:
                return langs.get(lang)

            # XXX Have this more configurable. For example pt is not a
            # fallback for pt-br. Have a list of allowed fallbacks somewhere
            # in the same way we had PTS X-is-fallback-for headers in po files
            # before.

            # If the user asked for a specific variation, but we don't
            # have it available we may serve the most generic one,
            # according to the spec (eg: user asks for ('en-us',
            # 'de'), but we don't have 'en-us', then 'en' is preferred
            # to 'de').
            parts = lang.split('-')
            if len(parts) > 1 and parts[0] in langs:
                return langs.get(parts[0])
        return None
