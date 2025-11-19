Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

6.0.0a1 (2025-11-19)
--------------------

Breaking changes:


- Replace ``pkg_resources`` namespace with PEP 420 native namespace.
  Support only Plone 6.2 and Python 3.10+. (#3928)


5.1.1 (2025-09-10)
------------------

Internal:


- Move distribution to src layout [gforcada] (#4217)


5.1.0 (2025-03-25)
------------------

New features:


- Added directives hint for validation of the `default_language` field in languages control panel.
  [sneridagh] (#73)


Bug fixes:


- Added missing Zope dependency.
  [maurits] (#64)


5.0.2 (2023-10-07)
------------------

Internal:


- Update configuration files.
  [plone devs] (cfffba8c)


5.0.1 (2023-03-21)
------------------

Bug fixes:


- Correctly specified dependencies.  ``plone.supermodel`` and a few others were missing.
  [plone devs] (#49)


Internal:


- Update configuration files.
  [plone devs] (25f71b87)


5.0.0 (2022-11-30)
------------------

Bug fixes:


- Fixed error in listAvailableLanguageInformation (#40)
- Final release.
  [gforcada] (#600)


5.0.0b1 (2022-09-01)
--------------------

New features:


- Add some more native names to language-country combinations
  [erral] (#45)
- Fix the missing native names for language-country variants
  [erral] (#46)


Bug fixes:


- Added native names for German and Dutch country-specific language variants.
  Then all related language variants are shown together in the language control panel.
  [maurits] (#824)


5.0.0a5 (2022-06-07)
--------------------

Breaking changes:


- Use SVG Flags in Language Selector
  Update Name of Flags
  Prepare of use the Icon Resolver in Plone 6
  [1letter, jensens] (#42)


5.0.0a4 (2022-01-28)
--------------------

Bug fixes:


- Tests: call self.publish with handle_errors=False.
  [maurits] (#41)


5.0.0a3 (2021-10-20)
--------------------

New features:


- Let the sr language be Latin: Sprski.
  If you want to use the Cyrillic character set variant,
  set environment variable `zope_i18n_allowed_languages` to `sr@Cyrl`.
  [maurits] (#326)


5.0.0a2 (2021-10-16)
--------------------

New features:


- Support Cyrillic and Latin character sets for Serbian.
  See `locales issue 326 <https://github.com/collective/plone.app.locales/issues/326>`_.
  [maurits, fredvd] (#326)


5.0.0a1 (2021-09-01)
--------------------

Breaking changes:


- Drop support of Python 2 [jensens] (#31)


New features:


- Make it work with newwest Unidecode 1.2.0. 
  Use its method instead of duplicating it in here.
  Also support newer unicode chars, like with `Bei Jing` in the example.
  [gogobd, jensens, alert] (#31)


4.0.6 (2020-04-20)
------------------

Bug fixes:


- Minor packaging updates. (#1)


4.0.5 (2019-06-27)
------------------

Bug fixes:


- bugfix Shortname starts "b" in Japanese https://github.com/plone/Products.CMFPlone/issues/2901 [terapyon] (#32)


4.0.4 (2019-03-03)
------------------

New features:


- Move the interface `ILanguageSchema` from `Products.CMFPlone.interfaces` to
  this package to avoid install dependency on `Products.CMFPlone` and the whole
  Plone stack. This also breaks the circular reference between those packages.
  [sallner] (#29)


4.0.3 (2019-02-13)
------------------

Bug fixes:


- Be more verbose when Japanese normalizer fails in tests. Test that the length
  of the returned string is lower but not always equal to the given max_length.
  Changed tested string. (#25)


4.0.2 (2018-12-11)
------------------

Bug fixes:

- Code and test cleanuo.
  [jensens]


4.0.1 (2018-10-31)
------------------

Bug fixes:

- Fix py3 tests and functionality
  [pbauer]


4.0.0 (2018-02-02)
------------------

Breaking changes:

- Move PTS Negotiator over form PlacelessTranslationService over to here in order to get rid of PTS itself.
  [jensens, ksuess]

Bug fixes:

- Add Python 2 / 3 compatibility
  [pbauer]


3.0.7 (2017-05-16)
------------------

Bug fixes:

- Add missing entries to requirements in setup.py.
  [dhavlik]


3.0.6 (2016-10-03)
------------------

Bug fixes:

- Code Cleanup: isort, pep8, manual cleanup
  [jensens]


3.0.5 (2016-08-15)
------------------

Fixes:

- Use zope.interface decorator.
  [gforcada]


3.0.4 (2016-03-31)
------------------

Fixes:

- URLNormalizer now removes leading underscores.
  They are disallowed for content objects in zope.
  [do3cc]


3.0.3 (2016-02-19)
------------------

Fixes:

- Fixed test (don't expect role from pac-tests).  [pbauer]


3.0.2 (2015-05-04)
------------------

- Allow calling getPreferedLanguage without parameter again
  [tomgross]


3.0.1 (2015-03-30)
------------------

- Avoid loading of registry on BeforeTraversal breake the request
  [bloodbare]


3.0.0 (2015-03-26)
------------------

- Adapted for Plone5
  [bloodbare]

- Added the tests from Products.PloneLanguageTool
  [bloodbare]

- Added the Products.PloneLanguageTool on this package
  [bloodbare]

- Added the negotiation traverse hook for language negotiation
  [bloodbare]


2.0.9 (2013-08-13)
------------------

- German URL normalizer: handle German ‚single‘ and „double“
  quotation marks, em dash –, paragraph § and € sign.
  [jnachtigall]


2.0.8 (2013-05-26)
------------------

- Add Portuguese normalizer.
  [hvelarde]


2.0.7 (2013-05-23)
------------------

- Fix regression in normalizer: handle POSIX locale identifiers
  in addition to IETF language codes.
  [davisagli]


2.0.6 (2013-04-06)
------------------

- Fixed does not correctly handle client HTTP_ACCEPT_LANGUAGE is
  language/country combination.
  [jianaijun]

2.0.5 (2013-01-13)
------------------

- Revert 97645c76f5e0cf14e525f702c66fe0c4de8cb0fc.
  [esteele]


2.0.4 (2013-01-13)
------------------

- Add Latvian flag to language list
  [maartenkling]

2.0.3 (2012-10-16)
------------------

- Removed unknown cctld entry for um.
  [hannosch]

- Added new cctld entries for: asia, kp, ss and xxx.
  [hannosch]

- Added new country codes and flags for: bl, bq, cw, mf, ss and sx.
  [hannosch]

- Clarify and test availability of reserved country codes an and cs.
  [hannosch]

- Clarify and test availability of deprecated language codes mo and sh.
  [hannosch]

- Removed invalid me language code added in 2007. me is only a country code.
  [hannosch]

- Correct language code for Javanese from jw to jv.
  [hannosch]

- Added missing ISO-639-1 language codes: ae, ak, an, bm, ce, ch, cr, cu, cv,
  dv, ee, ff, ho, ht, hz, ig, ii, io, kg, ki, kj, kr, kv, lg, lu, mh, nb, ng,
  nv, ny, oj, os, pi, sc, vk.
  [hannosch]

- URLNormalizer should remove all ignored characters before making any
  substitutions.
  [esteele]

- Added three new countries and its corresponding flags. Also updated
  the internet top level domains list. Added countries are Kosovo,
  Montenegro and Serbia.
  [alecghica]

- Fixed tests not to fail when a new country, language or domain is added.
  [alecghica]

2.0.2 (2012-08-29)
------------------

- Avoid infinite loop if buggy queryUtility() returns normalizer instance
  of wrong class. Fixes http://dev.plone.org/ticket/11630.
  [patch by Sardtok, applied by kleist]

2.0.1 (2012-07-02)
------------------

- Use `zope.browserresource`.
  [hannosch]

- Converted most tests from doctests to proper unit tests.
  [hannosch]

- Fixed various native names of African languages. Added ``nd``, ``nr`` and
  ``ve`` language codes. Thanks to Dwayne Bailey and Roche Compaan.
  [hannosch]

- The max_length argument was ignored by
  plone.i18n.normalizer.ja.Normalizer.
  [rossp]

2.0 - 2010-07-18
----------------

- Use the standard libraries doctest module.
  [hannosch]

- Update license to GPL version 2 only.
  [hannosch]

1.1b1 - 2010-01-24
------------------

- In practice the Unidecode data didn't produce good enough results for various
  languages. We therefore limit the transliteration approach again to latin-like
  languages and introduce a UNIDECODE_LIMIT. This closes
  http://dev.plone.org/plone/ticket/10107.
  [hannosch]

1.1a3 - 2009-12-27
------------------

- Use the flag of Bangladesh for the Bengali language (code: bn) in general
  and not only for the ``bn-bd`` variant. This closes
  http://dev.plone.org/plone/ticket/9950.
  [hannosch]

- Fixed the IIDNormalizer to generate valid CSS ID or Python variable names as
  specified in its docstring. It no longer tries to preserve filename
  extensions. This closes http://dev.plone.org/plone/ticket/9708.
  [hannosch]

- Added a new explicit base normalizer for Thai, as the Unidecode based
  transliteration isn't good enough.
  [hannosch]

- Added new specific normalizer for Japanese, which avoids the Unidecode based
  transliteration. This refs http://dev.plone.org/plone/ticket/9914.
  [hannosch]

1.1a2 - 2009-12-02
------------------

- Depend on and include ``Unidecode`` based transliterations. These provide
  more meaningful results than unicodedata NFKD normalizations or hex codes.
  [hannosch]

- Added cs-cz combined language code. It solves problem with default language
  on new Plone site creation (Safari/Mac).
  [naro]

- Added catalan flag. This closes
  http://dev.plone.org/plone/ticket/9540
  [ramon]

- Added missing 'native' descriptions to pt-* combined languages.
  [igbun]

1.1a1 - 2009-04-04
------------------

- Removed the negotiator sub-package, as it hasn't been enabled or used yet.
  The functionality is better placed as a WSGI-middleware.
  [hannosch]

- Register all dependencies in setup.py. Move test dependencies into a
  separate extra to keep the dependencies low so things like the normalizer
  can be used in non-zope contexts.
  [wichert]

1.0.9 - Unreleased
------------------

- Added Romanian language as the language for the .ro TLD. This closes
  http://dev.plone.org/plone/ticket/9152
  [vincentfretin]

1.0.8 - 2009-10-15
------------------

- Added new UNDERSCORE_START_REGEX to the file normalizer. This removes any
  leading underscores from uploaded file names. Objects in Zope cannot start
  with an underscore, so it makes little sense to generate suggested file
  names which cannot work.
  [hannosch]

- Added bulgarian normalizer.
  [vlado]

1.0.7 - 2008-11-05
------------------

- Allow _ as a valid character in file names and URLs. Do not remove # from
  file names. It only has a special meaning for URLs.
  [hannosch, sidnei]

1.0.6 - August 18, 2008
-----------------------

- Added normalization for a French-only character (igature of o and e)
  which isn't part of ISO 8859-1. This closes
  http://dev.plone.org/plone/ticket/7512.
  [dbaty, hannosch]

- Fixed the greek character normalization based on a patch by ggozad.
  This closes http://dev.plone.org/plone/ticket/8308.
  [hannosch]

- Changed the default normalization of characters used in Scandinavian
  languages to meet the most common rules. This is based on a discussion
  with translators from all Scandinavian countries.
  [hannosch]

- Added a subdomain language negotiator (e.g. de.plone.org).
  [stefan]

1.0.5 - May 22, 2008
--------------------

- Added a new max_length argument to the normalize method. This allows you
  to override the default values for the maximum length on a call basis.
  [hannosch, fschulze]

- Added a new MAX_URL_LENGTH constant used by the URL normalizer. It
  defaults to 255.
  [hannosch]

- Added '`' to the list of dangerous chars, which will be removed by the
  url and be replaced with a dash by the file name normalizer now.
  [hannosch, mj]

1.0.4 - April 19, 2008
----------------------

- If a dot was used in a url, the url was not lowercased. This closes
  http://dev.plone.org/plone/ticket/7961.
  [hannosch]

1.0.3 - February 13, 2008
-------------------------

- Updating the flag/language listings. Updating readme to include the flag
  mapping logic. This closes http://dev.plone.org/plone/ticket/7441.
  [limi]

- Adding all the Arabic-speaking countries with their respective flags, and
  adding a generic flag to represent Arabic in general (verified to be OK with
  two independent, native residents).
  [limi]

- Added tests for the filename and url request adapters. We have now 100%
  test coverage.
  [hannosch]

- Wrote tests for the locale-aware id normalizer and fixed a bug in it.
  [hannosch]

- Added more tests.
  [hannosch]

- Removed unused and untested 'native' from country information.
  [hannosch]

- Don't allow double quotes in normalized urls.
  This closes http://dev.plone.org/archetypes/ticket/764.
  [hannosch]

1.0.2 - November 24, 2007
-------------------------

- Remove those [] brackets from file names as well.
  [hannosch]

- Increase the maximum filename size to 1023 and make it independently
  configurable.
  [hannosch]

1.0.1 - October 7, 2007
-----------------------

- Extend polish normalizer 'dashed L' to L. This closes
  http://dev.plone.org/plone/ticket/6845.
  [hannosch]

- Added test for filename with non-ascii character and extension. Fixes
  http://dev.plone.org/plone/ticket/7128.
  [dreamcatcher]

1.0 - August 13, 2007
---------------------

- Added Polish normalizer which normalizes 'dashed l' to l. This fixes
  http://dev.plone.org/plone/ticket/6845.
  [hannosch]

1.0rc1 - July 9, 2007
---------------------

- Merged udg-sprint branch. This adds a Zope3-based configurable language
  negotiator with similar functionality as PloneLanguageTool. It is not
  enabled by default.
  [hannosch]

- Added the reference to the Faroese flag.
  [deo]

- Remove more punctuation characters as for example using a comma in the
  title results in a not so friendly ID. This closes
  http://dev.plone.org/plone/ticket/6585.
  [hannosch]

1.0b1 - March 5, 2007
---------------------

- Initial implementation.
  [hannosch]
