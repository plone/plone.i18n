from pathlib import Path
from setuptools import setup


version = "6.0.0a1.dev0"

long_description = (
    f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst').read_text()}"
)

setup(
    name="plone.i18n",
    version=version,
    description="Advanced i18n/l10n features",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="i18n l10n Plone",
    author="Plone Foundation",
    author_email="releaseteam@plone.org",
    url="https://github.com/plone/plone.i18n",
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "plone.autoform",
        "plone.registry",
        "plone.subrequest",
        "plone.supermodel",
        "Products.CMFCore",
        "Unidecode>=1.0.22",
        "Zope",
        "zope.globalrequest",
    ],
    extras_require=dict(
        test=[
            "plone.app.contenttypes[test]",
            "plone.app.multilingual",
            "plone.app.testing",
            "plone.base",
            "zope.browserresource",
        ],
    ),
)
