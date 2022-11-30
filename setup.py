from setuptools import find_packages
from setuptools import setup


version = "5.0.0"

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
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="i18n l10n Plone",
    author="Plone Foundation",
    author_email="releaseteam@plone.org",
    url="https://github.com/plone/plone.i18n",
    license="GPL version 2",
    packages=find_packages(),
    namespace_packages=["plone"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "plone.base",
        "setuptools",
        "Unidecode>=1.0.22",
        "zope.globalrequest",
    ],
    extras_require=dict(
        test=[
            "plone.app.contenttypes[testing]",
            "plone.app.testing",
            "zope.testing",
        ],
    ),
)
