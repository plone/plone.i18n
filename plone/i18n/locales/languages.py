from .interfaces import IContentLanguageAvailability
from .interfaces import ILanguageAvailability
from .interfaces import IMetadataLanguageAvailability
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
#     u'flag' : u'countryflag/*.gif'
# }
#
# This list follows ISO-639-1. The list retains entries for mo and sh,
# even tough these have later been deprecated from the standard.

_languagelist = {
    "aa": {
        "native": "магIарул мацI",
        "name": "Afar",
        "flag": "countryflag/dj",
    },
    "ab": {
        "native": "бызшәа",
        "name": "Abkhazian",
        "flag": "countryflag/ge",
    },
    "ae": {"native": "avesta", "name": "Avestan"},
    "af": {"native": "Afrikaans", "name": "Afrikaans"},
    "ak": {"native": "Akan", "name": "Akan"},
    "am": {"native": "አማርኛ", "name": "Amharic"},
    "an": {"native": "aragonés", "name": "Aragonese"},
    "ar": {
        "native": "العربية",
        "name": "Arabic",
        "flag": "languageflag/ar",
    },
    "as": {"native": "অসমিয়া", "name": "Assamese"},
    "ay": {"native": "Aymara", "name": "Aymara"},
    "az": {
        "native": "Azəri Türkçəsi",
        "name": "Azerbaijani",
        "flag": "countryflag/az",
    },
    "ba": {"native": "Bashkir", "name": "Bashkir"},
    "be": {
        "native": "Беларускі",
        "name": "Belarussian",
        "flag": "countryflag/by",
    },
    "bg": {
        "native": "Български",
        "name": "Bulgarian",
        "flag": "countryflag/bg",
    },
    "bh": {"native": "Bihari", "name": "Bihari"},
    "bi": {"native": "Bislama", "name": "Bislama"},
    "bm": {"native": "bamanankan", "name": "Bambara"},
    "bn": {
        "native": "বাংলা",
        "name": "Bengali",
        "flag": "countryflag/bd",
    },
    "bo": {"native": "བོད་སྐད་", "name": "Tibetan"},
    "br": {"native": "brezhoneg", "name": "Breton"},
    "bs": {
        "native": "Bosanski",
        "name": "Bosnian",
        "flag": "countryflag/ba",
    },
    "ca": {
        "native": "Català",
        "name": "Catalan",
        "flag": "languageflag/ca",
    },
    "ce": {"native": "нохчийн мотт", "name": "Chechen"},
    "ch": {"native": "Chamoru", "name": "Chamorro"},
    "co": {"native": "Corsu", "name": "Corsican"},
    "cr": {"native": "ᓀᐦᐃᔭᐍᐏᐣ", "name": "Cree"},
    "cs": {
        "native": "Čeština",
        "name": "Czech",
        "flag": "countryflag/cz",
    },
    "cu": {"native": "ѩзыкъ словѣньскъ", "name": "Old Church Slavonic"},
    "cv": {"native": "чӑваш чӗлхи", "name": "Chuvash"},
    "cy": {
        "native": "Cymraeg",
        "name": "Welsh",
        "flag": "languageflag/cy",
    },
    "da": {
        "native": "Dansk",
        "name": "Danish",
        "flag": "countryflag/dk",
    },
    "de": {
        "native": "Deutsch",
        "name": "German",
        "flag": "countryflag/de",
    },
    "dv": {"native": "Divehi", "name": "Maldivian"},
    "dz": {"native": "Bhutani", "name": "Indian Bhutani"},
    "ee": {"native": "Eʋegbe", "name": "Ewe"},
    "el": {
        "native": "Ελληνικά",
        "name": "Greek",
        "flag": "countryflag/gr",
    },
    "en": {
        "native": "English",
        "name": "English",
        "flag": "countryflag/gb",
    },
    "eo": {
        "native": "Esperanto",
        "name": "Esperanto",
        "flag": "languageflag/eo",
    },
    "es": {
        "native": "Español",
        "name": "Spanish",
        "flag": "countryflag/es",
    },
    "et": {
        "native": "Eesti",
        "name": "Estonian",
        "flag": "countryflag/ee",
    },
    "eu": {
        "native": "Euskara",
        "name": "Basque",
        "flag": "languageflag/eu",
    },
    "fa": {"native": "فارسی", "name": "Persian"},
    "ff": {"native": "Fulfulde", "name": "Fula"},
    "fi": {
        "native": "Suomi",
        "name": "Finnish",
        "flag": "countryflag/fi",
    },
    "fj": {
        "native": "Fiji",
        "name": "Fiji",
        "flag": "countryflag/fj",
    },
    "fo": {
        "native": "Føroyska",
        "name": "Faroese",
        "flag": "countryflag/fo",
    },
    "fr": {
        "native": "Français",
        "name": "French",
        "flag": "countryflag/fr",
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
        "flag": "countryflag/il",
    },
    "hi": {
        "native": "हिंदी",
        "name": "Hindi",
        "flag": "countryflag/in",
    },
    "ho": {"native": "Hiri Motu", "name": "Hiri Motu"},
    "hr": {
        "native": "Hrvatski",
        "name": "Croatian",
        "flag": "countryflag/hr",
    },
    "ht": {"native": "Kreyòl ayisyen", "name": "Haitian"},
    "hu": {
        "native": "Magyar",
        "name": "Hungarian",
        "flag": "countryflag/hu",
    },
    "hy": {
        "native": "Հայերէն",
        "name": "Armenian",
        "flag": "countryflag/am",
    },
    "hz": {"native": "Otjiherero", "name": "Herero"},
    "ia": {"native": "Interlingua", "name": "Interlingua"},
    "id": {
        "native": "Bahasa Indonesia",
        "name": "Indonesian",
        "flag": "countryflag/id",
    },
    "ie": {"native": "Interlingue", "name": "Interlingue"},
    "ig": {"native": "Asụsụ Igbo", "name": "Igbo"},
    "ii": {"native": "Nuosu", "name": "Nuosu"},
    "ik": {"native": "Iñupiaq", "name": "Inupiak"},
    "io": {"native": "Ido", "name": "Ido"},
    "is": {
        "native": "Íslenska",
        "name": "Icelandic",
        "flag": "countryflag/is",
    },
    "it": {
        "native": "Italiano",
        "name": "Italian",
        "flag": "countryflag/it",
    },
    "iu": {"native": "ᐃᓄᒃᑎᑐᑦ", "name": "Inuktitut"},
    "ja": {
        "native": "日本語",
        "name": "Japanese",
        "flag": "countryflag/jp",
    },
    "jv": {"native": "Javanese", "name": "basa Jawa"},
    "ka": {
        "native": "ქართული",
        "name": "Georgian",
        "flag": "countryflag/ge",
    },
    "kg": {"native": "KiKongo", "name": "Kongo"},
    "ki": {"native": "Gĩkũyũ", "name": "Kikuyu"},
    "kj": {"native": "Kuanyama", "name": "Kwanyama"},
    "kk": {
        "native": "ﻗﺎﺯﺍﻗﺸﺎ",
        "name": "Kazakh",
        "flag": "countryflag/kz",
    },
    "kl": {
        "native": "Greenlandic",
        "name": "Greenlandic",
        "flag": "countryflag/gl",
    },
    "km": {
        "native": "ខ្មែរ",
        "name": "Cambodian/Khmer",
        "flag": "countryflag/kh",
    },
    "kn": {
        "native": "ಕನ್ನಡ",
        "name": "Kannada",
        "flag": "countryflag/in",
    },
    "ko": {
        "native": "한국어",
        "name": "Korean",
        "flag": "countryflag/kr",
    },
    "kr": {"native": "Kanuri", "name": "Kanuri"},
    "ks": {
        "native": "काऽशुर",
        "name": "Kashmiri",
        "flag": "countryflag/in",
    },
    "ku": {"native": "Kurdí", "name": "Kurdish"},
    "kv": {"native": "коми кыв", "name": "Komi"},
    "kw": {"native": "Kernewek", "name": "Cornish"},
    "ky": {"native": "Кыргыз", "name": "Kirghiz"},
    "la": {
        "native": "Latin",
        "name": "Latin",
        "flag": "countryflag/va",
    },
    "lb": {
        "native": "Lëtzebuergesch",
        "name": "Luxemburgish",
        "flag": "countryflag/lu",
    },
    "lg": {"native": "Luganda", "name": "Ganda"},
    "li": {"native": "Limburgs", "name": "Limburgish"},
    "ln": {"native": "Lingala", "name": "Lingala"},
    "lo": {
        "native": "ພາສາລາວ",
        "name": "Laotian",
        "flag": "countryflag/la",
    },
    "lt": {
        "native": "Lietuvių",
        "name": "Lithuanian",
        "flag": "countryflag/lt",
    },
    "lu": {"native": "Tshiluba", "name": "Luba-Katanga"},
    "lv": {
        "native": "Latviešu",
        "name": "Latvian",
        "flag": "countryflag/lv",
    },
    "mg": {
        "native": "Malagasy",
        "name": "Madagascarian",
        "flag": "countryflag/mg",
    },
    "mh": {"native": "Kajin M̧ajeļ", "name": "Marshallese"},
    "mi": {"native": "Maori", "name": "Maori"},
    "mk": {
        "native": "Македонски",
        "name": "Macedonian",
        "flag": "countryflag/mk",
    },
    "ml": {"native": "മലയാളം", "name": "Malayalam"},
    "mn": {
        "native": "Монгол",
        "name": "Mongolian",
        "flag": "countryflag/mn",
    },
    "mo": {
        "native": "Moldavian",
        "name": "Moldavian",
        "flag": "countryflag/md",
    },
    "mr": {"native": "मराठी", "name": "Marathi"},
    "ms": {"native": "Bahasa Melayu", "name": "Malay"},
    "mt": {
        "native": "Malti",
        "name": "Maltese",
        "flag": "countryflag/mt",
    },
    "my": {"native": "Burmese", "name": "Burmese"},
    "na": {
        "native": "Nauru",
        "name": "Nauruan",
        "flag": "countryflag/nr",
    },
    "nb": {"native": "Norsk bokmål", "name": "Norwegian Bokmål"},
    "nd": {"native": "Ndebele (North)", "name": "Ndebele (North)"},
    "ne": {"native": "नेपाली", "name": "Nepali"},
    "ng": {"native": "Owambo", "name": "Ndonga"},
    "nl": {
        "native": "Nederlands",
        "name": "Dutch",
        "flag": "countryflag/nl",
    },
    "nn": {
        "native": "Nynorsk",
        "name": "Nynorsk",
        "flag": "countryflag/no",
    },
    "no": {
        "native": "Norsk",
        "name": "Norwegian",
        "flag": "countryflag/no",
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
        "flag": "countryflag/pl",
    },
    "ps": {"native": "پښتو", "name": "Pashto"},
    "pt": {
        "native": "Português",
        "name": "Portuguese",
        "flag": "countryflag/pt",
    },
    "qu": {"native": "Quechua", "name": "Quechua"},
    "rm": {"native": "Rhaeto-Romance", "name": "Rhaeto-Romance"},
    "rn": {"native": "Kirundi", "name": "Kirundi"},
    "ro": {
        "native": "Română",
        "name": "Romanian",
        "flag": "countryflag/ro",
    },
    "ru": {
        "native": "Русский",
        "name": "Russian",
        "flag": "countryflag/ru",
    },
    "rw": {"native": "Kinyarwanda", "name": "Kinyarwanda"},
    "sa": {"native": "संस्कृत", "name": "Sanskrit"},
    "sc": {"native": "sardu", "name": "Sardinian"},
    "sd": {
        "native": "Sindhi",
        "name": "Sindhi",
        "flag": "countryflag/pk",
    },
    "se": {"native": "Northern Sámi", "name": "Northern Sámi"},
    "sg": {
        "native": "Sangho",
        "name": "Sangho",
        "flag": "countryflag/cf",
    },
    "sh": {"native": "Serbo-Croatian", "name": "Serbo-Croatian"},
    "si": {"native": "Singhalese", "name": "Singhalese"},
    "sk": {
        "native": "Slovenčina",
        "name": "Slovak",
        "flag": "countryflag/sk",
    },
    "sl": {
        "native": "Slovenščina",
        "name": "Slovenian",
        "flag": "countryflag/si",
    },
    "sm": {"native": "Samoan", "name": "Samoan"},
    "sn": {"native": "Shona", "name": "Shona"},
    "so": {
        "native": "Somali",
        "name": "Somali",
        "flag": "countryflag/so",
    },
    "sq": {
        "native": "Shqip",
        "name": "Albanian",
        "flag": "countryflag/al",
    },
    "sr": {
        # Note: we support two character sets for this language.
        # See zope_i18n_allowed_languages below.
        # Until and including 5.2, native was Cyrillic: српски.
        # In Plone 6.0 native became Latin: Srpski.
        "native": "Srpski",
        "name": "Serbian",
        "flag": "countryflag/cs",
    },
    "ss": {"native": "SiSwati", "name": "Swati"},
    "st": {"native": "Sesotho", "name": "Southern Sotho"},
    "su": {
        "native": "Sudanese",
        "name": "Sudanese",
        "flag": "countryflag/sd",
    },
    "sv": {
        "native": "Svenska",
        "name": "Swedish",
        "flag": "countryflag/se",
    },
    "sw": {"native": "Kiswahili", "name": "Swahili"},
    "ta": {"native": "தமிழ", "name": "Tamil"},
    "te": {"native": "తెలుగు", "name": "Telugu"},
    "tg": {
        "native": "Тоҷики",
        "name": "Tadjik",
        "flag": "countryflag/tj",
    },
    "th": {
        "native": "ไทย",
        "name": "Thai",
        "flag": "countryflag/th",
    },
    "ti": {"native": "ትግርኛ", "name": "Tigrinya"},
    "tk": {
        "native": "түркmенче",
        "name": "Turkmen",
        "flag": "countryflag/tm",
    },
    "tl": {"native": "Tagalog", "name": "Tagalog"},
    "tn": {
        "native": "Setswana",
        "name": "Tswana",
        "flag": "countryflag/bw",
    },
    "to": {"native": "Tonga", "name": "Tonga"},
    "tr": {
        "native": "Türkçe",
        "name": "Turkish",
        "flag": "countryflag/tr",
    },
    "ts": {"native": "Xitsonga", "name": "Tsonga"},
    "tt": {"native": "татарча", "name": "Tatar"},
    "tw": {"native": "Twi", "name": "Twi"},
    "ty": {"native": "Reo Tahiti", "name": "Tahitian"},
    "ug": {"native": "Uigur", "name": "Uigur"},
    "uk": {
        "native": "Українська",
        "name": "Ukrainian",
        "flag": "countryflag/ua",
    },
    "ur": {"native": "اردو", "name": "Urdu"},
    "uz": {
        "native": "Ўзбекча",
        "name": "Uzbek",
        "flag": "countryflag/uz",
    },
    "ve": {"native": "Tshivenḓa", "name": "Venda"},
    "vi": {
        "native": "Tiếng Việt",
        "name": "Vietnamese",
        "flag": "countryflag/vn",
    },
    "vk": {"native": "Ovalingo", "name": "Viking"},
    "vo": {"native": "Volapük", "name": "Volapük"},
    "wa": {"native": "Walon", "name": "Walloon"},
    "wo": {"native": "Wolof", "name": "Wolof"},
    "xh": {"native": "IsiXhosa", "name": "Xhosa"},
    "yi": {
        "native": "ײִדיש",
        "name": "Yiddish",
        "flag": "countryflag/il",
    },
    "yo": {"native": "Yorùbá", "name": "Yorouba"},
    "za": {"native": "Zhuang", "name": "Zhuang"},
    "zh": {
        "native": "中文",
        "name": "Chinese",
        "flag": "countryflag/cn",
    },
    "zu": {
        "native": "IsiZulu",
        "name": "Zulu",
        "flag": "countryflag/za",
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
        "flag": "countryflag/cs",
    }
elif "sr@Cyrl" in _zope_i18n_allowed_languages:
    _languagelist["sr"] = {
        "native": "српски",
        "name": "Serbian (Cyrillic)",
        "flag": "countryflag/cs",
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
        "flag": "countryflag/ae",
    },
    "ar-bh": {
        "name": "Arabic (Bahrain)",
        "flag": "countryflag/bh",
    },
    "ar-dz": {
        "name": "Arabic (Algeria)",
        "flag": "countryflag/dz",
    },
    "ar-eg": {
        "name": "Arabic (Egypt)",
        "flag": "countryflag/eg",
    },
    "ar-il": {
        "name": "Arabic (Israel)",
        "flag": "countryflag/il",
    },
    "ar-iq": {
        "name": "Arabic (Iraq)",
        "flag": "countryflag/iq",
    },
    "ar-jo": {
        "name": "Arabic (Jordan)",
        "flag": "countryflag/jo",
    },
    "ar-kw": {
        "name": "Arabic (Kuwait)",
        "flag": "countryflag/kw",
    },
    "ar-lb": {
        "name": "Arabic (Lebanon)",
        "flag": "countryflag/lb",
    },
    "ar-ly": {
        "name": "Arabic (Libya)",
        "flag": "countryflag/ly",
    },
    "ar-ma": {
        "name": "Arabic (Morocco)",
        "flag": "countryflag/ma",
    },
    "ar-mr": {
        "name": "Arabic (Mauritania)",
        "flag": "countryflag/mr",
    },
    "ar-om": {
        "name": "Arabic (Oman)",
        "flag": "countryflag/om",
    },
    "ar-ps": {
        "name": "Arabic (Palestinian West Bank and Gaza)",
        "flag": "countryflag/ps",
    },
    "ar-qa": {
        "name": "Arabic (Qatar)",
        "flag": "countryflag/qa",
    },
    "ar-sa": {
        "name": "Arabic (Saudi Arabia)",
        "flag": "countryflag/sa",
    },
    "ar-sd": {
        "name": "Arabic (Sudan)",
        "flag": "countryflag/ly",
    },
    "ar-so": {
        "name": "Arabic (Somalia)",
        "flag": "countryflag/so",
    },
    "ar-sy": {
        "name": "Arabic (Syria)",
        "flag": "countryflag/sy",
    },
    "ar-td": {
        "name": "Arabic (Chad)",
        "flag": "countryflag/td",
    },
    "ar-tn": {
        "name": "Arabic (Tunisia)",
        "flag": "countryflag/ly",
    },
    "ar-ye": {
        "name": "Arabic (Yemen)",
        "flag": "countryflag/ye",
    },
    "bn-bd": {
        "name": "Bengali (Bangladesh)",
        "flag": "countryflag/bd",
    },
    "bn-in": {
        "name": "Bengali (India)",
        "flag": "countryflag/in",
    },
    "bn-sg": {
        "name": "Bengali (Singapore)",
        "flag": "countryflag/sg",
    },
    "ch-gu": {
        "name": "Chamorro (Guam)",
        "flag": "countryflag/gu",
    },
    "ch-mp": {
        "name": "Chamorro (Northern Mariana Islands)",
        "flag": "countryflag/mp",
    },
    "cs-cz": {
        "name": "Czech (Czech republic)",
        "native": "Čeština (Česká republika)",
        "flag": "countryflag/cz",
    },
    "da-dk": {
        "name": "Danish (Denmark)",
        "flag": "countryflag/dk",
    },
    "da-gl": {
        "name": "Danish (Greenland)",
        "flag": "countryflag/gl",
    },
    "de-at": {
        "name": "German (Austria)",
        "native": "Deutsch (Österreich)",
        "flag": "countryflag/at",
    },
    "de-be": {
        "name": "German (Belgium)",
        "native": "Deutsch (Belgien)",
        "flag": "countryflag/de",
    },
    "de-ch": {
        "name": "German (Switzerland)",
        "native": "Deutsch (Schweiz)",
        "flag": "countryflag/ch",
    },
    "de-de": {
        "name": "German (Germany)",
        "native": "Deutsch (Deutschland)",
        "flag": "countryflag/de",
    },
    "de-dk": {
        "name": "German (Denmark)",
        "native": "Deutsch (Danmark)",
        "flag": "countryflag/de",
    },
    "de-li": {
        "name": "German (Liechtenstein)",
        "native": "Deutsch (Liechtenstein)",
        "flag": "countryflag/li",
    },
    "de-lu": {
        "name": "German (Luxembourg)",
        "native": "Deutsch (Luxemburg)",
        "flag": "countryflag/de",
    },
    "el-cy": {
        "name": "Greek (Cyprus)",
        "flag": "countryflag/cy",
    },
    "el-gr": {
        "name": "Greek (Greece)",
        "flag": "countryflag/gr",
    },
    "en-ag": {
        "name": "English (Antigua and Barbuda)",
        "flag": "countryflag/ag",
    },
    "en-ai": {
        "name": "English (Anguilla)",
        "flag": "countryflag/ai",
    },
    "en-as": {
        "name": "English (American Samoa)",
        "flag": "countryflag/as",
    },
    "en-au": {
        "name": "English (Australia)",
        "flag": "countryflag/au",
    },
    "en-bb": {
        "name": "English (Barbados)",
        "flag": "countryflag/bb",
    },
    "en-bm": {
        "name": "English (Bermuda)",
        "flag": "countryflag/bm",
    },
    "en-bn": {
        "name": "English (Brunei)",
        "flag": "countryflag/bn",
    },
    "en-bs": {
        "name": "English (Bahamas)",
        "flag": "countryflag/bs",
    },
    "en-bw": {
        "name": "English (Botswana)",
        "flag": "countryflag/bw",
    },
    "en-bz": {
        "name": "English (Belize)",
        "flag": "countryflag/bz",
    },
    "en-ca": {
        "name": "English (Canada)",
        "flag": "countryflag/ca",
    },
    "en-ck": {
        "name": "English (Cook Islands)",
        "flag": "countryflag/ck",
    },
    "en-cm": {
        "name": "English (Cameroon)",
        "flag": "countryflag/cm",
    },
    "en-dm": {
        "name": "English (Dominica)",
        "flag": "countryflag/dm",
    },
    "en-er": {
        "name": "English (Eritrea)",
        "flag": "countryflag/er",
    },
    "en-et": {
        "name": "English (Ethiopia)",
        "flag": "countryflag/et",
    },
    "en-fj": {
        "name": "English (Fiji)",
        "flag": "countryflag/fj",
    },
    "en-fk": {
        "name": "English (Falkland Islands)",
        "flag": "countryflag/fk",
    },
    "en-fm": {
        "name": "English (Micronesia)",
        "flag": "countryflag/fm",
    },
    "en-gb": {
        "name": "English (United Kingdom)",
        "flag": "countryflag/gb",
    },
    "en-gd": {
        "name": "English (Grenada)",
        "flag": "countryflag/gd",
    },
    "en-gh": {
        "name": "English (Ghana)",
        "flag": "countryflag/gh",
    },
    "en-gi": {
        "name": "English (Gibraltar)",
        "flag": "countryflag/gi",
    },
    "en-gm": {
        "name": "English (Gambia)",
        "flag": "countryflag/gm",
    },
    "en-gu": {
        "name": "English (Guam)",
        "flag": "countryflag/gu",
    },
    "en-gy": {
        "name": "English (Guyana)",
        "flag": "countryflag/gy",
    },
    "en-ie": {
        "name": "English (Ireland)",
        "flag": "countryflag/ie",
    },
    "en-il": {
        "name": "English (Israel)",
        "flag": "countryflag/gb",
    },
    "en-io": {
        "name": "English (British Indian Ocean Territory)",
        "flag": "countryflag/io",
    },
    "en-jm": {
        "name": "English (Jamaica)",
        "flag": "countryflag/jm",
    },
    "en-ke": {
        "name": "English (Kenya)",
        "flag": "countryflag/ke",
    },
    "en-ki": {
        "name": "English (Kiribati)",
        "flag": "countryflag/ki",
    },
    "en-kn": {
        "name": "English (St. Kitts-Nevis)",
        "flag": "countryflag/kn",
    },
    "en-ky": {
        "name": "English (Cayman Islands)",
        "flag": "countryflag/ky",
    },
    "en-lc": {
        "name": "English (St. Lucia)",
        "flag": "countryflag/lc",
    },
    "en-lr": {
        "name": "English (Liberia)",
        "flag": "countryflag/lr",
    },
    "en-ls": {
        "name": "English (Lesotho)",
        "flag": "countryflag/ls",
    },
    "en-mp": {
        "name": "English (Northern Mariana Islands)",
        "flag": "countryflag/mp",
    },
    "en-ms": {
        "name": "English (Montserrat)",
        "flag": "countryflag/ms",
    },
    "en-mt": {
        "name": "English (Malta)",
        "flag": "countryflag/mt",
    },
    "en-mu": {
        "name": "English (Mauritius)",
        "flag": "countryflag/mu",
    },
    "en-mw": {
        "name": "English (Malawi)",
        "flag": "countryflag/mw",
    },
    "en-na": {
        "name": "English (Namibia)",
        "flag": "countryflag/na",
    },
    "en-nf": {
        "name": "English (Norfolk Island)",
        "flag": "countryflag/nf",
    },
    "en-ng": {
        "name": "English (Nigeria)",
        "flag": "countryflag/ng",
    },
    "en-nr": {
        "name": "English (Nauru)",
        "flag": "countryflag/nr",
    },
    "en-nu": {
        "name": "English (Niue)",
        "flag": "countryflag/nu",
    },
    "en-nz": {
        "name": "English (New Zealand)",
        "flag": "countryflag/nz",
    },
    "en-pg": {
        "name": "English (Papua New Guinea)",
        "flag": "countryflag/pg",
    },
    "en-ph": {
        "name": "English (Philippines)",
        "flag": "countryflag/ph",
    },
    "en-pk": {
        "name": "English (Pakistan)",
        "flag": "countryflag/pk",
    },
    "en-pn": {
        "name": "English (Pitcairn)",
        "flag": "countryflag/pn",
    },
    "en-pr": {
        "name": "English (Puerto Rico)",
        "flag": "countryflag/pr",
    },
    "en-pw": {
        "name": "English (Palau)",
        "flag": "countryflag/pw",
    },
    "en-rw": {
        "name": "English (Rwanda)",
        "flag": "countryflag/rw",
    },
    "en-sb": {
        "name": "English (Solomon Islands)",
        "flag": "countryflag/sb",
    },
    "en-sc": {
        "name": "English (Seychelles)",
        "flag": "countryflag/sc",
    },
    "en-sg": {
        "name": "English (Singapore)",
        "flag": "countryflag/sg",
    },
    "en-sh": {
        "name": "English (St. Helena)",
        "flag": "countryflag/sh",
    },
    "en-sl": {
        "name": "English (Sierra Leone)",
        "flag": "countryflag/sl",
    },
    "en-so": {
        "name": "English (Somalia)",
        "flag": "countryflag/so",
    },
    "en-sz": {
        "name": "English (Swaziland)",
        "flag": "countryflag/sz",
    },
    "en-tc": {
        "name": "English (Turks and Caicos Islands)",
        "flag": "countryflag/tc",
    },
    "en-tk": {
        "name": "English (Tokelau)",
        "flag": "countryflag/tk",
    },
    "en-to": {
        "name": "English (Tonga)",
        "flag": "countryflag/to",
    },
    "en-tt": {
        "name": "English (Trinidad and Tobago)",
        "flag": "countryflag/tt",
    },
    "en-ug": {
        "name": "English (Uganda)",
        "flag": "countryflag/ug",
    },
    "en-us": {
        "name": "English (USA)",
        "flag": "countryflag/us",
    },
    "en-vc": {
        "name": "English (St. Vincent and the Grenadi)",
        "flag": "countryflag/vc",
    },
    "en-vg": {
        "name": "English (British Virgin Islands)",
        "flag": "countryflag/vg",
    },
    "en-vi": {
        "name": "English (U.S. Virgin Islands)",
        "flag": "countryflag/vi",
    },
    "en-vu": {
        "name": "English (Vanuatu)",
        "flag": "countryflag/vu",
    },
    "en-ws": {
        "name": "English (Western Samoa)",
        "flag": "countryflag/ws",
    },
    "en-za": {
        "name": "English (South Africa)",
        "flag": "countryflag/za",
    },
    "en-zm": {
        "name": "English (Zambia)",
        "flag": "countryflag/zm",
    },
    "en-zw": {
        "name": "English (Zimbabwe)",
        "flag": "countryflag/zw",
    },
    "es-ar": {
        "name": "Spanish (Argentina)",
        "flag": "countryflag/ar",
    },
    "es-bo": {
        "name": "Spanish (Bolivia)",
        "flag": "countryflag/bo",
    },
    "es-cl": {
        "name": "Spanish (Chile)",
        "flag": "countryflag/cl",
    },
    "es-co": {
        "name": "Spanish (Colombia)",
        "flag": "countryflag/co",
    },
    "es-cr": {
        "name": "Spanish (Costa Rica)",
        "flag": "countryflag/cr",
    },
    "es-cu": {
        "name": "Spanish (Cuba)",
        "flag": "countryflag/cu",
    },
    "es-do": {
        "name": "Spanish (Dominican Republic)",
        "flag": "countryflag/do",
    },
    "es-ec": {
        "name": "Spanish (Ecuador)",
        "flag": "countryflag/ec",
    },
    "es-es": {
        "name": "Spanish (Spain)",
        "flag": "countryflag/es",
    },
    "es-gq": {
        "name": "Spanish (Equatorial Guinea)",
        "flag": "countryflag/gq",
    },
    "es-gt": {
        "name": "Spanish (Guatemala)",
        "flag": "countryflag/gt",
    },
    "es-hn": {
        "name": "Spanish (Honduras)",
        "flag": "countryflag/hn",
    },
    "es-mx": {
        "name": "Spanish (Mexico)",
        "flag": "countryflag/mx",
    },
    "es-ni": {
        "name": "Spanish (Nicaragua)",
        "flag": "countryflag/ni",
    },
    "es-pa": {
        "name": "Spanish (Panama)",
        "flag": "countryflag/pa",
    },
    "es-pe": {
        "name": "Spanish (Peru)",
        "flag": "countryflag/pe",
    },
    "es-pr": {
        "name": "Spanish (Puerto Rico)",
        "flag": "countryflag/pr",
    },
    "es-py": {
        "name": "Spanish (Paraguay)",
        "flag": "countryflag/py",
    },
    "es-sv": {
        "name": "Spanish (El Salvador)",
        "flag": "countryflag/sv",
    },
    "es-us": {
        "name": "Spanish (USA)",
        "flag": "countryflag/us",
    },
    "es-uy": {
        "name": "Spanish (Uruguay)",
        "flag": "countryflag/uy",
    },
    "es-ve": {
        "name": "Spanish (Venezuela)",
        "flag": "countryflag/ve",
    },
    "fr-ad": {
        "name": "French (Andorra)",
        "flag": "countryflag/ad",
    },
    "fr-be": {
        "name": "French (Belgium)",
        "flag": "countryflag/be",
    },
    "fr-bf": {
        "name": "French (Burkina Faso)",
        "flag": "countryflag/bf",
    },
    "fr-bi": {
        "name": "French (Burundi)",
        "flag": "countryflag/bi",
    },
    "fr-bj": {
        "name": "French (Benin)",
        "flag": "countryflag/bj",
    },
    "fr-ca": {
        "name": "French (Canada)",
        "flag": "countryflag/ca",
    },
    "fr-cd": {
        "name": "French (Democratic Republic of Congo)",
        "flag": "countryflag/cd",
    },
    "fr-cf": {
        "name": "French (Central African Republic)",
        "flag": "countryflag/cf",
    },
    "fr-cg": {
        "name": "French (Congo)",
        "flag": "countryflag/cg",
    },
    "fr-ch": {
        "name": "French (Switzerland)",
        "flag": "countryflag/ch",
    },
    "fr-ci": {
        "name": "French (Cote d'Ivoire)",
        "flag": "countryflag/ci",
    },
    "fr-cm": {
        "name": "French (Cameroon)",
        "flag": "countryflag/cm",
    },
    "fr-dj": {
        "name": "French (Djibouti)",
        "flag": "countryflag/dj",
    },
    "fr-fr": {
        "name": "French (France)",
        "flag": "countryflag/fr",
    },
    "fr-ga": {
        "name": "French (Gabon)",
        "flag": "countryflag/ga",
    },
    "fr-gb": {
        "name": "French (United Kingdom)",
        "flag": "countryflag/gb",
    },
    "fr-gf": {
        "name": "French (French Guiana)",
        "flag": "countryflag/gf",
    },
    "fr-gn": {
        "name": "French (Guinea)",
        "flag": "countryflag/gn",
    },
    "fr-gp": {
        "name": "French (Guadeloupe)",
        "flag": "countryflag/gp",
    },
    "fr-ht": {
        "name": "French (Haiti)",
        "flag": "countryflag/ht",
    },
    "fr-it": {
        "name": "French (Italy)",
        "flag": "countryflag/it",
    },
    "fr-km": {
        "name": "French (Comoros Islands)",
        "flag": "countryflag/km",
    },
    "fr-lb": {
        "name": "French (Lebanon)",
        "flag": "countryflag/lb",
    },
    "fr-lu": {
        "name": "French (Luxembourg)",
        "flag": "countryflag/lu",
    },
    "fr-mc": {
        "name": "French (Monaco)",
        "flag": "countryflag/mc",
    },
    "fr-mg": {
        "name": "French (Madagascar)",
        "flag": "countryflag/mg",
    },
    "fr-ml": {
        "name": "French (Mali)",
        "flag": "countryflag/ml",
    },
    "fr-mq": {
        "name": "French (Martinique)",
        "flag": "countryflag/mq",
    },
    "fr-nc": {
        "name": "French (New Caledonia)",
        "flag": "countryflag/nc",
    },
    "fr-pf": {
        "name": "French (French Polynesia)",
        "flag": "countryflag/pf",
    },
    "fr-pm": {
        "name": "French (St. Pierre and Miquelon)",
        "flag": "countryflag/pm",
    },
    "fr-re": {
        "name": "French (Reunion)",
        "flag": "countryflag/re",
    },
    "fr-rw": {
        "name": "French (Rwanda)",
        "flag": "countryflag/rw",
    },
    "fr-sc": {
        "name": "French (Seychelles)",
        "flag": "countryflag/sc",
    },
    "fr-td": {
        "name": "French (Chad)",
        "flag": "countryflag/td",
    },
    "fr-tg": {
        "name": "French (Togo)",
        "flag": "countryflag/tg",
    },
    "fr-vu": {
        "name": "French (Vanuatu)",
        "flag": "countryflag/vu",
    },
    "fr-wf": {
        "name": "French (Wallis and Futuna)",
        "flag": "countryflag/wf",
    },
    "fr-yt": {
        "name": "French (Mayotte)",
        "flag": "countryflag/yt",
    },
    "hr-ba": {
        "name": "Croatian (Bosnia-Herzegovina)",
        "flag": "countryflag/ba",
    },
    "hr-hr": {
        "name": "Croatian (Croatia)",
        "flag": "countryflag/hr",
    },
    "hu-hu": {
        "name": "Hungarian (Hungary)",
        "flag": "countryflag/hu",
    },
    "hu-si": {
        "name": "Hungarian (Slovenia)",
        "flag": "countryflag/hu",
    },
    "it-ch": {
        "name": "Italian (Switzerland)",
        "flag": "countryflag/it",
    },
    "it-hr": {
        "name": "Italian (Croatia)",
        "flag": "countryflag/it",
    },
    "it-it": {
        "name": "Italian (Italy)",
        "flag": "countryflag/it",
    },
    "it-si": {
        "name": "Italian (Slovenia)",
        "flag": "countryflag/it",
    },
    "it-sm": {
        "name": "Italian (San Marino)",
        "flag": "countryflag/sm",
    },
    "ko-kp": {
        "name": "Korean (Korea, North)",
        "flag": "countryflag/kp",
    },
    "ko-kr": {
        "name": "Korean (Korea, South)",
        "flag": "countryflag/kr",
    },
    "ln-cd": {
        "name": "Lingala (Democratic Republic of Congo)",
        "flag": "countryflag/cd",
    },
    "ln-cg": {
        "name": "Lingala (Congo)",
        "flag": "countryflag/cg",
    },
    "ms-bn": {
        "name": "Malay (Brunei)",
        "flag": "countryflag/bn",
    },
    "ms-my": {
        "name": "Malay (Malaysia)",
        "flag": "countryflag/my",
    },
    "ms-sg": {
        "name": "Malay (Singapore)",
        "flag": "countryflag/sg",
    },
    "nl-an": {
        "name": "Dutch (Netherlands Antilles)",
        "native": "Nederlands (Antillen)",
        "flag": "countryflag/an",
    },
    "nl-aw": {
        "name": "Dutch (Aruba)",
        "native": "Nederlands (Aruba)",
        "flag": "countryflag/aw",
    },
    "nl-be": {
        "name": "Dutch (Belgium)",
        "native": "Nederlands (België)",
        "flag": "countryflag/be",
    },
    "nl-nl": {
        "name": "Dutch (Netherlands)",
        "native": "Nederlands (Nederland)",
        "flag": "countryflag/nl",
    },
    "nl-sr": {
        "name": "Dutch (Suriname)",
        "native": "Nederlands (Suriname)",
        "flag": "countryflag/sr",
    },
    "pt-ao": {
        "name": "Portuguese (Angola)",
        "native": "Português (Angola)",
        "flag": "countryflag/ao",
    },
    "pt-br": {
        "name": "Portuguese (Brazil)",
        "native": "Português (Brasil)",
        "flag": "countryflag/br",
    },
    "pt-cv": {
        "name": "Portuguese (Ilhas Cabo Verde)",
        "native": "Português (Cabo Verde)",
        "flag": "countryflag/cv",
    },
    "pt-gw": {
        "name": "Portuguese (Guiné-Bissau)",
        "native": "Português (Guiné-Bissau)",
        "flag": "countryflag/gw",
    },
    "pt-mz": {
        "name": "Portuguese (Moçambique)",
        "native": "Português (Moçambique)",
        "flag": "countryflag/mz",
    },
    "pt-pt": {
        "name": "Portuguese (Portugal)",
        "native": "Português (Portugal)",
        "flag": "countryflag/pt",
    },
    "pt-st": {
        "name": "Portuguese (São Tomé e Príncipe)",
        "native": "Português (São Tomé e Príncipe)",
        "flag": "countryflag/st",
    },
    "sd-in": {
        "name": "Sindhi (India)",
        "flag": "countryflag/in",
    },
    "sd-pk": {
        "name": "Sindhi (Pakistan)",
        "flag": "countryflag/pk",
    },
    "sr-ba": {
        "name": "Serbian (Bosnia-Herzegovina)",
        "flag": "countryflag/ba",
    },
    "ss-sz": {
        "name": "Swati (Swaziland)",
        "flag": "countryflag/sz",
    },
    "ss-za": {
        "name": "Swati (South Africa)",
        "flag": "countryflag/za",
    },
    "sv-fi": {
        "name": "Swedish (Finland)",
        "flag": "countryflag/se",
    },
    "sv-se": {
        "name": "Swedish (Sweden)",
        "flag": "countryflag/se",
    },
    "sw-ke": {
        "name": "Swahili (Kenya)",
        "flag": "countryflag/ke",
    },
    "sw-tz": {
        "name": "Swahili (Tanzania)",
        "flag": "countryflag/tz",
    },
    "ta-in": {
        "name": "Tamil (India)",
        "flag": "countryflag/in",
    },
    "ta-sg": {
        "name": "Tamil (Singapore)",
        "flag": "countryflag/sg",
    },
    "tn-bw": {
        "name": "Tswana (Botswana)",
        "flag": "countryflag/bw",
    },
    "tn-za": {
        "name": "Tswana (South Africa)",
        "flag": "countryflag/za",
    },
    "tr-bg": {
        "name": "Turkish (Bulgaria)",
        "flag": "countryflag/tr",
    },
    "tr-cy": {
        "name": "Turkish (Cyprus)",
        "flag": "countryflag/tr",
    },
    "tr-tr": {
        "name": "Turkish (Turkey)",
        "flag": "countryflag/tr",
    },
    "ur-in": {
        "name": "Urdu (India)",
        "flag": "countryflag/in",
    },
    "ur-pk": {
        "name": "Urdu (Pakistan)",
        "flag": "countryflag/pk",
    },
    "zh-cn": {
        "name": "Chinese (China)",
        "native": "简体中文(中国)",
        "flag": "countryflag/cn",
    },
    "zh-hk": {
        "name": "Chinese (Hongkong)",
        "native": "繁體中文(香港)",
        "flag": "countryflag/hk",
    },
    "zh-sg": {
        "name": "Chinese (Singapore)",
        "native": "简体中文(新加坡)",
        "flag": "countryflag/sg",
    },
    "zh-tw": {
        "name": "Chinese (Taiwan)",
        "native": "繁體中文(臺灣)",
        "flag": "countryflag/tw",
    },
}

# convert the utf-8 encoded values to unicode
for code in _combinedlanguagelist:
    value = _combinedlanguagelist[code]
    if "name" in value:
        value["name"] = value["name"]
    if "native" in value:
        value["native"] = value["native"]
