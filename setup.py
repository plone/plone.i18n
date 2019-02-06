from setuptools import setup, find_packages

version = '4.0.3.dev0'

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
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='i18n l10n Plone',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.org/project/plone.i18n',
    license='GPL version 2',
    packages=find_packages(),
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
