from plone.i18n.locales.interfaces import IContentLanguageAvailability
from plone.i18n.locales.interfaces import ILanguageAvailability
from plone.i18n.locales.interfaces import IMetadataLanguageAvailability
from zope.interface import implementer

import os


@implementer(ILanguageAvailability)
class LanguageAvailability:
    """A list of available languages."""

    def getAvailableLanguages(self, combined=False):
        """Return a sequence of language tags for available languages."""
        languages = list(_languagelist.keys())
        if combined:
            languages.extend(list(_combinedlanguagelist.keys()))
        return languages

    def getLanguages(self, combined=False):
        """Return a sequence of Language objects for available languages."""
        languages = _languagelist.copy()
        if combined:
            languages.update(_combinedlanguagelist.copy())
        return languages

    def getLanguageListing(self, combined=False):
        """Return a sequence of language code and language name tuples."""
        languages = _languagelist.copy()
        if combined:
            languages.update(_combinedlanguagelist.copy())
        return [(code, languages[code]["name"]) for code in languages]


@implementer(IContentLanguageAvailability)
class ContentLanguageAvailability(LanguageAvailability):
    """A list of available content languages."""


contentlanguages = ContentLanguageAvailability()


@implementer(IMetadataLanguageAvailability)
class MetadataLanguageAvailability(LanguageAvailability):
    """A list of available metadata languages."""


metadatalanguages = MetadataLanguageAvailability()

# This is a dictionary of dictonaries:
#
# 'langcode-variation' : {
#     u'native' : 'Native name',
#     u'name' : 'English name',
#     u'flag' : u'/++resource++country-flags/*.gif'
# }
#
# This list follows ISO-639-1. The list retains entries for mo and sh,
# even tough these have later been deprecated from the standard.

