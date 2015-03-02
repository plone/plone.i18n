from Products.CMFCore.utils import registerToolInterface
from plone.i18n.interfaces import ILanguageUtility


registerToolInterface('portal_languages', ILanguageUtility)
