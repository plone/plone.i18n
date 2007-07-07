from zope.component import queryUtility
from zope.i18n.interfaces import ILanguageAvailability
from zope.i18n.interfaces import IUserPreferredLanguages
from zope.interface import implements

from plone.i18n.locales.interfaces import ICcTLDInformation


class TldLanguage(object):

    implements(IUserPreferredLanguages)

    def __init__(self, request):
        self.request = request

    def getPreferredLanguages(self):
        """Return a sequence of user preferred languages."""
        langs = []

        host = self.request.get('HTTP_HOST', None)
        tlds = queryUtility(ICcTLDInformation)
        if host is None or tlds is None:
            return None

        tld = host.split(":")[0].lower().split(".")[-1]
        wanted = tlds.getTLDs().get(tld, [])

        available = queryUtility(ILanguageAvailability)
        if available is not None:
            langs = [str(lang) for lang in available.getAvailableLanguages()]

        langs = [lang for lang in wanted if lang in langs]
        return langs and langs or None