_languagelist = {
    "aa": {
        "native": "магIарул мацI",
        "name": "Afar",
        "flag": "/++resource++country-flags/dj.gif",
    },
    "ab": {
        "native": "бызшәа",
        "name": "Abkhazian",
        "flag": "/++resource++country-flags/ge.gif",
    },
    "ae": {"native": "avesta", "name": "Avestan"},
    "af": {"native": "Afrikaans", "name": "Afrikaans"},
    "ak": {"native": "Akan", "name": "Akan"},
    "am": {"native": "አማርኛ", "name": "Amharic"},
    "an": {"native": "aragonés", "name": "Aragonese"},
    "ar": {
        "native": "العربية",
        "name": "Arabic",
        "flag": "/++resource++language-flags/ar.gif",
    },
    "as": {"native": "অসমিয়া", "name": "Assamese"},
    "ay": {"native": "Aymara", "name": "Aymara"},
    "az": {
        "native": "Azəri Türkçəsi",
        "name": "Azerbaijani",
        "flag": "/++resource++country-flags/az.gif",
    },
    "ba": {"native": "Bashkir", "name": "Bashkir"},
    "be": {
        "native": "Беларускі",
        "name": "Belarussian",
        "flag": "/++resource++country-flags/by.gif",
    },
    "bg": {
        "native": "Български",
        "name": "Bulgarian",
        "flag": "/++resource++country-flags/bg.gif",
    },
    "bh": {"native": "Bihari", "name": "Bihari"},
    "bi": {"native": "Bislama", "name": "Bislama"},
    "bm": {"native": "bamanankan", "name": "Bambara"},
    "bn": {
        "native": "বাংলা",
        "name": "Bengali",
        "flag": "/++resource++country-flags/bd.gif",
    },
    "bo": {"native": "བོད་སྐད་", "name": "Tibetan"},
    "br": {"native": "brezhoneg", "name": "Breton"},
    "bs": {
        "native": "Bosanski",
        "name": "Bosnian",
        "flag": "/++resource++country-flags/ba.gif",
    },
    "ca": {
        "native": "Català",
        "name": "Catalan",
        "flag": "/++resource++language-flags/ca.gif",
    },
    "ce": {"native": "нохчийн мотт", "name": "Chechen"},
    "ch": {"native": "Chamoru", "name": "Chamorro"},
    "co": {"native": "Corsu", "name": "Corsican"},
    "cr": {"native": "ᓀᐦᐃᔭᐍᐏᐣ", "name": "Cree"},
    "cs": {
        "native": "Čeština",
        "name": "Czech",
        "flag": "/++resource++country-flags/cz.gif",
    },
    "cu": {"native": "ѩзыкъ словѣньскъ", "name": "Old Church Slavonic"},
    "cv": {"native": "чӑваш чӗлхи", "name": "Chuvash"},
    "cy": {
        "native": "Cymraeg",
        "name": "Welsh",
        "flag": "/++resource++language-flags/cy.gif",
    },
    "da": {
        "native": "Dansk",
        "name": "Danish",
        "flag": "/++resource++country-flags/dk.gif",
    },
    "de": {
        "native": "Deutsch",
        "name": "German",
        "flag": "/++resource++country-flags/de.gif",
    },
    "dv": {"native": "Divehi", "name": "Maldivian"},
    "dz": {"native": "Bhutani", "name": "Indian Bhutani"},
    "ee": {"native": "Eʋegbe", "name": "Ewe"},
    "el": {
        "native": "Ελληνικά",
        "name": "Greek",
        "flag": "/++resource++country-flags/gr.gif",
    },
    "en": {
        "native": "English",
        "name": "English",
        "flag": "/++resource++country-flags/gb.gif",
    },
    "eo": {
        "native": "Esperanto",
        "name": "Esperanto",
        "flag": "/++resource++language-flags/eo.gif",
    },
    "es": {
        "native": "Español",
        "name": "Spanish",
        "flag": "/++resource++country-flags/es.gif",
    },
    "et": {
        "native": "Eesti",
        "name": "Estonian",
        "flag": "/++resource++country-flags/ee.gif",
    },
    "eu": {
        "native": "Euskara",
        "name": "Basque",
        "flag": "/++resource++language-flags/eu.gif",
    },
    "fa": {"native": "فارسی", "name": "Persian"},
    "ff": {"native": "Fulfulde", "name": "Fula"},
    "fi": {
        "native": "Suomi",
        "name": "Finnish",
        "flag": "/++resource++country-flags/fi.gif",
    },
    "fj": {
        "native": "Fiji",
        "name": "Fiji",
        "flag": "/++resource++country-flags/fj.gif",
    },
    "fo": {
        "native": "Føroyska",
        "name": "Faroese",
        "flag": "/++resource++country-flags/fo.gif",
    },
    "fr": {
        "native": "Français",
        "name": "French",
        "flag": "/++resource++country-flags/fr.gif",
    },
    "fy": {"native": "Frysk", "name": "Frisian"},
    "ga": {"native": "Gaeilge", "name": "Irish Gaelic"},
    "gd": {"native": "Gàidhlig", "name": "Scottish Gaelic"},
    "gl": {"native": "Galego", "name": "Galician"},
    "gn": {"native": "Guarani", "name": "Guarani"},
    "gu": {"native": "ગુજરાતી", "name": "Gujarati"},
    "gv": {"native": "Gaelg", "name": "Manx Gaelic"},
    "ha": {"native": "هَوُس", "name": "Hausa"},
    "he": {
        "native": "עברית",
        "name": "Hebrew",
        "flag": "/++resource++country-flags/il.gif",
    },
    "hi": {
        "native": "हिंदी",
        "name": "Hindi",
        "flag": "/++resource++country-flags/in.gif",
    },
    "ho": {"native": "Hiri Motu", "name": "Hiri Motu"},
    "hr": {
        "native": "Hrvatski",
        "name": "Croatian",
        "flag": "/++resource++country-flags/hr.gif",
    },
    "ht": {"native": "Kreyòl ayisyen", "name": "Haitian"},
    "hu": {
        "native": "Magyar",
        "name": "Hungarian",
        "flag": "/++resource++country-flags/hu.gif",
    },
    "hy": {
        "native": "Հայերէն",
        "name": "Armenian",
        "flag": "/++resource++country-flags/am.gif",
    },
    "hz": {"native": "Otjiherero", "name": "Herero"},
    "ia": {"native": "Interlingua", "name": "Interlingua"},
    "id": {
        "native": "Bahasa Indonesia",
        "name": "Indonesian",
        "flag": "/++resource++country-flags/id.gif",
    },
    "ie": {"native": "Interlingue", "name": "Interlingue"},
    "ig": {"native": "Asụsụ Igbo", "name": "Igbo"},
    "ii": {"native": "Nuosu", "name": "Nuosu"},
    "ik": {"native": "Iñupiaq", "name": "Inupiak"},
    "io": {"native": "Ido", "name": "Ido"},
    "is": {
        "native": "Íslenska",
        "name": "Icelandic",
        "flag": "/++resource++country-flags/is.gif",
    },
    "it": {
        "native": "Italiano",
        "name": "Italian",
        "flag": "/++resource++country-flags/it.gif",
    },
    "iu": {"native": "ᐃᓄᒃᑎᑐᑦ", "name": "Inuktitut"},
    "ja": {
        "native": "日本語",
        "name": "Japanese",
        "flag": "/++resource++country-flags/jp.gif",
    },
    "jv": {"native": "Javanese", "name": "basa Jawa"},
    "ka": {
        "native": "ქართული",
        "name": "Georgian",
        "flag": "/++resource++country-flags/ge.gif",
    },
    "kg": {"native": "KiKongo", "name": "Kongo"},
    "ki": {"native": "Gĩkũyũ", "name": "Kikuyu"},
    "kj": {"native": "Kuanyama", "name": "Kwanyama"},
    "kk": {
        "native": "ﻗﺎﺯﺍﻗﺸﺎ",
        "name": "Kazakh",
        "flag": "/++resource++country-flags/kz.gif",
    },
    "kl": {
        "native": "Greenlandic",
        "name": "Greenlandic",
        "flag": "/++resource++country-flags/gl.gif",
    },
    "km": {
        "native": "ខ្មែរ",
        "name": "Cambodian/Khmer",
        "flag": "/++resource++country-flags/kh.gif",
    },
    "kn": {
        "native": "ಕನ್ನಡ",
        "name": "Kannada",
        "flag": "/++resource++country-flags/in.gif",
    },
    "ko": {
        "native": "한국어",
        "name": "Korean",
        "flag": "/++resource++country-flags/kr.gif",
    },
    "kr": {"native": "Kanuri", "name": "Kanuri"},
    "ks": {
        "native": "काऽशुर",
        "name": "Kashmiri",
        "flag": "/++resource++country-flags/in.gif",
    },
    "ku": {"native": "Kurdí", "name": "Kurdish"},
    "kv": {"native": "коми кыв", "name": "Komi"},
    "kw": {"native": "Kernewek", "name": "Cornish"},
    "ky": {"native": "Кыргыз", "name": "Kirghiz"},
    "la": {
        "native": "Latin",
        "name": "Latin",
        "flag": "/++resource++country-flags/va.gif",
    },
    "lb": {
        "native": "Lëtzebuergesch",
        "name": "Luxemburgish",
        "flag": "/++resource++country-flags/lu.gif",
    },
    "lg": {"native": "Luganda", "name": "Ganda"},
    "li": {"native": "Limburgs", "name": "Limburgish"},
    "ln": {"native": "Lingala", "name": "Lingala"},
    "lo": {
        "native": "ພາສາລາວ",
        "name": "Laotian",
        "flag": "/++resource++country-flags/la.gif",
    },
    "lt": {
        "native": "Lietuvių",
        "name": "Lithuanian",
        "flag": "/++resource++country-flags/lt.gif",
    },
    "lu": {"native": "Tshiluba", "name": "Luba-Katanga"},
    "lv": {
        "native": "Latviešu",
        "name": "Latvian",
        "flag": "/++resource++country-flags/lv.gif",
    },
    "mg": {
        "native": "Malagasy",
        "name": "Madagascarian",
        "flag": "/++resource++country-flags/mg.gif",
    },
    "mh": {"native": "Kajin M̧ajeļ", "name": "Marshallese"},
    "mi": {"native": "Maori", "name": "Maori"},
    "mk": {
        "native": "Македонски",
        "name": "Macedonian",
        "flag": "/++resource++country-flags/mk.gif",
    },
    "ml": {"native": "മലയാളം", "name": "Malayalam"},
    "mn": {
        "native": "Монгол",
        "name": "Mongolian",
        "flag": "/++resource++country-flags/mn.gif",
    },
    "mo": {
        "native": "Moldavian",
        "name": "Moldavian",
        "flag": "/++resource++country-flags/md.gif",
    },
    "mr": {"native": "मराठी", "name": "Marathi"},
    "ms": {"native": "Bahasa Melayu", "name": "Malay"},
    "mt": {
        "native": "Malti",
        "name": "Maltese",
        "flag": "/++resource++country-flags/mt.gif",
    },
    "my": {"native": "Burmese", "name": "Burmese"},
    "na": {
        "native": "Nauru",
        "name": "Nauruan",
        "flag": "/++resource++country-flags/nr.gif",
    },
    "nb": {"native": "Norsk bokmål", "name": "Norwegian Bokmål"},
    "nd": {"native": "Ndebele (North)", "name": "Ndebele (North)"},
    "ne": {"native": "नेपाली", "name": "Nepali"},
    "ng": {"native": "Owambo", "name": "Ndonga"},
    "nl": {
        "native": "Nederlands",
        "name": "Dutch",
        "flag": "/++resource++country-flags/nl.gif",
    },
    "nn": {
        "native": "Nynorsk",
        "name": "Nynorsk",
        "flag": "/++resource++country-flags/no.gif",
    },
    "no": {
        "native": "Norsk",
        "name": "Norwegian",
        "flag": "/++resource++country-flags/no.gif",
    },
    "nr": {"native": "IsiNdebele", "name": "Ndebele (South)"},
    "nv": {"native": "Diné bizaad", "name": "Navajo"},
    "ny": {"native": "chiCheŵa", "name": "Chichewa"},
    "oc": {"native": "Occitan", "name": "Occitan"},
    "oj": {"native": "ᐊᓂᔑᓈᐯᒧᐎᓐ", "name": "Ojibwe"},
    "om": {"native": "Oromo", "name": "Oromo"},
    "or": {"native": "ଓଡ଼ିଆ", "name": "Oriya"},
    "os": {"native": "ирон æвзаг", "name": "Ossetian"},
    "pa": {"native": "ਪੰਜਾਬੀ", "name": "Punjabi"},
    "pi": {"native": "पाऴि", "name": "Pāli"},
    "pl": {
        "native": "Polski",
        "name": "Polish",
        "flag": "/++resource++country-flags/pl.gif",
    },
    "ps": {"native": "پښتو", "name": "Pashto"},
    "pt": {
        "native": "Português",
        "name": "Portuguese",
        "flag": "/++resource++country-flags/pt.gif",
    },
    "qu": {"native": "Quechua", "name": "Quechua"},
    "rm": {"native": "Rhaeto-Romance", "name": "Rhaeto-Romance"},
    "rn": {"native": "Kirundi", "name": "Kirundi"},
    "ro": {
        "native": "Română",
        "name": "Romanian",
        "flag": "/++resource++country-flags/ro.gif",
    },
    "ru": {
        "native": "Русский",
        "name": "Russian",
        "flag": "/++resource++country-flags/ru.gif",
    },
    "rw": {"native": "Kinyarwanda", "name": "Kinyarwanda"},
    "sa": {"native": "संस्कृत", "name": "Sanskrit"},
    "sc": {"native": "sardu", "name": "Sardinian"},
    "sd": {
        "native": "Sindhi",
        "name": "Sindhi",
        "flag": "/++resource++country-flags/pk.gif",
    },
    "se": {"native": "Northern Sámi", "name": "Northern Sámi"},
    "sg": {
        "native": "Sangho",
        "name": "Sangho",
        "flag": "/++resource++country-flags/cf.gif",
    },
    "sh": {"native": "Serbo-Croatian", "name": "Serbo-Croatian"},
    "si": {"native": "Singhalese", "name": "Singhalese"},
    "sk": {
        "native": "Slovenčina",
        "name": "Slovak",
        "flag": "/++resource++country-flags/sk.gif",
    },
    "sl": {
        "native": "Slovenščina",
        "name": "Slovenian",
        "flag": "/++resource++country-flags/si.gif",
    },
    "sm": {"native": "Samoan", "name": "Samoan"},
    "sn": {"native": "Shona", "name": "Shona"},
    "so": {
        "native": "Somali",
        "name": "Somali",
        "flag": "/++resource++country-flags/so.gif",
    },
    "sq": {
        "native": "Shqip",
        "name": "Albanian",
        "flag": "/++resource++country-flags/al.gif",
    },
    "sr": {
        # Note: we support two character sets for this language.
        # See zope_i18n_allowed_languages below.
        # Until and including 5.2, native was Cyrillic: српски.
        # In Plone 6.0 native became Latin: Srpski.
        "native": "Srpski",
        "name": "Serbian",
        "flag": "/++resource++country-flags/cs.gif",
    },
    "ss": {"native": "SiSwati", "name": "Swati"},
    "st": {"native": "Sesotho", "name": "Southern Sotho"},
    "su": {
        "native": "Sudanese",
        "name": "Sudanese",
        "flag": "/++resource++country-flags/sd.gif",
    },
    "sv": {
        "native": "Svenska",
        "name": "Swedish",
        "flag": "/++resource++country-flags/se.gif",
    },
    "sw": {"native": "Kiswahili", "name": "Swahili"},
    "ta": {"native": "தமிழ", "name": "Tamil"},
    "te": {"native": "తెలుగు", "name": "Telugu"},
    "tg": {
        "native": "Тоҷики",
        "name": "Tadjik",
        "flag": "/++resource++country-flags/tj.gif",
    },
    "th": {
        "native": "ไทย",
        "name": "Thai",
        "flag": "/++resource++country-flags/th.gif",
    },
    "ti": {"native": "ትግርኛ", "name": "Tigrinya"},
    "tk": {
        "native": "түркmенче",
        "name": "Turkmen",
        "flag": "/++resource++country-flags/tm.gif",
    },
    "tl": {"native": "Tagalog", "name": "Tagalog"},
    "tn": {
        "native": "Setswana",
        "name": "Tswana",
        "flag": "/++resource++country-flags/bw.gif",
    },
    "to": {"native": "Tonga", "name": "Tonga"},
    "tr": {
        "native": "Türkçe",
        "name": "Turkish",
        "flag": "/++resource++country-flags/tr.gif",
    },
    "ts": {"native": "Xitsonga", "name": "Tsonga"},
    "tt": {"native": "татарча", "name": "Tatar"},
    "tw": {"native": "Twi", "name": "Twi"},
    "ty": {"native": "Reo Tahiti", "name": "Tahitian"},
    "ug": {"native": "Uigur", "name": "Uigur"},
    "uk": {
        "native": "Українська",
        "name": "Ukrainian",
        "flag": "/++resource++country-flags/ua.gif",
    },
    "ur": {"native": "اردو", "name": "Urdu"},
    "uz": {
        "native": "Ўзбекча",
        "name": "Uzbek",
        "flag": "/++resource++country-flags/uz.gif",
    },
    "ve": {"native": "Tshivenḓa", "name": "Venda"},
    "vi": {
        "native": "Tiếng Việt",
        "name": "Vietnamese",
        "flag": "/++resource++country-flags/vn.gif",
    },
    "vk": {"native": "Ovalingo", "name": "Viking"},
    "vo": {"native": "Volapük", "name": "Volapük"},
    "wa": {"native": "Walon", "name": "Walloon"},
    "wo": {"native": "Wolof", "name": "Wolof"},
    "xh": {"native": "IsiXhosa", "name": "Xhosa"},
    "yi": {
        "native": "ײִדיש",
        "name": "Yiddish",
        "flag": "/++resource++country-flags/il.gif",
    },
    "yo": {"native": "Yorùbá", "name": "Yorouba"},
    "za": {"native": "Zhuang", "name": "Zhuang"},
    "zh": {
        "native": "中文",
        "name": "Chinese",
        "flag": "/++resource++country-flags/cn.gif",
    },
    "zu": {
        "native": "IsiZulu",
        "name": "Zulu",
        "flag": "/++resource++country-flags/za.gif",
    },
}

