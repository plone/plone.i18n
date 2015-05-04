from setuptools import setup, find_packages

version = '3.0.2'

setup(
    name='plone.i18n',
    version=version,
    description="Advanced i18n/l10n features",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    keywords='i18n l10n Plone',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='http://pypi.python.org/pypi/plone.i18n',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.component',
        'zope.i18n',
        'zope.interface',
        'zope.publisher',
        'Unidecode',
    ],
    extras_require=dict(
        test=[
            'zope.browserresource',
            'zope.component [zcml]',
            'zope.configuration',
            'zope.testing',
        ],
    ),
)
