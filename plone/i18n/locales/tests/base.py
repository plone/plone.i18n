from zope.configuration.xmlconfig import XMLConfig


def setUp():
    from zope.component.testing import setUp

    setUp()
    import zope.component

    XMLConfig("meta.zcml", zope.component)()

    import zope.browserresource

    XMLConfig("meta.zcml", zope.browserresource)()

    import plone.i18n.locales

    XMLConfig("configure.zcml", plone.i18n.locales)()


def tearDown():
    from zope.component.testing import tearDown

    tearDown()
