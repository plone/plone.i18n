from zope.interface import Interface, Attribute

class ICountry(Interface):
    """A single country object."""

    code = Attribute('The ISO 3166-1 country code of this country.')

    name = Attribute('The english name of this country.')

    native = Attribute('The native name of this country.')

    flag = Attribute('A path to the flag resource of this country.')


class ILanguage(Interface):
    """A single language object."""

    code = Attribute('The ISO 639-1 language code of this language.')

    name = Attribute('The english name of this language.')

    native = Attribute('The native name of this language.')

    flag = Attribute('A path to a flag resource that can be used to symolize '
                     'this language.')

