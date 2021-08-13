from plone.i18n.interfaces import ILanguageUtility
from Products.CMFCore.utils import registerToolInterface


registerToolInterface("portal_languages", ILanguageUtility)
