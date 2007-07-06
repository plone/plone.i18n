from zope.i18n.interfaces import IUserPreferredLanguages
from zope.interface import implements


class DefaultLanguage(object):
    
    implements(IUserPreferredLanguages)

    def __init__(self, request):
        self.request = request

    def getPreferredLanguages(self):
        """Return a sequence of user preferred languages."""
        return []
