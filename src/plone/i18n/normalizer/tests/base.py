from zope.configuration.xmlconfig import XMLConfig


def setUp(self=None):
    from zope.component.testing import setUp

    setUp()

    import zope.component

    XMLConfig("meta.zcml", zope.component)()

    import plone.i18n.normalizer

    XMLConfig("configure.zcml", plone.i18n.normalizer)()

    from zope.publisher.browser import BrowserLanguages

    zope.component.provideAdapter(BrowserLanguages)


def tearDown(self=None):
    from zope.component.testing import tearDown

    tearDown()
