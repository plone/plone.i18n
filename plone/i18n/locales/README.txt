==================
Plone i18n Locales
==================

The plone.i18n.locales subpackage provides flags for countries - naming
conventions follow the ISO3166:1 standard and some language flags whose naming
follow the ISO639-1 standard.

=====================
Flag/language mapping
=====================

The following logic is used with the language/flag mapping:

- If a language is only used in one country, then that flag is mapped to it.
  Example: Finnish (fi and fi-fi)

- If a language is the *only* official language in a country, then that
  country's flag is used. Example: Chile (es-cl) - language is Spanish, but 
  it's the only official language). This is the most common configuration
  when you are using combined language codes (xx-yy), but there are some 
  exceptions.

- If there is more than one official language, then the flags reflect the 
  origin of the language, which may or may not be acceptable, always check
  this. Example: Swedish Finnish (sv-fi) is one of the official languages in
  Finland, but will show the Swedish flag, so the difference can be discerned
  when both fi(-fi) and sv-fi is used with flags. Usually we recommend using
  textual links in these cases, but if you are 100% sure that flags are OK,
  this is what will happen.

- In special cases where we have been told by independent sources that there
  is a flag that represents the collection of countries or grouping that use
  the language, we have included a "language-specific flag" if it exists.
  Examples: Arabic (ar), Esperanto (eo). We still recommend textual links in
  these cases.

There might still be mappings that are wrong, but we have tried to check as 
many of them as possible. If you find any problems, please contact the 
Internationalization list at http://plone.org/support.

We also lack native language representation for a lot of the languages - if
you can help with this, please contact the same list mentioned above.

Remember, this approach makes an assumption that flags are a politically 
non-controversial way of representing language choice in that area - *always*
check if use of flags to represent languages is inappropriate in your context. 
If in doubt, always use textual links instead of flags.
