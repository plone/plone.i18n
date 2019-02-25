Move the interface `ILanguageSchema` from `Products.CMFPlone.interfaces` to
this package to avoid install dependency on `Products.CMFPlone` and the whole
Plone stack. This also breaks the circular reference between those packages.
[sallner]
