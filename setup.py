from setuptools import setup, find_packages

version = '4.0.0'

setup(
    name='plone.i18n',
    version=version,
    description="Advanced i18n/l10n features",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='i18n l10n Plone',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/plone.i18n',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFCore',
        'Products.CMFPlone',
        'setuptools',
        'six',
        'Unidecode',
        'zope.component',
        'zope.i18n',
        'zope.interface',
        'zope.publisher',
        'Zope2',
    ],
    extras_require=dict(
        test=[
            'plone.registry',
            'zope.browserresource',
            'zope.component [zcml]',
            'zope.configuration',
            'zope.testing',
        ],
    ),
)
