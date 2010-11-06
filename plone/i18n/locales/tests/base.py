from zope.configuration.xmlconfig import XMLConfig


def setUp():
    from zope.component.testing import setUp
    setUp()
    import zope.component
    XMLConfig('meta.zcml', zope.component)()

    # BBB Zope 2.12
    try:
        import zope.browserresource
        XMLConfig('meta.zcml', zope.browserresource)()
    except ImportError:
        import zope.app.publisher.browser
        XMLConfig('meta.zcml', zope.app.publisher.browser)()

    import plone.i18n.locales
    XMLConfig('configure.zcml', plone.i18n.locales)()


def tearDown():
    from zope.component.testing import tearDown
    tearDown()
