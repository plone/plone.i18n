from zope.interface import implements
from plone.i18n.interfaces import ILanguageUtility, INegotiateLanguage
from zope.component import queryUtility
from plone.i18n.locales.interfaces import ICountryAvailability
from plone.i18n.locales.interfaces import IContentLanguageAvailability
from plone.i18n.locales.interfaces import ICcTLDInformation
from Products.SiteAccess.VirtualHostMonster import VirtualHostMonster
from ZODB.POSException import ConflictError
from AccessControl import ClassSecurityInfo
from zope.component.hooks import getSite
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.interfaces import IDublinCore


class LanguageUtility(object):
    implements(ILanguageUtility)

    def getSupportedLanguages(self):
        """Returns a list of supported language codes."""
        return self.supported_langs

    def listSupportedLanguages(self):
        """Returns a list of supported language names."""
        r = []
        available = self.getAvailableLanguages()
        for i in self.supported_langs:
            if available.get(i):
                r.append((i, available[i][u'name']))
        return r

    def getAvailableLanguages(self):
        """Returns the dictionary of available languages.
        """
        util = queryUtility(IContentLanguageAvailability)
        if self.use_combined_language_codes:
            languages = util.getLanguages(combined=True)
        else:
            languages = util.getLanguages()
        return languages

    def getCcTLDInformation(self):
        util = queryUtility(ICcTLDInformation)
        return util.getTLDs()

    def listAvailableLanguages(self):
        """Returns sorted list of available languages (code, name)."""
        util = queryUtility(IContentLanguageAvailability)
        if self.use_combined_language_codes:
            languages = util.getLanguageListing(combined=True)
        else:
            languages = util.getLanguageListing()
        languages.sort(lambda x, y: cmp(x[1], y[1]))
        return languages

    def listAvailableLanguageInformation(self):
        """Returns list of available languages."""
        langs = self.getAvailableLanguageInformation()
        new_langs = []
        for lang in langs:
            # add language-code to dict
            langs[lang][u'code'] = lang
            # flatten outer dict to list to make it sortable
            new_langs.append(langs[lang])
        new_langs.sort(lambda x, y: cmp(x.get(u'native', x.get(u'name')), y.get(u'native', y.get(u'name'))))
        return new_langs

    def getAvailableLanguageInformation(self):
        """Returns the dictionary of available languages."""
        util = queryUtility(IContentLanguageAvailability)
        if self.use_combined_language_codes:
            languages = util.getLanguages(combined=True)
        else:
            languages = util.getLanguages()

        for lang in languages:
            languages[lang]['code'] = lang
            if lang in self.supported_langs:
                languages[lang]['selected'] = True
            else:
                languages[lang]['selected'] = False
        return languages

    def getDefaultLanguage(self):
        """Returns the default language."""
        portal_properties = getToolByName(self, "portal_properties", None)
        if portal_properties is None:
            return 'en'
        site_properties = getattr(portal_properties, 'site_properties', None)
        if site_properties is not None:
            if site_properties.hasProperty('default_language'):
                return site_properties.getProperty('default_language')
        portal = getUtility(ISiteRoot)
        if portal.hasProperty('default_language'):
            return portal.getProperty('default_language')
        return getattr(self, 'default_lang', 'en')

    def setDefaultLanguage(self, langCode):
        """Sets the default language."""
        portal_properties = getToolByName(self, "portal_properties")
        site_properties = getattr(portal_properties, 'site_properties', None)
        if site_properties is not None:
            if site_properties.hasProperty('default_language'):
                return site_properties._updateProperty('default_language', langCode)
        portal = getUtility(ISiteRoot)
        if portal.hasProperty('default_language'):
            return portal._updateProperty('default_language', langCode)
        self.default_lang = langCode

    def getNameForLanguageCode(self, langCode):
        """Returns the name for a language code."""
        info = self.getAvailableLanguageInformation().get(langCode, None)
        if info is not None:
            return info.get(u'name', None)
        return None

    def getFlagForLanguageCode(self, langCode):
        """Returns the name of the flag for a language code."""
        info = self.getAvailableLanguageInformation().get(langCode, None)
        if info is not None:
            return info.get(u'flag', None)
        return None

    def addSupportedLanguage(self, langCode):
        """Registers a language code as supported."""
        alist = self.supported_langs[:]
        if (langCode in self.getAvailableLanguages().keys()) and not langCode in alist:
            alist.append(langCode)
            self.supported_langs = alist

    def removeSupportedLanguages(self, langCodes):
        """Unregisters language codes from supported."""
        alist = self.supported_langs[:]
        for i in langCodes:
            alist.remove(i)
        self.supported_langs = alist

    def setLanguageCookie(self, lang=None, REQUEST=None, noredir=None):
        """Sets a cookie for overriding language negotiation."""
        res = None
        if lang and lang in self.getSupportedLanguages():
            if lang != self.getLanguageCookie():
                self.REQUEST.RESPONSE.setCookie('I18N_LANGUAGE', lang, path='/')
            res = lang
        if noredir is None:
            if REQUEST:
                REQUEST.RESPONSE.redirect(REQUEST['HTTP_REFERER'])
        return res

    def getLanguageCookie(self):
        """Gets the preferred cookie language."""
        if not hasattr(self, 'REQUEST'):
            return None
        langCookie = self.REQUEST.cookies.get('I18N_LANGUAGE')
        if langCookie in self.getSupportedLanguages():
            return langCookie
        return None

    def getPreferredLanguage(self):
        """Gets the preferred site language."""
        l = self.getLanguageBindings()
        if l[0]:
            if not self.use_combined_language_codes:
                return l[0].split('-')[0]
            else:
                return l[0]
            return l[0]
        # this is the default language
        return l[1]

    def getPathLanguage(self):
        """Checks if a language is part of the current path."""
        if not hasattr(self, 'REQUEST'):
            return []
        items = self.REQUEST.get('TraversalRequestNameStack')
        # XXX Why this try/except?
        try:
            for item in items:
                if item in self.getSupportedLanguages():
                    return item
        except (ConflictError, KeyboardInterrupt):
            raise
        except:
            pass
        return None

    def getContentLanguage(self):
        """Checks the language of the current content if not folderish."""
        if not hasattr(self, 'REQUEST'):
            return []
        try: # This will actually work nicely with browserdefault as we get attribute error...
            contentpath = self.REQUEST.path[:]

            # Now check if we need to exclude from using language specific path
            # See https://dev.plone.org/ticket/11263
            if (bool([1 for p in self.exclude_paths if p in contentpath]) or
                bool([1 for p in self.exclude_exts if contentpath[0].endswith(p)])
                ):
                return None

            obj = self.aq_parent
            traversed = []
            while contentpath:
                name = contentpath.pop()
                if name[0] in '@+':
                    break
                next = obj.unrestrictedTraverse(name, None)
                if next is None:
                    break
                if isinstance(next, VirtualHostMonster):
                    # next element is the VH subpath
                    contentpath.pop()
                    continue
                obj = next
                traversed.append(obj)
            for obj in reversed(traversed):
                if IDublinCore.providedBy(obj):
                    lang = obj.Language()
                    if not lang:
                        continue
                    if lang in self.getSupportedLanguages():
                        return lang
                    else:
                        return None
        except ConflictError:
            raise
        except:
            pass
        return None

    def getCcTLDLanguages(self):
        if not hasattr(self, 'REQUEST'):
            return None
        request = self.REQUEST
        if not "HTTP_HOST" in request:
            return None
        host = request["HTTP_HOST"].split(":")[0].lower()
        tld = host.split(".")[-1]
        wanted = self.getCcTLDInformation().get(tld, [])
        allowed = self.getSupportedLanguages()
        return [lang for lang in wanted if lang in allowed]

    def getSubdomainLanguages(self):
        if not hasattr(self, 'REQUEST'):
            return None
        request = self.REQUEST
        if not "HTTP_HOST" in request:
            return None
        host = request["HTTP_HOST"].split(":")[0].lower()
        tld = host.split(".")[0]
        wanted = self.getCcTLDInformation().get(tld, [])
        allowed = self.getSupportedLanguages()
        return [lang for lang in wanted if lang in allowed]

    def getRequestLanguages(self):
        """Parses the request and return language list."""

        if not hasattr(self, 'REQUEST'):
            return None

        # Get browser accept languages
        browser_pref_langs = self.REQUEST.get('HTTP_ACCEPT_LANGUAGE', '')
        browser_pref_langs = browser_pref_langs.split(',')

        i = 0
        langs = []
        length = len(browser_pref_langs)

        # Parse quality strings and build a tuple like
        # ((float(quality), lang), (float(quality), lang))
        # which is sorted afterwards
        # If no quality string is given then the list order
        # is used as quality indicator
        for lang in browser_pref_langs:
            lang = lang.strip().lower().replace('_', '-')
            if lang:
                l = lang.split(';', 2)
                quality = []

                if len(l) == 2:
                    try:
                        q = l[1]
                        if q.startswith('q='):
                            q = q.split('=', 2)[1]
                            quality = float(q)
                    except:
                        pass

                if quality == []:
                    quality = float(length-i)

                language = l[0]
                if (self.use_combined_language_codes and
                        language in self.getSupportedLanguages()):
                    # If allowed add the language
                    langs.append((quality, language))
                else:
                    # if we only use simply language codes, we should recognize
                    # combined codes as their base code. So 'de-de' is treated
                    # as 'de'.
                    baselanguage = language.split('-')[0]
                    if baselanguage in self.getSupportedLanguages():
                        langs.append((quality, baselanguage))
                i = i + 1

        # Sort and reverse it
        langs.sort()
        langs.reverse()

        # Filter quality string
        langs = map(lambda x: x[1], langs)

        return langs

    def setLanguageBindings(self):
        """Setups the current language stuff."""
        if not hasattr(self, 'REQUEST'):
            return
        settings = getMultiAdapter((getSite(), self.REQUEST), INegotiateLanguage)
        binding = self.REQUEST.get('LANGUAGE_TOOL', None)
        if not isinstance(binding, LanguageBinding):
            # Create new binding instance
            binding = LanguageBinding(self)
            # Set bindings instance to request here to avoid infinite recursion
            self.REQUEST['LANGUAGE_TOOL'] = binding
        # Bind languages
        binding.LANGUAGE = lang = settings.language
        binding.DEFAULT_LANGUAGE = settings.default_language
        binding.LANGUAGE_LIST = list(settings.language_list)
        # Set LANGUAGE to request
        self.REQUEST['LANGUAGE'] = lang
        return lang

    def getLanguageBindings(self):
        """Returns the bound languages.

        (language, default_language, languages_list)
        """
        if not hasattr(self, 'REQUEST'):
            # Can't do anything
            return (None, self.getDefaultLanguage(), [])
        binding = self.REQUEST.get('LANGUAGE_TOOL', None)
        if not isinstance(binding, LanguageBinding):
            # Not bound -> bind
            self.setLanguageBindings()
            binding = self.REQUEST.get('LANGUAGE_TOOL')
        return binding.getLanguageBindings()

    def getAvailableCountries(self):
        """Returns the dictionary of available countries."""
        util = queryUtility(ICountryAvailability)
        return util.getCountries()

    def listAvailableCountries(self):
        """Returns the sorted list of available countries (code, name)."""
        util = queryUtility(ICountryAvailability)
        countries = util.getCountryListing()
        countries.sort(lambda x, y: cmp(x[1], y[1]))
        return countries

    def getNameForCountryCode(self, countryCode):
        """Returns the name for a country code."""
        return self.getAvailableCountries().get(countryCode, countryCode)

    def isAnonymousUser(self):
        from AccessControl import getSecurityManager
        user = getSecurityManager().getUser()
        return not user.has_role('Authenticated')

    def showSelector(self):
        """Returns True if the selector viewlet should be shown."""
        if self.always_show_selector:
            return True
        if (self.use_cookie_negotiation and
            not (self.authenticated_users_only and self.isAnonymousUser())):
            return True
        return False


class LanguageBinding:
    """Helper which holding language infos in request."""
    security = ClassSecurityInfo()
    __allow_access_to_unprotected_subobjects__ = 1

    DEFAULT_LANGUAGE = None
    LANGUAGE = None
    LANGUAGE_LIST = []

    def __init__(self, tool):
        self.tool = tool

    security.declarePublic('getLanguageBindings')

    def getLanguageBindings(self):
        """Returns the bound languages.

        (language, default_language, languages_list)
        """
        return (self.LANGUAGE, self.DEFAULT_LANGUAGE, self.LANGUAGE_LIST)
