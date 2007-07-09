from zope.component import queryUtility
from zope.i18n.interfaces import ILanguageAvailability
from zope.i18n.interfaces import IUserPreferredLanguages
from zope.interface import implements


class CookieLanguage(object):

    implements(IUserPreferredLanguages)

    def __init__(self, request):
        self.request = request

    def getPreferredLanguages(self):
        """Return a sequence of user preferred languages."""
        langs = []

        cookie = self.request.cookies.get('I18N_LANGUAGE', None)
        available = queryUtility(ILanguageAvailability)
        if available is None:
            return None

        if cookie in [str(lang) for lang in available.getAvailableLanguages()]:
            return [cookie]

        return None
