from setuptools import find_packages
from setuptools import setup


version = "5.0.0a3.dev0"

setup(
    name="plone.i18n",
    version=version,
    description="Advanced i18n/l10n features",
    long_description=(open("README.rst").read() + "\n" + open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="i18n l10n Plone",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://pypi.org/project/plone.i18n",
    license="GPL version 2",
    packages=find_packages(),
    namespace_packages=["plone"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "AccessControl",
        "Products.CMFCore",
        "plone.supermodel",
        "setuptools",
        "Unidecode>=1.0.22",
        "ZODB",
        "zope.component",
        "zope.i18n",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
        "zope.schema",
        "zope.globalrequest",
        "Zope",
    ],
    extras_require=dict(
        test=[
            "plone.app.contenttypes",
            "plone.app.testing",
            "plone.registry",
            "zope.browserresource",
            "zope.component [zcml]",
            "zope.configuration",
            "zope.testing",
        ],
    ),
)