# Character sets are a thing now.
# See https://github.com/collective/plone.app.locales/issues/326
# At the moment only for Serbian.
_zope_i18n_allowed_languages = os.environ.get("zope_i18n_allowed_languages", "")
if "sr@Latn" in _zope_i18n_allowed_languages:
    _languagelist["sr"] = {
        "native": "Srpski",
        "name": "Serbian (Latin)",
        "flag": "/++resource++country-flags/cs.gif",
    }
elif "sr@Cyrl" in _zope_i18n_allowed_languages:
    _languagelist["sr"] = {
        "native": "српски",
        "name": "Serbian (Cyrillic)",
        "flag": "/++resource++country-flags/cs.gif",
    }

# convert the utf-8 encoded values to unicode
for code in _languagelist:
    value = _languagelist[code]
    if "name" in value:
        value["name"] = value["name"]
    if "native" in value:
        value["native"] = value["native"]

_combinedlanguagelist = {
    "ar-ae": {
        "name": "Arabic (United Arab Emirates)",
        "flag": "/++resource++country-flags/ae.gif",
    },
    "ar-bh": {
        "name": "Arabic (Bahrain)",
        "flag": "/++resource++country-flags/bh.gif",
    },
    "ar-dz": {
        "name": "Arabic (Algeria)",
        "flag": "/++resource++country-flags/dz.gif",
    },
    "ar-eg": {
        "name": "Arabic (Egypt)",
        "flag": "/++resource++country-flags/eg.gif",
    },
    "ar-il": {
        "name": "Arabic (Israel)",
        "flag": "/++resource++country-flags/il.gif",
    },
    "ar-iq": {
        "name": "Arabic (Iraq)",
        "flag": "/++resource++country-flags/iq.gif",
    },
    "ar-jo": {
        "name": "Arabic (Jordan)",
        "flag": "/++resource++country-flags/jo.gif",
    },
    "ar-kw": {
        "name": "Arabic (Kuwait)",
        "flag": "/++resource++country-flags/kw.gif",
    },
    "ar-lb": {
        "name": "Arabic (Lebanon)",
        "flag": "/++resource++country-flags/lb.gif",
    },
    "ar-ly": {
        "name": "Arabic (Libya)",
        "flag": "/++resource++country-flags/ly.gif",
    },
    "ar-ma": {
        "name": "Arabic (Morocco)",
        "flag": "/++resource++country-flags/ma.gif",
    },
    "ar-mr": {
        "name": "Arabic (Mauritania)",
        "flag": "/++resource++country-flags/mr.gif",
    },
    "ar-om": {
        "name": "Arabic (Oman)",
        "flag": "/++resource++country-flags/om.gif",
    },
    "ar-ps": {
        "name": "Arabic (Palestinian West Bank and Gaza)",
        "flag": "/++resource++country-flags/ps.gif",
    },
    "ar-qa": {
        "name": "Arabic (Qatar)",
        "flag": "/++resource++country-flags/qa.gif",
    },
    "ar-sa": {
        "name": "Arabic (Saudi Arabia)",
        "flag": "/++resource++country-flags/sa.gif",
    },
    "ar-sd": {
        "name": "Arabic (Sudan)",
        "flag": "/++resource++country-flags/ly.gif",
    },
    "ar-so": {
        "name": "Arabic (Somalia)",
        "flag": "/++resource++country-flags/so.gif",
    },
    "ar-sy": {
        "name": "Arabic (Syria)",
        "flag": "/++resource++country-flags/sy.gif",
    },
    "ar-td": {
        "name": "Arabic (Chad)",
        "flag": "/++resource++country-flags/td.gif",
    },
    "ar-tn": {
        "name": "Arabic (Tunisia)",
        "flag": "/++resource++country-flags/ly.gif",
    },
    "ar-ye": {
        "name": "Arabic (Yemen)",
        "flag": "/++resource++country-flags/ye.gif",
    },
    "bn-bd": {
        "name": "Bengali (Bangladesh)",
        "flag": "/++resource++country-flags/bd.gif",
    },
    "bn-in": {
        "name": "Bengali (India)",
        "flag": "/++resource++country-flags/in.gif",
    },
    "bn-sg": {
        "name": "Bengali (Singapore)",
        "flag": "/++resource++country-flags/sg.gif",
    },
    "ch-gu": {
        "name": "Chamorro (Guam)",
        "flag": "/++resource++country-flags/gu.gif",
    },
    "ch-mp": {
        "name": "Chamorro (Northern Mariana Islands)",
        "flag": "/++resource++country-flags/mp.gif",
    },
    "cs-cz": {
        "name": "Czech (Czech republic)",
        "native": "Čeština (Česká republika)",
        "flag": "/++resource++country-flags/cz.gif",
    },
    "da-dk": {
        "name": "Danish (Denmark)",
        "flag": "/++resource++country-flags/dk.gif",
    },
    "da-gl": {
        "name": "Danish (Greenland)",
        "flag": "/++resource++country-flags/gl.gif",
    },
    "de-at": {
        "name": "German (Austria)",
        "native": "Deutsch (Österreich)",
        "flag": "/++resource++country-flags/at.gif",
    },
    "de-be": {
        "name": "German (Belgium)",
        "flag": "/++resource++country-flags/de.gif",
    },
    "de-ch": {
        "name": "German (Switzerland)",
        "flag": "/++resource++country-flags/ch.gif",
    },
    "de-de": {
        "name": "German (Germany)",
        "flag": "/++resource++country-flags/de.gif",
    },
    "de-dk": {
        "name": "German (Denmark)",
        "flag": "/++resource++country-flags/de.gif",
    },
    "de-li": {
        "name": "German (Liechtenstein)",
        "flag": "/++resource++country-flags/li.gif",
    },
    "de-lu": {
        "name": "German (Luxembourg)",
        "flag": "/++resource++country-flags/de.gif",
    },
    "el-cy": {
        "name": "Greek (Cyprus)",
        "flag": "/++resource++country-flags/cy.gif",
    },
    "el-gr": {
        "name": "Greek (Greece)",
        "flag": "/++resource++country-flags/gr.gif",
    },
    "en-ag": {
        "name": "English (Antigua and Barbuda)",
        "flag": "/++resource++country-flags/ag.gif",
    },
    "en-ai": {
        "name": "English (Anguilla)",
        "flag": "/++resource++country-flags/ai.gif",
    },
    "en-as": {
        "name": "English (American Samoa)",
        "flag": "/++resource++country-flags/as.gif",
    },
    "en-au": {
        "name": "English (Australia)",
        "flag": "/++resource++country-flags/au.gif",
    },
    "en-bb": {
        "name": "English (Barbados)",
        "flag": "/++resource++country-flags/bb.gif",
    },
    "en-bm": {
        "name": "English (Bermuda)",
        "flag": "/++resource++country-flags/bm.gif",
    },
    "en-bn": {
        "name": "English (Brunei)",
        "flag": "/++resource++country-flags/bn.gif",
    },
    "en-bs": {
        "name": "English (Bahamas)",
        "flag": "/++resource++country-flags/bs.gif",
    },
    "en-bw": {
        "name": "English (Botswana)",
        "flag": "/++resource++country-flags/bw.gif",
    },
    "en-bz": {
        "name": "English (Belize)",
        "flag": "/++resource++country-flags/bz.gif",
    },
    "en-ca": {
        "name": "English (Canada)",
        "flag": "/++resource++country-flags/ca.gif",
    },
    "en-ck": {
        "name": "English (Cook Islands)",
        "flag": "/++resource++country-flags/ck.gif",
    },
    "en-cm": {
        "name": "English (Cameroon)",
        "flag": "/++resource++country-flags/cm.gif",
    },
    "en-dm": {
        "name": "English (Dominica)",
        "flag": "/++resource++country-flags/dm.gif",
    },
    "en-er": {
        "name": "English (Eritrea)",
        "flag": "/++resource++country-flags/er.gif",
    },
    "en-et": {
        "name": "English (Ethiopia)",
        "flag": "/++resource++country-flags/et.gif",
    },
    "en-fj": {
        "name": "English (Fiji)",
        "flag": "/++resource++country-flags/fj.gif",
    },
    "en-fk": {
        "name": "English (Falkland Islands)",
        "flag": "/++resource++country-flags/fk.gif",
    },
    "en-fm": {
        "name": "English (Micronesia)",
        "flag": "/++resource++country-flags/fm.gif",
    },
    "en-gb": {
        "name": "English (United Kingdom)",
        "flag": "/++resource++country-flags/gb.gif",
    },
    "en-gd": {
        "name": "English (Grenada)",
        "flag": "/++resource++country-flags/gd.gif",
    },
    "en-gh": {
        "name": "English (Ghana)",
        "flag": "/++resource++country-flags/gh.gif",
    },
    "en-gi": {
        "name": "English (Gibraltar)",
        "flag": "/++resource++country-flags/gi.gif",
    },
    "en-gm": {
        "name": "English (Gambia)",
        "flag": "/++resource++country-flags/gm.gif",
    },
    "en-gu": {
        "name": "English (Guam)",
        "flag": "/++resource++country-flags/gu.gif",
    },
    "en-gy": {
        "name": "English (Guyana)",
        "flag": "/++resource++country-flags/gy.gif",
    },
    "en-ie": {
        "name": "English (Ireland)",
        "flag": "/++resource++country-flags/ie.gif",
    },
    "en-il": {
        "name": "English (Israel)",
        "flag": "/++resource++country-flags/gb.gif",
    },
    "en-io": {
        "name": "English (British Indian Ocean Territory)",
        "flag": "/++resource++country-flags/io.gif",
    },
    "en-jm": {
        "name": "English (Jamaica)",
        "flag": "/++resource++country-flags/jm.gif",
    },
    "en-ke": {
        "name": "English (Kenya)",
        "flag": "/++resource++country-flags/ke.gif",
    },
    "en-ki": {
        "name": "English (Kiribati)",
        "flag": "/++resource++country-flags/ki.gif",
    },
    "en-kn": {
        "name": "English (St. Kitts-Nevis)",
        "flag": "/++resource++country-flags/kn.gif",
    },
    "en-ky": {
        "name": "English (Cayman Islands)",
        "flag": "/++resource++country-flags/ky.gif",
    },
    "en-lc": {
        "name": "English (St. Lucia)",
        "flag": "/++resource++country-flags/lc.gif",
    },
    "en-lr": {
        "name": "English (Liberia)",
        "flag": "/++resource++country-flags/lr.gif",
    },
    "en-ls": {
        "name": "English (Lesotho)",
        "flag": "/++resource++country-flags/ls.gif",
    },
    "en-mp": {
        "name": "English (Northern Mariana Islands)",
        "flag": "/++resource++country-flags/mp.gif",
    },
    "en-ms": {
        "name": "English (Montserrat)",
        "flag": "/++resource++country-flags/ms.gif",
    },
    "en-mt": {
        "name": "English (Malta)",
        "flag": "/++resource++country-flags/mt.gif",
    },
    "en-mu": {
        "name": "English (Mauritius)",
        "flag": "/++resource++country-flags/mu.gif",
    },
    "en-mw": {
        "name": "English (Malawi)",
        "flag": "/++resource++country-flags/mw.gif",
    },
    "en-na": {
        "name": "English (Namibia)",
        "flag": "/++resource++country-flags/na.gif",
    },
    "en-nf": {
        "name": "English (Norfolk Island)",
        "flag": "/++resource++country-flags/nf.gif",
    },
    "en-ng": {
        "name": "English (Nigeria)",
        "flag": "/++resource++country-flags/ng.gif",
    },
    "en-nr": {
        "name": "English (Nauru)",
        "flag": "/++resource++country-flags/nr.gif",
    },
    "en-nu": {
        "name": "English (Niue)",
        "flag": "/++resource++country-flags/nu.gif",
    },
    "en-nz": {
        "name": "English (New Zealand)",
        "flag": "/++resource++country-flags/nz.gif",
    },
    "en-pg": {
        "name": "English (Papua New Guinea)",
        "flag": "/++resource++country-flags/pg.gif",
    },
    "en-ph": {
        "name": "English (Philippines)",
        "flag": "/++resource++country-flags/ph.gif",
    },
    "en-pk": {
        "name": "English (Pakistan)",
        "flag": "/++resource++country-flags/pk.gif",
    },
    "en-pn": {
        "name": "English (Pitcairn)",
        "flag": "/++resource++country-flags/pn.gif",
    },
    "en-pr": {
        "name": "English (Puerto Rico)",
        "flag": "/++resource++country-flags/pr.gif",
    },
    "en-pw": {
        "name": "English (Palau)",
        "flag": "/++resource++country-flags/pw.gif",
    },
    "en-rw": {
        "name": "English (Rwanda)",
        "flag": "/++resource++country-flags/rw.gif",
    },
    "en-sb": {
        "name": "English (Solomon Islands)",
        "flag": "/++resource++country-flags/sb.gif",
    },
    "en-sc": {
        "name": "English (Seychelles)",
        "flag": "/++resource++country-flags/sc.gif",
    },
    "en-sg": {
        "name": "English (Singapore)",
        "flag": "/++resource++country-flags/sg.gif",
    },
    "en-sh": {
        "name": "English (St. Helena)",
        "flag": "/++resource++country-flags/sh.gif",
    },
    "en-sl": {
        "name": "English (Sierra Leone)",
        "flag": "/++resource++country-flags/sl.gif",
    },
    "en-so": {
        "name": "English (Somalia)",
        "flag": "/++resource++country-flags/so.gif",
    },
    "en-sz": {
        "name": "English (Swaziland)",
        "flag": "/++resource++country-flags/sz.gif",
    },
    "en-tc": {
        "name": "English (Turks and Caicos Islands)",
        "flag": "/++resource++country-flags/tc.gif",
    },
    "en-tk": {
        "name": "English (Tokelau)",
        "flag": "/++resource++country-flags/tk.gif",
    },
    "en-to": {
        "name": "English (Tonga)",
        "flag": "/++resource++country-flags/to.gif",
    },
    "en-tt": {
        "name": "English (Trinidad and Tobago)",
        "flag": "/++resource++country-flags/tt.gif",
    },
    "en-ug": {
        "name": "English (Uganda)",
        "flag": "/++resource++country-flags/ug.gif",
    },
    "en-us": {
        "name": "English (USA)",
        "flag": "/++resource++country-flags/us.gif",
    },
    "en-vc": {
        "name": "English (St. Vincent and the Grenadi)",
        "flag": "/++resource++country-flags/vc.gif",
    },
    "en-vg": {
        "name": "English (British Virgin Islands)",
        "flag": "/++resource++country-flags/vg.gif",
    },
    "en-vi": {
        "name": "English (U.S. Virgin Islands)",
        "flag": "/++resource++country-flags/vi.gif",
    },
    "en-vu": {
        "name": "English (Vanuatu)",
        "flag": "/++resource++country-flags/vu.gif",
    },
    "en-ws": {
        "name": "English (Western Samoa)",
        "flag": "/++resource++country-flags/ws.gif",
    },
    "en-za": {
        "name": "English (South Africa)",
        "flag": "/++resource++country-flags/za.gif",
    },
    "en-zm": {
        "name": "English (Zambia)",
        "flag": "/++resource++country-flags/zm.gif",
    },
    "en-zw": {
        "name": "English (Zimbabwe)",
        "flag": "/++resource++country-flags/zw.gif",
    },
    "es-ar": {
        "name": "Spanish (Argentina)",
        "flag": "/++resource++country-flags/ar.gif",
    },
    "es-bo": {
        "name": "Spanish (Bolivia)",
        "flag": "/++resource++country-flags/bo.gif",
    },
    "es-cl": {
        "name": "Spanish (Chile)",
        "flag": "/++resource++country-flags/cl.gif",
    },
    "es-co": {
        "name": "Spanish (Colombia)",
        "flag": "/++resource++country-flags/co.gif",
    },
    "es-cr": {
        "name": "Spanish (Costa Rica)",
        "flag": "/++resource++country-flags/cr.gif",
    },
    "es-cu": {
        "name": "Spanish (Cuba)",
        "flag": "/++resource++country-flags/cu.gif",
    },
    "es-do": {
        "name": "Spanish (Dominican Republic)",
        "flag": "/++resource++country-flags/do.gif",
    },
    "es-ec": {
        "name": "Spanish (Ecuador)",
        "flag": "/++resource++country-flags/ec.gif",
    },
    "es-es": {
        "name": "Spanish (Spain)",
        "flag": "/++resource++country-flags/es.gif",
    },
    "es-gq": {
        "name": "Spanish (Equatorial Guinea)",
        "flag": "/++resource++country-flags/gq.gif",
    },
    "es-gt": {
        "name": "Spanish (Guatemala)",
        "flag": "/++resource++country-flags/gt.gif",
    },
    "es-hn": {
        "name": "Spanish (Honduras)",
        "flag": "/++resource++country-flags/hn.gif",
    },
    "es-mx": {
        "name": "Spanish (Mexico)",
        "flag": "/++resource++country-flags/mx.gif",
    },
    "es-ni": {
        "name": "Spanish (Nicaragua)",
        "flag": "/++resource++country-flags/ni.gif",
    },
    "es-pa": {
        "name": "Spanish (Panama)",
        "flag": "/++resource++country-flags/pa.gif",
    },
    "es-pe": {
        "name": "Spanish (Peru)",
        "flag": "/++resource++country-flags/pe.gif",
    },
    "es-pr": {
        "name": "Spanish (Puerto Rico)",
        "flag": "/++resource++country-flags/pr.gif",
    },
    "es-py": {
        "name": "Spanish (Paraguay)",
        "flag": "/++resource++country-flags/py.gif",
    },
    "es-sv": {
        "name": "Spanish (El Salvador)",
        "flag": "/++resource++country-flags/sv.gif",
    },
    "es-us": {
        "name": "Spanish (USA)",
        "flag": "/++resource++country-flags/us.gif",
    },
    "es-uy": {
        "name": "Spanish (Uruguay)",
        "flag": "/++resource++country-flags/uy.gif",
    },
    "es-ve": {
        "name": "Spanish (Venezuela)",
        "flag": "/++resource++country-flags/ve.gif",
    },
    "fr-ad": {
        "name": "French (Andorra)",
        "flag": "/++resource++country-flags/ad.gif",
    },
    "fr-be": {
        "name": "French (Belgium)",
        "flag": "/++resource++country-flags/be.gif",
    },
    "fr-bf": {
        "name": "French (Burkina Faso)",
        "flag": "/++resource++country-flags/bf.gif",
    },
    "fr-bi": {
        "name": "French (Burundi)",
        "flag": "/++resource++country-flags/bi.gif",
    },
    "fr-bj": {
        "name": "French (Benin)",
        "flag": "/++resource++country-flags/bj.gif",
    },
    "fr-ca": {
        "name": "French (Canada)",
        "flag": "/++resource++country-flags/ca.gif",
    },
    "fr-cd": {
        "name": "French (Democratic Republic of Congo)",
        "flag": "/++resource++country-flags/cd.gif",
    },
    "fr-cf": {
        "name": "French (Central African Republic)",
        "flag": "/++resource++country-flags/cf.gif",
    },
    "fr-cg": {
        "name": "French (Congo)",
        "flag": "/++resource++country-flags/cg.gif",
    },
    "fr-ch": {
        "name": "French (Switzerland)",
        "flag": "/++resource++country-flags/ch.gif",
    },
    "fr-ci": {
        "name": "French (Cote d'Ivoire)",
        "flag": "/++resource++country-flags/ci.gif",
    },
    "fr-cm": {
        "name": "French (Cameroon)",
        "flag": "/++resource++country-flags/cm.gif",
    },
    "fr-dj": {
        "name": "French (Djibouti)",
        "flag": "/++resource++country-flags/dj.gif",
    },
    "fr-fr": {
        "name": "French (France)",
        "flag": "/++resource++country-flags/fr.gif",
    },
    "fr-ga": {
        "name": "French (Gabon)",
        "flag": "/++resource++country-flags/ga.gif",
    },
    "fr-gb": {
        "name": "French (United Kingdom)",
        "flag": "/++resource++country-flags/gb.gif",
    },
    "fr-gf": {
        "name": "French (French Guiana)",
        "flag": "/++resource++country-flags/gf.gif",
    },
    "fr-gn": {
        "name": "French (Guinea)",
        "flag": "/++resource++country-flags/gn.gif",
    },
    "fr-gp": {
        "name": "French (Guadeloupe)",
        "flag": "/++resource++country-flags/gp.gif",
    },
    "fr-ht": {
        "name": "French (Haiti)",
        "flag": "/++resource++country-flags/ht.gif",
    },
    "fr-it": {
        "name": "French (Italy)",
        "flag": "/++resource++country-flags/it.gif",
    },
    "fr-km": {
        "name": "French (Comoros Islands)",
        "flag": "/++resource++country-flags/km.gif",
    },
    "fr-lb": {
        "name": "French (Lebanon)",
        "flag": "/++resource++country-flags/lb.gif",
    },
    "fr-lu": {
        "name": "French (Luxembourg)",
        "flag": "/++resource++country-flags/lu.gif",
    },
    "fr-mc": {
        "name": "French (Monaco)",
        "flag": "/++resource++country-flags/mc.gif",
    },
    "fr-mg": {
        "name": "French (Madagascar)",
        "flag": "/++resource++country-flags/mg.gif",
    },
    "fr-ml": {
        "name": "French (Mali)",
        "flag": "/++resource++country-flags/ml.gif",
    },
    "fr-mq": {
        "name": "French (Martinique)",
        "flag": "/++resource++country-flags/mq.gif",
    },
    "fr-nc": {
        "name": "French (New Caledonia)",
        "flag": "/++resource++country-flags/nc.gif",
    },
    "fr-pf": {
        "name": "French (French Polynesia)",
        "flag": "/++resource++country-flags/pf.gif",
    },
    "fr-pm": {
        "name": "French (St. Pierre and Miquelon)",
        "flag": "/++resource++country-flags/pm.gif",
    },
    "fr-re": {
        "name": "French (Reunion)",
        "flag": "/++resource++country-flags/re.gif",
    },
    "fr-rw": {
        "name": "French (Rwanda)",
        "flag": "/++resource++country-flags/rw.gif",
    },
    "fr-sc": {
        "name": "French (Seychelles)",
        "flag": "/++resource++country-flags/sc.gif",
    },
    "fr-td": {
        "name": "French (Chad)",
        "flag": "/++resource++country-flags/td.gif",
    },
    "fr-tg": {
        "name": "French (Togo)",
        "flag": "/++resource++country-flags/tg.gif",
    },
    "fr-vu": {
        "name": "French (Vanuatu)",
        "flag": "/++resource++country-flags/vu.gif",
    },
    "fr-wf": {
        "name": "French (Wallis and Futuna)",
        "flag": "/++resource++country-flags/wf.gif",
    },
    "fr-yt": {
        "name": "French (Mayotte)",
        "flag": "/++resource++country-flags/yt.gif",
    },
    "hr-ba": {
        "name": "Croatian (Bosnia-Herzegovina)",
        "flag": "/++resource++country-flags/ba.gif",
    },
    "hr-hr": {
        "name": "Croatian (Croatia)",
        "flag": "/++resource++country-flags/hr.gif",
    },
    "hu-hu": {
        "name": "Hungarian (Hungary)",
        "flag": "/++resource++country-flags/hu.gif",
    },
    "hu-si": {
        "name": "Hungarian (Slovenia)",
        "flag": "/++resource++country-flags/hu.gif",
    },
    "it-ch": {
        "name": "Italian (Switzerland)",
        "flag": "/++resource++country-flags/it.gif",
    },
    "it-hr": {
        "name": "Italian (Croatia)",
        "flag": "/++resource++country-flags/it.gif",
    },
    "it-it": {
        "name": "Italian (Italy)",
        "flag": "/++resource++country-flags/it.gif",
    },
    "it-si": {
        "name": "Italian (Slovenia)",
        "flag": "/++resource++country-flags/it.gif",
    },
    "it-sm": {
        "name": "Italian (San Marino)",
        "flag": "/++resource++country-flags/sm.gif",
    },
    "ko-kp": {
        "name": "Korean (Korea, North)",
        "flag": "/++resource++country-flags/kp.gif",
    },
    "ko-kr": {
        "name": "Korean (Korea, South)",
        "flag": "/++resource++country-flags/kr.gif",
    },
    "ln-cd": {
        "name": "Lingala (Democratic Republic of Congo)",
        "flag": "/++resource++country-flags/cd.gif",
    },
    "ln-cg": {
        "name": "Lingala (Congo)",
        "flag": "/++resource++country-flags/cg.gif",
    },
    "ms-bn": {
        "name": "Malay (Brunei)",
        "flag": "/++resource++country-flags/bn.gif",
    },
    "ms-my": {
        "name": "Malay (Malaysia)",
        "flag": "/++resource++country-flags/my.gif",
    },
    "ms-sg": {
        "name": "Malay (Singapore)",
        "flag": "/++resource++country-flags/sg.gif",
    },
    "nl-an": {
        "name": "Dutch (Netherlands Antilles)",
        "flag": "/++resource++country-flags/an.gif",
    },
    "nl-aw": {
        "name": "Dutch (Aruba)",
        "flag": "/++resource++country-flags/aw.gif",
    },
    "nl-be": {
        "name": "Dutch (Belgium)",
        "flag": "/++resource++country-flags/be.gif",
    },
    "nl-nl": {
        "name": "Dutch (Netherlands)",
        "flag": "/++resource++country-flags/nl.gif",
    },
    "nl-sr": {
        "name": "Dutch (Suriname)",
        "flag": "/++resource++country-flags/sr.gif",
    },
    "pt-ao": {
        "name": "Portuguese (Angola)",
        "native": "Português (Angola)",
        "flag": "/++resource++country-flags/ao.gif",
    },
    "pt-br": {
        "name": "Portuguese (Brazil)",
        "native": "Português (Brasil)",
        "flag": "/++resource++country-flags/br.gif",
    },
    "pt-cv": {
        "name": "Portuguese (Ilhas Cabo Verde)",
        "native": "Português (Cabo Verde)",
        "flag": "/++resource++country-flags/cv.gif",
    },
    "pt-gw": {
        "name": "Portuguese (Guiné-Bissau)",
        "native": "Português (Guiné-Bissau)",
        "flag": "/++resource++country-flags/gw.gif",
    },
    "pt-mz": {
        "name": "Portuguese (Moçambique)",
        "native": "Português (Moçambique)",
        "flag": "/++resource++country-flags/mz.gif",
    },
    "pt-pt": {
        "name": "Portuguese (Portugal)",
        "native": "Português (Portugal)",
        "flag": "/++resource++country-flags/pt.gif",
    },
    "pt-st": {
        "name": "Portuguese (São Tomé e Príncipe)",
        "native": "Português (São Tomé e Príncipe)",
        "flag": "/++resource++country-flags/st.gif",
    },
    "sd-in": {
        "name": "Sindhi (India)",
        "flag": "/++resource++country-flags/in.gif",
    },
    "sd-pk": {
        "name": "Sindhi (Pakistan)",
        "flag": "/++resource++country-flags/pk.gif",
    },
    "sr-ba": {
        "name": "Serbian (Bosnia-Herzegovina)",
        "flag": "/++resource++country-flags/ba.gif",
    },
    "ss-sz": {
        "name": "Swati (Swaziland)",
        "flag": "/++resource++country-flags/sz.gif",
    },
    "ss-za": {
        "name": "Swati (South Africa)",
        "flag": "/++resource++country-flags/za.gif",
    },
    "sv-fi": {
        "name": "Swedish (Finland)",
        "flag": "/++resource++country-flags/se.gif",
    },
    "sv-se": {
        "name": "Swedish (Sweden)",
        "flag": "/++resource++country-flags/se.gif",
    },
    "sw-ke": {
        "name": "Swahili (Kenya)",
        "flag": "/++resource++country-flags/ke.gif",
    },
    "sw-tz": {
        "name": "Swahili (Tanzania)",
        "flag": "/++resource++country-flags/tz.gif",
    },
    "ta-in": {
        "name": "Tamil (India)",
        "flag": "/++resource++country-flags/in.gif",
    },
    "ta-sg": {
        "name": "Tamil (Singapore)",
        "flag": "/++resource++country-flags/sg.gif",
    },
    "tn-bw": {
        "name": "Tswana (Botswana)",
        "flag": "/++resource++country-flags/bw.gif",
    },
    "tn-za": {
        "name": "Tswana (South Africa)",
        "flag": "/++resource++country-flags/za.gif",
    },
    "tr-bg": {
        "name": "Turkish (Bulgaria)",
        "flag": "/++resource++country-flags/tr.gif",
    },
    "tr-cy": {
        "name": "Turkish (Cyprus)",
        "flag": "/++resource++country-flags/tr.gif",
    },
    "tr-tr": {
        "name": "Turkish (Turkey)",
        "flag": "/++resource++country-flags/tr.gif",
    },
    "ur-in": {
        "name": "Urdu (India)",
        "flag": "/++resource++country-flags/in.gif",
    },
    "ur-pk": {
        "name": "Urdu (Pakistan)",
        "flag": "/++resource++country-flags/pk.gif",
    },
    "zh-cn": {
        "name": "Chinese (China)",
        "native": "简体中文(中国)",
        "flag": "/++resource++country-flags/cn.gif",
    },
    "zh-hk": {
        "name": "Chinese (Hongkong)",
        "native": "繁體中文(香港)",
        "flag": "/++resource++country-flags/hk.gif",
    },
    "zh-sg": {
        "name": "Chinese (Singapore)",
        "native": "简体中文(新加坡)",
        "flag": "/++resource++country-flags/sg.gif",
    },
    "zh-tw": {
        "name": "Chinese (Taiwan)",
        "native": "繁體中文(臺灣)",
        "flag": "/++resource++country-flags/tw.gif",
    },
}

# convert the utf-8 encoded values to unicode
for code in _combinedlanguagelist:
    value = _combinedlanguagelist[code]
    if "name" in value:
        value["name"] = value["name"]
    if "native" in value:
        value["native"] = value["native"]
