from zope.component import queryUtility
from zope.i18n.interfaces import ILanguageAvailability
from zope.i18n.interfaces import IUserPreferredLanguages
from zope.interface import implements


class PathLanguage(object):

    implements(IUserPreferredLanguages)

    def __init__(self, request):
        self.request = request

    def getPreferredLanguages(self):
        """Return a sequence of user preferred languages."""
        langs = []
        items = self.request.get('TraversalRequestNameStack')

        available = queryUtility(ILanguageAvailability)
        if available is not None:
            langs = [str(lang) for lang in available.getAvailableLanguages()]

        for item in items:
            if item in langs:
                return [item]

        return None
