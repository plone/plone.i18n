# -*- coding: UTF-8 -*-
from plone.i18n.locales.interfaces import IContentLanguageAvailability
from plone.i18n.locales.interfaces import ILanguageAvailability
from plone.i18n.locales.interfaces import IMetadataLanguageAvailability
from zope.interface import implementer

import six


@implementer(ILanguageAvailability)
class LanguageAvailability(object):
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
        return [(code, languages[code][u'name']) for code in languages]


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
#     u'flag' : u'countryflag/*'
# }
#
# This list follows ISO-639-1. The list retains entries for mo and sh,
# even tough these have later been deprecated from the standard.

_languagelist = {
    u'aa': {
        u'native': 'магIарул мацI',
        u'name': 'Afar',
        u'flag': u'countryflag/dj',
    },
    u'ab': {
        u'native': 'бызшәа',
        u'name': 'Abkhazian',
        u'flag': u'countryflag/ge',
    },
    u'ae': {u'native': 'avesta', u'name': 'Avestan'},
    u'af': {u'native': 'Afrikaans', u'name': 'Afrikaans'},
    u'ak': {u'native': 'Akan', u'name': 'Akan'},
    u'am': {u'native': 'አማርኛ', u'name': 'Amharic'},
    u'an': {u'native': 'aragonés', u'name': 'Aragonese'},
    u'ar': {
        u'native': 'العربية',
        u'name': 'Arabic',
        u'flag': 'languageflag/ar',
    },
    u'as': {u'native': 'অসমিয়া', u'name': 'Assamese'},
    u'ay': {u'native': 'Aymara', u'name': 'Aymara'},
    u'az': {
        u'native': 'Azəri Türkçəsi',
        u'name': 'Azerbaijani',
        u'flag': u'countryflag/az',
    },
    u'ba': {u'native': 'Bashkir', u'name': 'Bashkir'},
    u'be': {
        u'native': 'Беларускі',
        u'name': 'Belarussian',
        u'flag': u'countryflag/by',
    },
    u'bg': {
        u'native': 'Български',
        u'name': 'Bulgarian',
        u'flag': u'countryflag/bg',
    },
    u'bh': {u'native': 'Bihari', u'name': 'Bihari'},
    u'bi': {u'native': 'Bislama', u'name': 'Bislama'},
    u'bm': {u'native': 'bamanankan', u'name': 'Bambara'},
    u'bn': {
        u'native': 'বাংলা',
        u'name': 'Bengali',
        u'flag': u'countryflag/bd',
    },
    u'bo': {u'native': 'བོད་སྐད་', u'name': 'Tibetan'},
    u'br': {u'native': 'brezhoneg', u'name': 'Breton'},
    u'bs': {
        u'native': 'Bosanski',
        u'name': 'Bosnian',
        u'flag': u'countryflag/ba',
    },
    u'ca': {
        u'native': 'Català',
        u'name': 'Catalan',
        u'flag': u'languageflag/ca',
    },
    u'ce': {u'native': 'нохчийн мотт', u'name': 'Chechen'},
    u'ch': {u'native': 'Chamoru', u'name': 'Chamorro'},
    u'co': {u'native': 'Corsu', u'name': 'Corsican'},
    u'cr': {u'native': 'ᓀᐦᐃᔭᐍᐏᐣ', u'name': 'Cree'},
    u'cs': {
        u'native': 'Čeština',
        u'name': 'Czech',
        u'flag': u'countryflag/cz',
    },
    u'cu': {u'native': 'ѩзыкъ словѣньскъ', u'name': 'Old Church Slavonic'},
    u'cv': {u'native': 'чӑваш чӗлхи', u'name': 'Chuvash'},
    u'cy': {
        u'native': 'Cymraeg',
        u'name': 'Welsh',
        u'flag': 'languageflag/cy',
    },
    u'da': {
        u'native': 'Dansk',
        u'name': 'Danish',
        u'flag': u'countryflag/dk',
    },
    u'de': {
        u'native': 'Deutsch',
        u'name': 'German',
        u'flag': u'countryflag/de',
    },
    u'dv': {u'native': 'Divehi', u'name': 'Maldivian'},
    u'dz': {u'native': 'Bhutani', u'name': 'Indian Bhutani'},
    u'ee': {u'native': 'Eʋegbe', u'name': 'Ewe'},
    u'el': {
        u'native': 'Ελληνικά',
        u'name': 'Greek',
        u'flag': u'countryflag/gr',
    },
    u'en': {
        u'native': 'English',
        u'name': 'English',
        u'flag': u'countryflag/gb',
    },
    u'eo': {
        u'native': 'Esperanto',
        u'name': 'Esperanto',
        u'flag': 'languageflag/eo',
    },
    u'es': {
        u'native': 'Español',
        u'name': 'Spanish',
        u'flag': u'countryflag/es',
    },
    u'et': {
        u'native': 'Eesti',
        u'name': 'Estonian',
        u'flag': u'countryflag/ee',
    },
    u'eu': {
        u'native': 'Euskara',
        u'name': 'Basque',
        u'flag': 'languageflag/eu',
    },
    u'fa': {u'native': 'فارسی', u'name': 'Persian'},
    u'ff': {u'native': 'Fulfulde', u'name': 'Fula'},
    u'fi': {
        u'native': 'Suomi',
        u'name': 'Finnish',
        u'flag': u'countryflag/fi',
    },
    u'fj': {
        u'native': 'Fiji',
        u'name': 'Fiji',
        u'flag': u'countryflag/fj',
    },
    u'fo': {
        u'native': 'Føroyska',
        u'name': 'Faroese',
        u'flag': u'countryflag/fo',
    },
    u'fr': {
        u'native': 'Français',
        u'name': 'French',
        u'flag': u'countryflag/fr',
    },
    u'fy': {u'native': 'Frysk', u'name': 'Frisian'},
    u'ga': {u'native': 'Gaeilge', u'name': 'Irish Gaelic'},
    u'gd': {u'native': 'Gàidhlig', u'name': 'Scottish Gaelic'},
    u'gl': {u'native': 'Galego', u'name': 'Galician'},
    u'gn': {u'native': 'Guarani', u'name': 'Guarani'},
    u'gu': {u'native': 'ગુજરાતી', u'name': 'Gujarati'},
    u'gv': {u'native': 'Gaelg', u'name': 'Manx Gaelic'},
    u'ha': {u'native': 'هَوُس', u'name': 'Hausa'},
    u'he': {
        u'native': 'עברית',
        u'name': 'Hebrew',
        u'flag': u'countryflag/il',
    },
    u'hi': {
        u'native': 'हिंदी',
        u'name': 'Hindi',
        u'flag': u'countryflag/in',
    },
    u'ho': {u'native': 'Hiri Motu', u'name': 'Hiri Motu'},
    u'hr': {
        u'native': 'Hrvatski',
        u'name': 'Croatian',
        u'flag': u'countryflag/hr',
    },
    u'ht': {u'native': 'Kreyòl ayisyen', u'name': 'Haitian'},
    u'hu': {
        u'native': 'Magyar',
        u'name': 'Hungarian',
        u'flag': u'countryflag/hu',
    },
    u'hy': {
        u'native': 'Հայերէն',
        u'name': 'Armenian',
        u'flag': u'countryflag/am',
    },
    u'hz': {u'native': 'Otjiherero', u'name': 'Herero'},
    u'ia': {u'native': 'Interlingua', u'name': 'Interlingua'},
    u'id': {
        u'native': 'Bahasa Indonesia',
        u'name': 'Indonesian',
        u'flag': u'countryflag/id',
    },
    u'ie': {u'native': 'Interlingue', u'name': 'Interlingue'},
    u'ig': {u'native': 'Asụsụ Igbo', u'name': 'Igbo'},
    u'ii': {u'native': 'Nuosu', u'name': 'Nuosu'},
    u'ik': {u'native': 'Iñupiaq', u'name': 'Inupiak'},
    u'io': {u'native': 'Ido', u'name': 'Ido'},
    u'is': {
        u'native': 'Íslenska',
        u'name': 'Icelandic',
        u'flag': u'countryflag/is',
    },
    u'it': {
        u'native': 'Italiano',
        u'name': 'Italian',
        u'flag': u'countryflag/it',
    },
    u'iu': {u'native': 'ᐃᓄᒃᑎᑐᑦ', u'name': 'Inuktitut'},
    u'ja': {
        u'native': '日本語',
        u'name': 'Japanese',
        u'flag': u'countryflag/jp',
    },
    u'jv': {u'native': 'Javanese', u'name': 'basa Jawa'},
    u'ka': {
        u'native': 'ქართული',
        u'name': 'Georgian',
        u'flag': u'countryflag/ge',
    },
    u'kg': {u'native': 'KiKongo', u'name': 'Kongo'},
    u'ki': {u'native': 'Gĩkũyũ', u'name': 'Kikuyu'},
    u'kj': {u'native': 'Kuanyama', u'name': 'Kwanyama'},
    u'kk': {
        u'native': 'ﻗﺎﺯﺍﻗﺸﺎ',
        u'name': 'Kazakh',
        u'flag': u'countryflag/kz',
    },
    u'kl': {
        u'native': 'Greenlandic',
        u'name': 'Greenlandic',
        u'flag': u'countryflag/gl',
    },
    u'km': {
        u'native': 'ខ្មែរ',
        u'name': 'Cambodian/Khmer',
        u'flag': u'countryflag/kh',
    },
    u'kn': {
        u'native': 'ಕನ್ನಡ',
        u'name': 'Kannada',
        u'flag': u'countryflag/in',
    },
    u'ko': {
        u'native': '한국어',
        u'name': 'Korean',
        u'flag': u'countryflag/kr',
    },
    u'kr': {u'native': 'Kanuri', u'name': 'Kanuri'},
    u'ks': {
        u'native': 'काऽशुर',
        u'name': 'Kashmiri',
        u'flag': u'countryflag/in',
    },
    u'ku': {u'native': 'Kurdí', u'name': 'Kurdish'},
    u'kv': {u'native': 'коми кыв', u'name': 'Komi'},
    u'kw': {u'native': 'Kernewek', u'name': 'Cornish'},
    u'ky': {u'native': 'Кыргыз', u'name': 'Kirghiz'},
    u'la': {
        u'native': 'Latin',
        u'name': 'Latin',
        u'flag': u'countryflag/va',
    },
    u'lb': {
        u'native': 'Lëtzebuergesch',
        u'name': 'Luxemburgish',
        u'flag': u'countryflag/lu',
    },
    u'lg': {u'native': 'Luganda', u'name': 'Ganda'},
    u'li': {u'native': 'Limburgs', u'name': 'Limburgish'},
    u'ln': {u'native': 'Lingala', u'name': 'Lingala'},
    u'lo': {
        u'native': 'ພາສາລາວ',
        u'name': 'Laotian',
        u'flag': u'countryflag/la',
    },
    u'lt': {
        u'native': 'Lietuvių',
        u'name': 'Lithuanian',
        u'flag': u'countryflag/lt',
    },
    u'lu': {u'native': 'Tshiluba', u'name': 'Luba-Katanga'},
    u'lv': {
        u'native': 'Latviešu',
        u'name': 'Latvian',
        u'flag': u'countryflag/lv',
    },
    u'mg': {
        u'native': 'Malagasy',
        u'name': 'Madagascarian',
        u'flag': u'countryflag/mg',
    },
    u'mh': {u'native': 'Kajin M̧ajeļ', u'name': 'Marshallese'},
    u'mi': {u'native': 'Maori', u'name': 'Maori'},
    u'mk': {
        u'native': 'Македонски',
        u'name': 'Macedonian',
        u'flag': u'countryflag/mk',
    },
    u'ml': {u'native': 'മലയാളം', u'name': 'Malayalam'},
    u'mn': {
        u'native': 'Монгол',
        u'name': 'Mongolian',
        u'flag': u'countryflag/mn',
    },
    u'mo': {
        u'native': 'Moldavian',
        u'name': 'Moldavian',
        u'flag': u'countryflag/md',
    },
    u'mr': {u'native': 'मराठी', u'name': 'Marathi'},
    u'ms': {u'native': 'Bahasa Melayu', u'name': 'Malay'},
    u'mt': {
        u'native': 'Malti',
        u'name': 'Maltese',
        u'flag': u'countryflag/mt',
    },
    u'my': {u'native': 'Burmese', u'name': 'Burmese'},
    u'na': {
        u'native': 'Nauru',
        u'name': 'Nauruan',
        u'flag': u'countryflag/nr',
    },
    u'nb': {u'native': 'Norsk bokmål', u'name': 'Norwegian Bokmål'},
    u'nd': {u'native': 'Ndebele (North)', u'name': 'Ndebele (North)'},
    u'ne': {u'native': 'नेपाली', u'name': 'Nepali'},
    u'ng': {u'native': 'Owambo', u'name': 'Ndonga'},
    u'nl': {
        u'native': 'Nederlands',
        u'name': 'Dutch',
        u'flag': u'countryflag/nl',
    },
    u'nn': {
        u'native': 'Nynorsk',
        u'name': 'Nynorsk',
        u'flag': u'countryflag/no',
    },
    u'no': {
        u'native': 'Norsk',
        u'name': 'Norwegian',
        u'flag': u'countryflag/no',
    },
    u'nr': {u'native': 'IsiNdebele', u'name': 'Ndebele (South)'},
    u'nv': {u'native': 'Diné bizaad', u'name': 'Navajo'},
    u'ny': {u'native': 'chiCheŵa', u'name': 'Chichewa'},
    u'oc': {u'native': 'Occitan', u'name': 'Occitan'},
    u'oj': {u'native': 'ᐊᓂᔑᓈᐯᒧᐎᓐ', u'name': 'Ojibwe'},
    u'om': {u'native': 'Oromo', u'name': 'Oromo'},
    u'or': {u'native': 'ଓଡ଼ିଆ', u'name': 'Oriya'},
    u'os': {u'native': 'ирон æвзаг', u'name': 'Ossetian'},
    u'pa': {u'native': 'ਪੰਜਾਬੀ', u'name': 'Punjabi'},
    u'pi': {u'native': 'पाऴि', u'name': 'Pāli'},
    u'pl': {
        u'native': 'Polski',
        u'name': 'Polish',
        u'flag': u'countryflag/pl',
    },
    u'ps': {u'native': 'پښتو', u'name': 'Pashto'},
    u'pt': {
        u'native': 'Português',
        u'name': 'Portuguese',
        u'flag': u'countryflag/pt',
    },
    u'qu': {u'native': 'Quechua', u'name': 'Quechua'},
    u'rm': {u'native': 'Rhaeto-Romance', u'name': 'Rhaeto-Romance'},
    u'rn': {u'native': 'Kirundi', u'name': 'Kirundi'},
    u'ro': {
        u'native': 'Română',
        u'name': 'Romanian',
        u'flag': u'countryflag/ro',
    },
    u'ru': {
        u'native': 'Русский',
        u'name': 'Russian',
        u'flag': u'countryflag/ru',
    },
    u'rw': {u'native': 'Kinyarwanda', u'name': 'Kinyarwanda'},
    u'sa': {u'native': 'संस्कृत', u'name': 'Sanskrit'},
    u'sc': {u'native': 'sardu', u'name': 'Sardinian'},
    u'sd': {
        u'native': 'Sindhi',
        u'name': 'Sindhi',
        u'flag': u'countryflag/pk',
    },
    u'se': {u'native': 'Northern Sámi', u'name': 'Northern Sámi'},
    u'sg': {
        u'native': 'Sangho',
        u'name': 'Sangho',
        u'flag': u'countryflag/cf',
    },
    u'sh': {u'native': 'Serbo-Croatian', u'name': 'Serbo-Croatian'},
    u'si': {u'native': 'Singhalese', u'name': 'Singhalese'},
    u'sk': {
        u'native': 'Slovenčina',
        u'name': 'Slovak',
        u'flag': u'countryflag/sk',
    },
    u'sl': {
        u'native': 'Slovenščina',
        u'name': 'Slovenian',
        u'flag': u'countryflag/si',
    },
    u'sm': {u'native': 'Samoan', u'name': 'Samoan'},
    u'sn': {u'native': 'Shona', u'name': 'Shona'},
    u'so': {
        u'native': 'Somali',
        u'name': 'Somali',
        u'flag': u'countryflag/so',
    },
    u'sq': {
        u'native': 'Shqip',
        u'name': 'Albanian',
        u'flag': u'countryflag/al',
    },
    u'sr': {
        u'native': 'српски',
        u'name': 'Serbian',
        u'flag': u'countryflag/cs',
    },
    u'ss': {u'native': 'SiSwati', u'name': 'Swati'},
    u'st': {u'native': 'Sesotho', u'name': 'Southern Sotho'},
    u'su': {
        u'native': 'Sudanese',
        u'name': 'Sudanese',
        u'flag': u'countryflag/sd',
    },
    u'sv': {
        u'native': 'Svenska',
        u'name': 'Swedish',
        u'flag': u'countryflag/se',
    },
    u'sw': {u'native': 'Kiswahili', u'name': 'Swahili'},
    u'ta': {u'native': 'தமிழ', u'name': 'Tamil'},
    u'te': {u'native': 'తెలుగు', u'name': 'Telugu'},
    u'tg': {
        u'native': 'Тоҷики',
        u'name': 'Tadjik',
        u'flag': u'countryflag/tj',
    },
    u'th': {
        u'native': 'ไทย',
        u'name': 'Thai',
        u'flag': u'countryflag/th',
    },
    u'ti': {u'native': 'ትግርኛ', u'name': 'Tigrinya'},
    u'tk': {
        u'native': 'түркmенче',
        u'name': 'Turkmen',
        u'flag': u'countryflag/tm',
    },
    u'tl': {u'native': 'Tagalog', u'name': 'Tagalog'},
    u'tn': {
        u'native': 'Setswana',
        u'name': 'Tswana',
        u'flag': u'countryflag/bw',
    },
    u'to': {u'native': 'Tonga', u'name': 'Tonga'},
    u'tr': {
        u'native': 'Türkçe',
        u'name': 'Turkish',
        u'flag': u'countryflag/tr',
    },
    u'ts': {u'native': 'Xitsonga', u'name': 'Tsonga'},
    u'tt': {u'native': 'татарча', u'name': 'Tatar'},
    u'tw': {u'native': 'Twi', u'name': 'Twi'},
    u'ty': {u'native': 'Reo Tahiti', u'name': 'Tahitian'},
    u'ug': {u'native': 'Uigur', u'name': 'Uigur'},
    u'uk': {
        u'native': 'Українська',
        u'name': 'Ukrainian',
        u'flag': u'countryflag/ua',
    },
    u'ur': {u'native': 'اردو', u'name': 'Urdu'},
    u'uz': {
        u'native': 'Ўзбекча',
        u'name': 'Uzbek',
        u'flag': u'countryflag/uz',
    },
    u've': {u'native': 'Tshivenḓa', u'name': 'Venda'},
    u'vi': {
        u'native': 'Tiếng Việt',
        u'name': 'Vietnamese',
        u'flag': u'countryflag/vn',
    },
    u'vk': {u'native': 'Ovalingo', u'name': 'Viking'},
    u'vo': {u'native': 'Volapük', u'name': 'Volapük'},
    u'wa': {u'native': 'Walon', u'name': 'Walloon'},
    u'wo': {u'native': 'Wolof', u'name': 'Wolof'},
    u'xh': {u'native': 'IsiXhosa', u'name': 'Xhosa'},
    u'yi': {
        u'native': 'ײִדיש',
        u'name': 'Yiddish',
        u'flag': u'countryflag/il',
    },
    u'yo': {u'native': 'Yorùbá', u'name': 'Yorouba'},
    u'za': {u'native': 'Zhuang', u'name': 'Zhuang'},
    u'zh': {
        u'native': '中文',
        u'name': 'Chinese',
        u'flag': u'countryflag/cn',
    },
    u'zu': {
        u'native': 'IsiZulu',
        u'name': 'Zulu',
        u'flag': u'countryflag/za',
    },
}

