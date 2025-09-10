from ..interfaces import ILanguageUtility
from ..interfaces import INegotiateLanguage
from zope.component import getUtility
from zope.interface import implementer


@implementer(INegotiateLanguage)
class NegotiateLanguage:
    """Perform default language negotiation"""

    def __init__(self, site, request):
        """Setup the current language stuff."""
        tool = getUtility(ILanguageUtility)
        langs = []
        useContent = tool.settings.use_content_negotiation
        useCcTLD = tool.settings.use_cctld_negotiation
        useSubdomain = tool.settings.use_subdomain_negotiation
        usePath = tool.settings.use_path_negotiation
        useCookie = tool.settings.use_cookie_negotiation
        setCookieEverywhere = tool.settings.set_cookie_always
        authOnly = tool.settings.authenticated_users_only
        useRequest = tool.settings.use_request_negotiation
        useDefault = 1  # This should never be disabled
        langsCookie = None
        if usePath:
            # This one is set if there is an allowed language in the current
            # path
            langs.append(tool.getPathLanguage(request))

        if useContent:
            langs.append(tool.getContentLanguage(request))

        if useCookie and not (authOnly and tool.isAnonymousUser()):
            # If we are using the cookie stuff we provide the setter here
            set_language = request.get("set_language", None)
            if set_language:
                langsCookie = tool.setLanguageCookie(set_language, request=request)
            else:
                # Get from cookie
                langsCookie = tool.getLanguageCookie(request)
            langs.append(langsCookie)

        if useSubdomain:
            langs.extend(tool.getSubdomainLanguages(request))

        if useCcTLD:
            langs.extend(tool.getCcTLDLanguages(request))

        # Get langs from request
        if useRequest:
            langs.extend(tool.getRequestLanguages(request))

        # Get default
        if useDefault:
            langs.append(tool.getDefaultLanguage())

        # Filter None languages
        langs = [lang for lang in langs if lang is not None]

        # Set cookie language to language
        if setCookieEverywhere and langs[0] != langsCookie:
            # We need to make sure its not a subrequest otherwise we are going
            # To change the language of the main request
            from plone.subrequest import ISubRequest

            if not ISubRequest.providedBy(request):
                tool.setLanguageCookie(langs[0], noredir=True, request=request)

        self.default_language = langs[-1]
        self.language = langs[0]
        self.language_list = langs[1:-1]
