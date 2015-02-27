from zope.interface import implements
from plone.i18n.interfaces import INegotiateLanguage
from Products.CMFCore.utils import getToolByName


class NegotiateLanguage(object):
    """Perform default language negotiation"""
    implements(INegotiateLanguage)

    def __init__(self, site, request):
        """Setup the current language stuff."""
        tool = getToolByName(site, 'portal_languages')
        langs = []
        useContent = tool.use_content_negotiation
        useCcTLD = tool.use_cctld_negotiation
        useSubdomain = tool.use_subdomain_negotiation
        usePath = tool.use_path_negotiation
        useCookie = tool.use_cookie_negotiation
        setCookieEverywhere = tool.set_cookie_everywhere
        authOnly = tool.authenticated_users_only
        useRequest = tool.use_request_negotiation
        useDefault = 1 # This should never be disabled
        langsCookie = None

        if usePath:
            # This one is set if there is an allowed language in the current path
            langs.append(tool.getPathLanguage())

        if useContent:
            langs.append(tool.getContentLanguage())

        if useCookie and not (authOnly and tool.isAnonymousUser()):
            # If we are using the cookie stuff we provide the setter here
            set_language = tool.REQUEST.get('set_language', None)
            if set_language:
                langsCookie = tool.setLanguageCookie(set_language)
            else:
                # Get from cookie
                langsCookie = tool.getLanguageCookie()
            langs.append(langsCookie)

        if useSubdomain:
            langs.extend(tool.getSubdomainLanguages())

        if useCcTLD:
            langs.extend(tool.getCcTLDLanguages())

        # Get langs from request
        if useRequest:
            langs.extend(tool.getRequestLanguages())

        # Get default
        if useDefault:
            langs.append(tool.getDefaultLanguage())

        # Filter None languages
        langs = [lang for lang in langs if lang is not None]

        # Set cookie language to language
        if setCookieEverywhere and useCookie and langs[0] != langsCookie:
            tool.setLanguageCookie(langs[0], noredir=True)

        self.default_language = langs[-1]
        self.language = langs[0]
        self.language_list = langs[1:-1]