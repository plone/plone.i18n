from setuptools import setup, find_packages
import sys, os

version = '1.0rc1'

setup(name='plone.i18n',
      version=version,
      description="Advanced i18n/l10n features",
      long_description="""\
""",
      classifiers=[
        'Framework :: Plone',
        'Framework :: Zope2',
        'Framework :: Zope3'
      ],
      keywords='i18n l10n Plone',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/plone/plone.i18n',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
      ],
      )
