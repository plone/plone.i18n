from zope.interface import implements

from plone.i18n.negotiator.interfaces import ILanguageFallback


class LanguageFallback(object):

    implements(ILanguageFallback)

    def __init__(self):
        pass

    def fallback(self, language):
        # pt is not a fallback for pt-br
        if language.startswith('pt-br'):
            return ()
        parts = language.split('-')
        return (parts[0],)
