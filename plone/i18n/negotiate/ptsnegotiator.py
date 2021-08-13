from zope.i18n.interfaces import IUserPreferredLanguages
from zope.interface import implementer

import operator


# this is the negotiator from old PlacelessTranslationService
# may be cleaned up in future

_langPrefsRegistry = {}


def getAcceptedHelper(self, request, kind="language"):
    """this is patched on prefs classes which don't define the getAccepted
    classes but define the deprecated getPreferredLanguages method"""
    return self.getPreferredLanguages()


def registerLangPrefsMethod(prefs, kind="language"):
    # check for correct format of prefs
    if not isinstance(prefs, dict):
        prefs = {"klass": prefs, "priority": 0}
    # add chain for kind
    if kind not in _langPrefsRegistry:
        _langPrefsRegistry[kind] = []
    # backwards compatibilty monkey patch
    if not hasattr(prefs["klass"], "getAccepted"):
        prefs["klass"].getAccepted = getAcceptedHelper
    # add this pref helper
    _langPrefsRegistry[kind].append(prefs)
    # sort by priority
    _langPrefsRegistry[kind].sort(key=operator.itemgetter("priority"), reverse=True)


def getLangPrefs(env, kind="language"):
    """get higest prio method for kind"""
    for pref in _langPrefsRegistry[kind]:
        handler = pref["klass"](env)
        accepted = handler.getAccepted(env, kind)
        if accepted:
            return accepted
    return ()


def lang_normalize(lang):
    """filter"""
    return lang.replace("_", "-")


def str_lower(aString):
    """filter"""
    return aString.lower()


def str_strip(aString):
    """filter"""
    return aString.strip()


def type_accepted(available, preferred):
    # ex: preferred is text/* and available is text/html
    av = available.split("/")
    pr = preferred.split("/")
    if len(av) < 2 or len(pr) < 2:
        return False
    return pr[1] == "*" and pr[0] == av[0]


def lang_accepted(available, preferred):
    # ex: available is pt, preferred is pt-br
    return available.startswith(preferred)


def _false(*a, **kw):
    pass


class BrowserAccept:

    filters = {
        "content-type": (str_lower,),
        "language": (str_lower, lang_normalize, str_strip),
    }

    def __init__(self, request):
        pass

    def getAccepted(self, request, kind="content-type"):
        custom_name = ("user_%s" % kind).lower()
        if kind == "content-type":
            header_name = ("HTTP_ACCEPT").upper()
        else:
            header_name = ("HTTP_ACCEPT_%s" % kind).upper()

        user_accepts = request.get(custom_name, "")
        http_accepts = request.get(header_name, "")

        if (
            user_accepts
            and http_accepts
            and user_accepts == request.cookies.get("custom_name")
        ):
            user_accepts = [a.strip() for a in user_accepts.split(",")]
            http_accepts = [a.strip() for a in http_accepts.split(",")]
            for l in user_accepts:
                if l not in http_accepts:
                    req_accepts = user_accepts + http_accepts
                    break
                else:
                    # user_accepts is a subset of http_accepts
                    request.RESPONSE.expireCookie("custom_name", path="/")
                    req_accepts = http_accepts
        else:
            req_accepts = (user_accepts + "," + http_accepts).split(",")

        accepts = []
        i = 0
        length = len(req_accepts)
        filters = self.filters.get(kind, ())

        # parse quality strings and build a tuple like
        # ((float(quality), lang), (float(quality), lang))
        # which is sorted afterwards if no quality string is given then the
        # list order is used as quality indicator
        for accept in req_accepts:
            for normalizer in filters:
                accept = normalizer(accept)
            if accept:
                ll = accept.split(";", 2)
                quality = []

                if len(ll) == 2:
                    try:
                        q = l[1]
                        if q.startswith("q="):
                            q = q.split("=", 2)[1]
                            quality = float(q)
                    except Exception:
                        pass

                if quality == []:
                    quality = float(length - i)

                accepts.append((quality, ll[0]))
                i += 1

        # sort and reverse it
        accepts.sort()
        accepts.reverse()

        return [a[1] for a in accepts]


class CookieAccept:
    filters = (str_lower, lang_normalize, str_strip)

    def __init__(self, request):
        pass

    def getAccepted(self, request, kind="language"):
        if not hasattr(request, "cookies"):
            return ()
        language = request.cookies.get("pts_language", None)
        if language:
            if isinstance(language, tuple):
                return language
            else:
                # filter
                for filter in self.filters:
                    language = list(filter(language))
                return (language,)
        else:
            return ()


def setCookieLanguage(request, lang, REQUEST=None):
    """sets the language to a cookie

    request - the request object
    lang - language as string like de or pt_BR (it's normalizd)
    """
    if isinstance(lang, tuple):
        lang = lang[1]
    lang = str_lower(lang_normalize(lang))
    request.RESPONSE.setCookie("pts_language", lang)
    if REQUEST:
        REQUEST.RESPONSE.redirect(REQUEST.URL0)
    else:
        return lang


# higher number = higher priority
# if a acceptor returns a false value (() or None) then the next acceptor
# in the chain is queried
registerLangPrefsMethod({"klass": BrowserAccept, "priority": 10}, "language")
registerLangPrefsMethod({"klass": CookieAccept, "priority": 40}, "language")
registerLangPrefsMethod({"klass": BrowserAccept, "priority": 10}, "content-type")


class Negotiator:

    tests = {"content-type": type_accepted, "language": lang_accepted}

    def negotiate(self, choices, request, kind="content-type"):
        choices = tuple(choices)
        return self._negotiate(choices, request, kind)

    def _negotiate(self, choices, request, kind):
        userchoices = getLangPrefs(request, kind)
        # Prioritize on the user preferred choices. Return the first user
        # preferred choice that the object has available.
        test = self.tests.get(kind, _false)
        for choice in userchoices:
            if choice in choices:
                return choice
            for l_avail in choices:
                if test(l_avail, choice):
                    return l_avail
        return None

    # backwards compatibility... should be deprecated
    def getLanguage(self, langs, request):
        return self.negotiate(langs, request, "language")

    def getLanguages(self, request):
        return getLangPrefs(request, "language")


negotiator = Negotiator()


def negotiate(langs, request):
    return negotiator.negotiate(langs, request, "language")


@implementer(IUserPreferredLanguages)
class PTSLanguages:
    """Languages adapter that chooses languages for the zope.i18n machinery.

    This used to be part of Products.Five.i18n.
    """

    def __init__(self, context):
        self.context = context

    def getPreferredLanguages(self):
        return getLangPrefs(self.context)