# convert the utf-8 encoded values to unicode
for code in _languagelist:
    value = _languagelist[code]
    if u'name' in value:
        if six.PY3:
            value[u'name'] = value[u'name']
        else:
            value[u'name'] = unicode(value[u'name'], 'utf-8')
    if u'native' in value:
        if six.PY3:
            value[u'native'] = value[u'native']
        else:
            value[u'native'] = unicode(value[u'native'], 'utf-8')

_combinedlanguagelist = {
    u'ar-ae': {
        u'name': 'Arabic (United Arab Emirates)',
        u'flag': u'countryflag/ae',
    },
    u'ar-bh': {
        u'name': 'Arabic (Bahrain)',
        u'flag': u'countryflag/bh',
    },
    u'ar-dz': {
        u'name': 'Arabic (Algeria)',
        u'flag': u'countryflag/dz',
    },
    u'ar-eg': {
        u'name': 'Arabic (Egypt)',
        u'flag': u'countryflag/eg',
    },
    u'ar-il': {
        u'name': 'Arabic (Israel)',
        u'flag': u'countryflag/il',
    },
    u'ar-iq': {
        u'name': 'Arabic (Iraq)',
        u'flag': u'countryflag/iq',
    },
    u'ar-jo': {
        u'name': 'Arabic (Jordan)',
        u'flag': u'countryflag/jo',
    },
    u'ar-kw': {
        u'name': 'Arabic (Kuwait)',
        u'flag': u'countryflag/kw',
    },
    u'ar-lb': {
        u'name': 'Arabic (Lebanon)',
        u'flag': u'countryflag/lb',
    },
    u'ar-ly': {
        u'name': 'Arabic (Libya)',
        u'flag': u'countryflag/ly',
    },
    u'ar-ma': {
        u'name': 'Arabic (Morocco)',
        u'flag': u'countryflag/ma',
    },
    u'ar-mr': {
        u'name': 'Arabic (Mauritania)',
        u'flag': u'countryflag/mr',
    },
    u'ar-om': {
        u'name': 'Arabic (Oman)',
        u'flag': u'countryflag/om',
    },
    u'ar-ps': {
        u'name': 'Arabic (Palestinian West Bank and Gaza)',
        u'flag': u'countryflag/ps',
    },
    u'ar-qa': {
        u'name': 'Arabic (Qatar)',
        u'flag': u'countryflag/qa',
    },
    u'ar-sa': {
        u'name': 'Arabic (Saudi Arabia)',
        u'flag': u'countryflag/sa',
    },
    u'ar-sd': {
        u'name': 'Arabic (Sudan)',
        u'flag': u'countryflag/ly',
    },
    u'ar-so': {
        u'name': 'Arabic (Somalia)',
        u'flag': u'countryflag/so',
    },
    u'ar-sy': {
        u'name': 'Arabic (Syria)',
        u'flag': u'countryflag/sy',
    },
    u'ar-td': {
        u'name': 'Arabic (Chad)',
        u'flag': u'countryflag/td',
    },
    u'ar-tn': {
        u'name': 'Arabic (Tunisia)',
        u'flag': u'countryflag/ly',
    },
    u'ar-ye': {
        u'name': 'Arabic (Yemen)',
        u'flag': u'countryflag/ye',
    },
    u'bn-bd': {
        u'name': 'Bengali (Bangladesh)',
        u'flag': u'countryflag/bd',
    },
    u'bn-in': {
        u'name': 'Bengali (India)',
        u'flag': u'countryflag/in',
    },
    u'bn-sg': {
        u'name': 'Bengali (Singapore)',
        u'flag': u'countryflag/sg',
    },
    u'ch-gu': {
        u'name': 'Chamorro (Guam)',
        u'flag': u'countryflag/gu',
    },
    u'ch-mp': {
        u'name': 'Chamorro (Northern Mariana Islands)',
        u'flag': u'countryflag/mp',
    },
    u'cs-cz': {
        u'name': 'Czech (Czech republic)',
        u'native': 'Čeština (Česká republika)',
        u'flag': u'countryflag/cz',
    },
    u'da-dk': {
        u'name': 'Danish (Denmark)',
        u'flag': u'countryflag/dk',
    },
    u'da-gl': {
        u'name': 'Danish (Greenland)',
        u'flag': u'countryflag/gl',
    },
    u'de-at': {
        u'name': 'German (Austria)',
        u'native': 'Deutsch (Österreich)',
        u'flag': u'countryflag/at',
    },
    u'de-be': {
        u'name': 'German (Belgium)',
        u'flag': u'countryflag/de',
    },
    u'de-ch': {
        u'name': 'German (Switzerland)',
        u'flag': u'countryflag/ch',
    },
    u'de-de': {
        u'name': 'German (Germany)',
        u'flag': u'countryflag/de',
    },
    u'de-dk': {
        u'name': 'German (Denmark)',
        u'flag': u'countryflag/de',
    },
    u'de-li': {
        u'name': 'German (Liechtenstein)',
        u'flag': u'countryflag/li',
    },
    u'de-lu': {
        u'name': 'German (Luxembourg)',
        u'flag': u'countryflag/de',
    },
    u'el-cy': {
        u'name': 'Greek (Cyprus)',
        u'flag': u'countryflag/cy',
    },
    u'el-gr': {
        u'name': 'Greek (Greece)',
        u'flag': u'countryflag/gr',
    },
    u'en-ag': {
        u'name': 'English (Antigua and Barbuda)',
        u'flag': u'countryflag/ag',
    },
    u'en-ai': {
        u'name': 'English (Anguilla)',
        u'flag': u'countryflag/ai',
    },
    u'en-as': {
        u'name': 'English (American Samoa)',
        u'flag': u'countryflag/as',
    },
    u'en-au': {
        u'name': 'English (Australia)',
        u'flag': u'countryflag/au',
    },
    u'en-bb': {
        u'name': 'English (Barbados)',
        u'flag': u'countryflag/bb',
    },
    u'en-bm': {
        u'name': 'English (Bermuda)',
        u'flag': u'countryflag/bm',
    },
    u'en-bn': {
        u'name': 'English (Brunei)',
        u'flag': u'countryflag/bn',
    },
    u'en-bs': {
        u'name': 'English (Bahamas)',
        u'flag': u'countryflag/bs',
    },
    u'en-bw': {
        u'name': 'English (Botswana)',
        u'flag': u'countryflag/bw',
    },
    u'en-bz': {
        u'name': 'English (Belize)',
        u'flag': u'countryflag/bz',
    },
    u'en-ca': {
        u'name': 'English (Canada)',
        u'flag': u'countryflag/ca',
    },
    u'en-ck': {
        u'name': 'English (Cook Islands)',
        u'flag': u'countryflag/ck',
    },
    u'en-cm': {
        u'name': 'English (Cameroon)',
        u'flag': u'countryflag/cm',
    },
    u'en-dm': {
        u'name': 'English (Dominica)',
        u'flag': u'countryflag/dm',
    },
    u'en-er': {
        u'name': 'English (Eritrea)',
        u'flag': u'countryflag/er',
    },
    u'en-et': {
        u'name': 'English (Ethiopia)',
        u'flag': u'countryflag/et',
    },
    u'en-fj': {
        u'name': 'English (Fiji)',
        u'flag': u'countryflag/fj',
    },
    u'en-fk': {
        u'name': 'English (Falkland Islands)',
        u'flag': u'countryflag/fk',
    },
    u'en-fm': {
        u'name': 'English (Micronesia)',
        u'flag': u'countryflag/fm',
    },
    u'en-gb': {
        u'name': 'English (United Kingdom)',
        u'flag': u'countryflag/gb',
    },
    u'en-gd': {
        u'name': 'English (Grenada)',
        u'flag': u'countryflag/gd',
    },
    u'en-gh': {
        u'name': 'English (Ghana)',
        u'flag': u'countryflag/gh',
    },
    u'en-gi': {
        u'name': 'English (Gibraltar)',
        u'flag': u'countryflag/gi',
    },
    u'en-gm': {
        u'name': 'English (Gambia)',
        u'flag': u'countryflag/gm',
    },
    u'en-gu': {
        u'name': 'English (Guam)',
        u'flag': u'countryflag/gu',
    },
    u'en-gy': {
        u'name': 'English (Guyana)',
        u'flag': u'countryflag/gy',
    },
    u'en-ie': {
        u'name': 'English (Ireland)',
        u'flag': u'countryflag/ie',
    },
    u'en-il': {
        u'name': 'English (Israel)',
        u'flag': u'countryflag/gb',
    },
    u'en-io': {
        u'name': 'English (British Indian Ocean Territory)',
        u'flag': u'countryflag/io',
    },
    u'en-jm': {
        u'name': 'English (Jamaica)',
        u'flag': u'countryflag/jm',
    },
    u'en-ke': {
        u'name': 'English (Kenya)',
        u'flag': u'countryflag/ke',
    },
    u'en-ki': {
        u'name': 'English (Kiribati)',
        u'flag': u'countryflag/ki',
    },
    u'en-kn': {
        u'name': 'English (St. Kitts-Nevis)',
        u'flag': u'countryflag/kn',
    },
    u'en-ky': {
        u'name': 'English (Cayman Islands)',
        u'flag': u'countryflag/ky',
    },
    u'en-lc': {
        u'name': 'English (St. Lucia)',
        u'flag': u'countryflag/lc',
    },
    u'en-lr': {
        u'name': 'English (Liberia)',
        u'flag': u'countryflag/lr',
    },
    u'en-ls': {
        u'name': 'English (Lesotho)',
        u'flag': u'countryflag/ls',
    },
    u'en-mp': {
        u'name': 'English (Northern Mariana Islands)',
        u'flag': u'countryflag/mp',
    },
    u'en-ms': {
        u'name': 'English (Montserrat)',
        u'flag': u'countryflag/ms',
    },
    u'en-mt': {
        u'name': 'English (Malta)',
        u'flag': u'countryflag/mt',
    },
    u'en-mu': {
        u'name': 'English (Mauritius)',
        u'flag': u'countryflag/mu',
    },
    u'en-mw': {
        u'name': 'English (Malawi)',
        u'flag': u'countryflag/mw',
    },
    u'en-na': {
        u'name': 'English (Namibia)',
        u'flag': u'countryflag/na',
    },
    u'en-nf': {
        u'name': 'English (Norfolk Island)',
        u'flag': u'countryflag/nf',
    },
    u'en-ng': {
        u'name': 'English (Nigeria)',
        u'flag': u'countryflag/ng',
    },
    u'en-nr': {
        u'name': 'English (Nauru)',
        u'flag': u'countryflag/nr',
    },
    u'en-nu': {
        u'name': 'English (Niue)',
        u'flag': u'countryflag/nu',
    },
    u'en-nz': {
        u'name': 'English (New Zealand)',
        u'flag': u'countryflag/nz',
    },
    u'en-pg': {
        u'name': 'English (Papua New Guinea)',
        u'flag': u'countryflag/pg',
    },
    u'en-ph': {
        u'name': 'English (Philippines)',
        u'flag': u'countryflag/ph',
    },
    u'en-pk': {
        u'name': 'English (Pakistan)',
        u'flag': u'countryflag/pk',
    },
    u'en-pn': {
        u'name': 'English (Pitcairn)',
        u'flag': u'countryflag/pn',
    },
    u'en-pr': {
        u'name': 'English (Puerto Rico)',
        u'flag': u'countryflag/pr',
    },
    u'en-pw': {
        u'name': 'English (Palau)',
        u'flag': u'countryflag/pw',
    },
    u'en-rw': {
        u'name': 'English (Rwanda)',
        u'flag': u'countryflag/rw',
    },
    u'en-sb': {
        u'name': 'English (Solomon Islands)',
        u'flag': u'countryflag/sb',
    },
    u'en-sc': {
        u'name': 'English (Seychelles)',
        u'flag': u'countryflag/sc',
    },
    u'en-sg': {
        u'name': 'English (Singapore)',
        u'flag': u'countryflag/sg',
    },
    u'en-sh': {
        u'name': 'English (St. Helena)',
        u'flag': u'countryflag/sh',
    },
    u'en-sl': {
        u'name': 'English (Sierra Leone)',
        u'flag': u'countryflag/sl',
    },
    u'en-so': {
        u'name': 'English (Somalia)',
        u'flag': u'countryflag/so',
    },
    u'en-sz': {
        u'name': 'English (Swaziland)',
        u'flag': u'countryflag/sz',
    },
    u'en-tc': {
        u'name': 'English (Turks and Caicos Islands)',
        u'flag': u'countryflag/tc',
    },
    u'en-tk': {
        u'name': 'English (Tokelau)',
        u'flag': u'countryflag/tk',
    },
    u'en-to': {
        u'name': 'English (Tonga)',
        u'flag': u'countryflag/to',
    },
    u'en-tt': {
        u'name': 'English (Trinidad and Tobago)',
        u'flag': u'countryflag/tt',
    },
    u'en-ug': {
        u'name': 'English (Uganda)',
        u'flag': u'countryflag/ug',
    },
    u'en-us': {
        u'name': 'English (USA)',
        u'flag': u'countryflag/us',
    },
    u'en-vc': {
        u'name': 'English (St. Vincent and the Grenadi)',
        u'flag': u'countryflag/vc',
    },
    u'en-vg': {
        u'name': 'English (British Virgin Islands)',
        u'flag': u'countryflag/vg',
    },
    u'en-vi': {
        u'name': 'English (U.S. Virgin Islands)',
        u'flag': u'countryflag/vi',
    },
    u'en-vu': {
        u'name': 'English (Vanuatu)',
        u'flag': u'countryflag/vu',
    },
    u'en-ws': {
        u'name': 'English (Western Samoa)',
        u'flag': u'countryflag/ws',
    },
    u'en-za': {
        u'name': 'English (South Africa)',
        u'flag': u'countryflag/za',
    },
    u'en-zm': {
        u'name': 'English (Zambia)',
        u'flag': u'countryflag/zm',
    },
    u'en-zw': {
        u'name': 'English (Zimbabwe)',
        u'flag': u'countryflag/zw',
    },
    u'es-ar': {
        u'name': 'Spanish (Argentina)',
        u'flag': u'countryflag/ar',
    },
    u'es-bo': {
        u'name': 'Spanish (Bolivia)',
        u'flag': u'countryflag/bo',
    },
    u'es-cl': {
        u'name': 'Spanish (Chile)',
        u'flag': u'countryflag/cl',
    },
    u'es-co': {
        u'name': 'Spanish (Colombia)',
        u'flag': u'countryflag/co',
    },
    u'es-cr': {
        u'name': 'Spanish (Costa Rica)',
        u'flag': u'countryflag/cr',
    },
    u'es-cu': {
        u'name': 'Spanish (Cuba)',
        u'flag': u'countryflag/cu',
    },
    u'es-do': {
        u'name': 'Spanish (Dominican Republic)',
        u'flag': u'countryflag/do',
    },
    u'es-ec': {
        u'name': 'Spanish (Ecuador)',
        u'flag': u'countryflag/ec',
    },
    u'es-es': {
        u'name': 'Spanish (Spain)',
        u'flag': u'countryflag/es',
    },
    u'es-gq': {
        u'name': 'Spanish (Equatorial Guinea)',
        u'flag': u'countryflag/gq',
    },
    u'es-gt': {
        u'name': 'Spanish (Guatemala)',
        u'flag': u'countryflag/gt',
    },
    u'es-hn': {
        u'name': 'Spanish (Honduras)',
        u'flag': u'countryflag/hn',
    },
    u'es-mx': {
        u'name': 'Spanish (Mexico)',
        u'flag': u'countryflag/mx',
    },
    u'es-ni': {
        u'name': 'Spanish (Nicaragua)',
        u'flag': u'countryflag/ni',
    },
    u'es-pa': {
        u'name': 'Spanish (Panama)',
        u'flag': u'countryflag/pa',
    },
    u'es-pe': {
        u'name': 'Spanish (Peru)',
        u'flag': u'countryflag/pe',
    },
    u'es-pr': {
        u'name': 'Spanish (Puerto Rico)',
        u'flag': u'countryflag/pr',
    },
    u'es-py': {
        u'name': 'Spanish (Paraguay)',
        u'flag': u'countryflag/py',
    },
    u'es-sv': {
        u'name': 'Spanish (El Salvador)',
        u'flag': u'countryflag/sv',
    },
    u'es-us': {
        u'name': 'Spanish (USA)',
        u'flag': u'countryflag/us',
    },
    u'es-uy': {
        u'name': 'Spanish (Uruguay)',
        u'flag': u'countryflag/uy',
    },
    u'es-ve': {
        u'name': 'Spanish (Venezuela)',
        u'flag': u'countryflag/ve',
    },
    u'fr-ad': {
        u'name': 'French (Andorra)',
        u'flag': u'countryflag/ad',
    },
    u'fr-be': {
        u'name': 'French (Belgium)',
        u'flag': u'countryflag/be',
    },
    u'fr-bf': {
        u'name': 'French (Burkina Faso)',
        u'flag': u'countryflag/bf',
    },
    u'fr-bi': {
        u'name': 'French (Burundi)',
        u'flag': u'countryflag/bi',
    },
    u'fr-bj': {
        u'name': 'French (Benin)',
        u'flag': u'countryflag/bj',
    },
    u'fr-ca': {
        u'name': 'French (Canada)',
        u'flag': u'countryflag/ca',
    },
    u'fr-cd': {
        u'name': 'French (Democratic Republic of Congo)',
        u'flag': u'countryflag/cd',
    },
    u'fr-cf': {
        u'name': 'French (Central African Republic)',
        u'flag': u'countryflag/cf',
    },
    u'fr-cg': {
        u'name': 'French (Congo)',
        u'flag': u'countryflag/cg',
    },
    u'fr-ch': {
        u'name': 'French (Switzerland)',
        u'flag': u'countryflag/ch',
    },
    u'fr-ci': {
        u'name': 'French (Cote d\'Ivoire)',
        u'flag': u'countryflag/ci',
    },
    u'fr-cm': {
        u'name': 'French (Cameroon)',
        u'flag': u'countryflag/cm',
    },
    u'fr-dj': {
        u'name': 'French (Djibouti)',
        u'flag': u'countryflag/dj',
    },
    u'fr-fr': {
        u'name': 'French (France)',
        u'flag': u'countryflag/fr',
    },
    u'fr-ga': {
        u'name': 'French (Gabon)',
        u'flag': u'countryflag/ga',
    },
    u'fr-gb': {
        u'name': 'French (United Kingdom)',
        u'flag': u'countryflag/gb',
    },
    u'fr-gf': {
        u'name': 'French (French Guiana)',
        u'flag': u'countryflag/gf',
    },
    u'fr-gn': {
        u'name': 'French (Guinea)',
        u'flag': u'countryflag/gn',
    },
    u'fr-gp': {
        u'name': 'French (Guadeloupe)',
        u'flag': u'countryflag/gp',
    },
    u'fr-ht': {
        u'name': 'French (Haiti)',
        u'flag': u'countryflag/ht',
    },
    u'fr-it': {
        u'name': 'French (Italy)',
        u'flag': u'countryflag/it',
    },
    u'fr-km': {
        u'name': 'French (Comoros Islands)',
        u'flag': u'countryflag/km',
    },
    u'fr-lb': {
        u'name': 'French (Lebanon)',
        u'flag': u'countryflag/lb',
    },
    u'fr-lu': {
        u'name': 'French (Luxembourg)',
        u'flag': u'countryflag/lu',
    },
    u'fr-mc': {
        u'name': 'French (Monaco)',
        u'flag': u'countryflag/mc',
    },
    u'fr-mg': {
        u'name': 'French (Madagascar)',
        u'flag': u'countryflag/mg',
    },
    u'fr-ml': {
        u'name': 'French (Mali)',
        u'flag': u'countryflag/ml',
    },
    u'fr-mq': {
        u'name': 'French (Martinique)',
        u'flag': u'countryflag/mq',
    },
    u'fr-nc': {
        u'name': 'French (New Caledonia)',
        u'flag': u'countryflag/nc',
    },
    u'fr-pf': {
        u'name': 'French (French Polynesia)',
        u'flag': u'countryflag/pf',
    },
    u'fr-pm': {
        u'name': 'French (St. Pierre and Miquelon)',
        u'flag': u'countryflag/pm',
    },
    u'fr-re': {
        u'name': 'French (Reunion)',
        u'flag': u'countryflag/re',
    },
    u'fr-rw': {
        u'name': 'French (Rwanda)',
        u'flag': u'countryflag/rw',
    },
    u'fr-sc': {
        u'name': 'French (Seychelles)',
        u'flag': u'countryflag/sc',
    },
    u'fr-td': {
        u'name': 'French (Chad)',
        u'flag': u'countryflag/td',
    },
    u'fr-tg': {
        u'name': 'French (Togo)',
        u'flag': u'countryflag/tg',
    },
    u'fr-vu': {
        u'name': 'French (Vanuatu)',
        u'flag': u'countryflag/vu',
    },
    u'fr-wf': {
        u'name': 'French (Wallis and Futuna)',
        u'flag': u'countryflag/wf',
    },
    u'fr-yt': {
        u'name': 'French (Mayotte)',
        u'flag': u'countryflag/yt',
    },
    u'hr-ba': {
        u'name': 'Croatian (Bosnia-Herzegovina)',
        u'flag': u'countryflag/ba',
    },
    u'hr-hr': {
        u'name': 'Croatian (Croatia)',
        u'flag': u'countryflag/hr',
    },
    u'hu-hu': {
        u'name': 'Hungarian (Hungary)',
        u'flag': u'countryflag/hu',
    },
    u'hu-si': {
        u'name': 'Hungarian (Slovenia)',
        u'flag': u'countryflag/hu',
    },
    u'it-ch': {
        u'name': 'Italian (Switzerland)',
        u'flag': u'countryflag/it',
    },
    u'it-hr': {
        u'name': 'Italian (Croatia)',
        u'flag': u'countryflag/it',
    },
    u'it-it': {
        u'name': 'Italian (Italy)',
        u'flag': u'countryflag/it',
    },
    u'it-si': {
        u'name': 'Italian (Slovenia)',
        u'flag': u'countryflag/it',
    },
    u'it-sm': {
        u'name': 'Italian (San Marino)',
        u'flag': u'countryflag/sm',
    },
    u'ko-kp': {
        u'name': 'Korean (Korea, North)',
        u'flag': u'countryflag/kp',
    },
    u'ko-kr': {
        u'name': 'Korean (Korea, South)',
        u'flag': u'countryflag/kr',
    },
    u'ln-cd': {
        u'name': 'Lingala (Democratic Republic of Congo)',
        u'flag': u'countryflag/cd',
    },
    u'ln-cg': {
        u'name': 'Lingala (Congo)',
        u'flag': u'countryflag/cg',
    },
    u'ms-bn': {
        u'name': 'Malay (Brunei)',
        u'flag': u'countryflag/bn',
    },
    u'ms-my': {
        u'name': 'Malay (Malaysia)',
        u'flag': u'countryflag/my',
    },
    u'ms-sg': {
        u'name': 'Malay (Singapore)',
        u'flag': u'countryflag/sg',
    },
    u'nl-an': {
        u'name': 'Dutch (Netherlands Antilles)',
        u'flag': u'countryflag/an',
    },
    u'nl-aw': {
        u'name': 'Dutch (Aruba)',
        u'flag': u'countryflag/aw',
    },
    u'nl-be': {
        u'name': 'Dutch (Belgium)',
        u'flag': u'countryflag/be',
    },
    u'nl-nl': {
        u'name': 'Dutch (Netherlands)',
        u'flag': u'countryflag/nl',
    },
    u'nl-sr': {
        u'name': 'Dutch (Suriname)',
        u'flag': u'countryflag/sr',
    },
    u'pt-ao': {
        u'name': 'Portuguese (Angola)',
        u'native': 'Português (Angola)',
        u'flag': u'countryflag/ao',
    },
    u'pt-br': {
        u'name': 'Portuguese (Brazil)',
        u'native': 'Português (Brasil)',
        u'flag': u'countryflag/br',
    },
    u'pt-cv': {
        u'name': 'Portuguese (Ilhas Cabo Verde)',
        u'native': 'Português (Cabo Verde)',
        u'flag': u'countryflag/cv',
    },
    u'pt-gw': {
        u'name': 'Portuguese (Guiné-Bissau)',
        u'native': 'Português (Guiné-Bissau)',
        u'flag': u'countryflag/gw',
    },
    u'pt-mz': {
        u'name': 'Portuguese (Moçambique)',
        u'native': 'Português (Moçambique)',
        u'flag': u'countryflag/mz',
    },
    u'pt-pt': {
        u'name': 'Portuguese (Portugal)',
        u'native': 'Português (Portugal)',
        u'flag': u'countryflag/pt',
    },
    u'pt-st': {
        u'name': 'Portuguese (São Tomé e Príncipe)',
        u'native': 'Português (São Tomé e Príncipe)',
        u'flag': u'countryflag/st',
    },
    u'sd-in': {
        u'name': 'Sindhi (India)',
        u'flag': u'countryflag/in',
    },
    u'sd-pk': {
        u'name': 'Sindhi (Pakistan)',
        u'flag': u'countryflag/pk',
    },
    u'sr-ba': {
        u'name': 'Serbian (Bosnia-Herzegovina)',
        u'flag': u'countryflag/ba',
    },
    u'ss-sz': {
        u'name': 'Swati (Swaziland)',
        u'flag': u'countryflag/sz',
    },
    u'ss-za': {
        u'name': 'Swati (South Africa)',
        u'flag': u'countryflag/za',
    },
    u'sv-fi': {
        u'name': 'Swedish (Finland)',
        u'flag': u'countryflag/se',
    },
    u'sv-se': {
        u'name': 'Swedish (Sweden)',
        u'flag': u'countryflag/se',
    },
    u'sw-ke': {
        u'name': 'Swahili (Kenya)',
        u'flag': u'countryflag/ke',
    },
    u'sw-tz': {
        u'name': 'Swahili (Tanzania)',
        u'flag': u'countryflag/tz',
    },
    u'ta-in': {
        u'name': 'Tamil (India)',
        u'flag': u'countryflag/in',
    },
    u'ta-sg': {
        u'name': 'Tamil (Singapore)',
        u'flag': u'countryflag/sg',
    },
    u'tn-bw': {
        u'name': 'Tswana (Botswana)',
        u'flag': u'countryflag/bw',
    },
    u'tn-za': {
        u'name': 'Tswana (South Africa)',
        u'flag': u'countryflag/za',
    },
    u'tr-bg': {
        u'name': 'Turkish (Bulgaria)',
        u'flag': u'countryflag/tr',
    },
    u'tr-cy': {
        u'name': 'Turkish (Cyprus)',
        u'flag': u'countryflag/tr',
    },
    u'tr-tr': {
        u'name': 'Turkish (Turkey)',
        u'flag': u'countryflag/tr',
    },
    u'ur-in': {
        u'name': 'Urdu (India)',
        u'flag': u'countryflag/in',
    },
    u'ur-pk': {
        u'name': 'Urdu (Pakistan)',
        u'flag': u'countryflag/pk',
    },
    u'zh-cn': {
        u'name': 'Chinese (China)',
        u'native': '简体中文(中国)',
        u'flag': u'countryflag/cn',
    },
    u'zh-hk': {
        u'name': 'Chinese (Hongkong)',
        u'native': '繁體中文(香港)',
        u'flag': u'countryflag/hk',
    },
    u'zh-sg': {
        u'name': 'Chinese (Singapore)',
        u'native': '简体中文(新加坡)',
        u'flag': u'countryflag/sg',
    },
    u'zh-tw': {
        u'name': 'Chinese (Taiwan)',
        u'native': '繁體中文(臺灣)',
        u'flag': u'countryflag/tw',
    },
}

# convert the utf-8 encoded values to unicode
for code in _combinedlanguagelist:
    value = _combinedlanguagelist[code]
    if u'name' in value:
        if six.PY3:
            value[u'name'] = value[u'name']
        else:
            value[u'name'] = unicode(value[u'name'], 'utf-8')
    if u'native' in value:
        if six.PY3:
            value[u'native'] = value[u'native']
        else:
            value[u'native'] = unicode(value[u'native'], 'utf-8')
