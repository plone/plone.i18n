from setuptools import setup, find_packages
import sys, os

version = '1.0.8'

setup(name='plone.i18n',
      version=version,
      description="Advanced i18n/l10n features",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        'Framework :: Plone',
        'Framework :: Zope2',
      ],
      keywords='i18n l10n Plone',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.i18n',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
      ],
      )
