from plone.i18n.locales.interfaces import ICountry
from plone.i18n.locales.interfaces import ILanguage

from zope.interface import implements

class Country(object):
    """
    This object has some basic information about a country.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ICountry, Country)
      True

      >>> de = Country(u'de', u'Germany', native = u'Deutschland',
      ...               flag='/@@/country-flags/de.gif')
      >>> de.code
      u'de'
      >>> de.name
      u'Germany'
      >>> de.native
      u'Deutschland'
      >>> de.flag
      '/@@/country-flags/de.gif'
    """
    implements(ICountry)

    def __init__(self, code, name, native=u'', flag=None):
        self.code = code
        self.native = native
        self.name = name
        self.flag = flag


class Language(object):
    """
    This object has some basic information about a language.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ILanguage, Language)
      True

      >>> de = Language(u'de', u'German', native = u'Deutsch',
      ...               flag='/@@/country-flags/de.gif')
      >>> de.code
      u'de'
      >>> de.name
      u'German'
      >>> de.native
      u'Deutsch'
      >>> de.flag
      '/@@/country-flags/de.gif'
    """
    implements(ILanguage)

    def __init__(self, code, name, native=u'', flag=None):
        self.code = code
        self.native = native
        self.name = name
        self.flag = flag

