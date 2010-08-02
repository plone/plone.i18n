# -*- coding: UTF-8 -*-

from plone.i18n.locales.interfaces import IContentLanguageAvailability
from plone.i18n.locales.interfaces import IMetadataLanguageAvailability
from plone.i18n.locales.interfaces import ILanguageAvailability
from zope.interface import implements

class LanguageAvailability(object):
    """A list of available languages.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ILanguageAvailability, LanguageAvailability)
      True
    """
    implements(ILanguageAvailability)

    def getAvailableLanguages(self, combined=False):
        """Return a sequence of language tags for available languages.
        """
        languages = _languagelist.keys()
        if combined:
            languages.extend(_combinedlanguagelist.keys())
        return languages

    def getLanguages(self, combined=False):
        """Return a sequence of Language objects for available languages.
        """
        languages = _languagelist.copy()
        if combined:
            languages.update(_combinedlanguagelist.copy())
        return languages

    def getLanguageListing(self, combined=False):
        """Return a sequence of language code and language name tuples.
        """
        languages = _languagelist.copy()
        if combined:
            languages.update(_combinedlanguagelist.copy())
        return [(code, languages[code][u'name']) for code in languages]


class ContentLanguageAvailability(LanguageAvailability):
    """A list of available content languages.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IContentLanguageAvailability, ContentLanguageAvailability)
      True
    """
    implements(IContentLanguageAvailability)

contentlanguages = ContentLanguageAvailability()

class MetadataLanguageAvailability(LanguageAvailability):
    """A list of available metadata languages.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IMetadataLanguageAvailability, MetadataLanguageAvailability)
      True
    """
    implements(IMetadataLanguageAvailability)

metadatalanguages = MetadataLanguageAvailability()

# This is a dictionary of dictonaries:
#
# 'langcode-variation' : {u'native' : 'Native name', u'name' : 'English name', u'flag' : u'/++resource++country-flags/*.gif'}

_languagelist = {
u'aa' : {u'native' : 'магIарул мацI', u'name' : 'Afar',                         u'flag' : u'/++resource++country-flags/dj.gif'},
u'ab' : {u'native' : 'бызшәа', u'name' : 'Abkhazian',                           u'flag' : u'/++resource++country-flags/ge.gif'},
u'af' : {u'native' : 'Afrikaans', u'name' : 'Afrikaans'},
u'am' : {u'native' : 'አማርኛ', u'name' : 'Amharic'},
u'ar' : {u'native' : 'العربية', u'name' : 'Arabic',                             u'flag' : '/++resource++language-flags/ar.gif'},
u'as' : {u'native' : 'অসমিয়া', u'name' : 'Assamese'},
u'ay' : {u'native' : 'Aymara', u'name' : 'Aymara'},
u'az' : {u'native' : 'Azəri Türkçəsi', u'name' : 'Azerbaijani',                 u'flag' : u'/++resource++country-flags/az.gif'},
u'ba' : {u'native' : 'Bashkir', u'name' : 'Bashkir'},
u'be' : {u'native' : 'Беларускі', u'name' : 'Belarussian',                      u'flag' : u'/++resource++country-flags/by.gif'},
u'bg' : {u'native' : 'Български', u'name' : 'Bulgarian',                        u'flag' : u'/++resource++country-flags/bg.gif'},
u'bh' : {u'native' : 'Bihari', u'name' : 'Bihari'},
u'bi' : {u'native' : 'Bislama', u'name' : 'Bislama'},
u'bn' : {u'native' : 'বাংলা', u'name' : 'Bengali',                              u'flag' : u'/++resource++country-flags/bd.gif'},
u'bo' : {u'native' : 'བོད་སྐད་', u'name' : 'Tibetan'},
u'bs' : {u'native' : 'Bosanski', u'name' : 'Bosnian',                           u'flag' : u'/++resource++country-flags/ba.gif'},
u'br' : {u'native' : 'Brezhoneg', u'name' : 'Breton'},
u'ca' : {u'native' : 'Català', u'name' : 'Catalan',                             u'flag' : u'/++resource++language-flags/ca.gif'},
u'co' : {u'native' : 'Corsu', u'name' : 'Corsican'},
u'cs' : {u'native' : 'Čeština', u'name' : 'Czech',                              u'flag' : u'/++resource++country-flags/cz.gif'},
u'cy' : {u'native' : 'Cymraeg', u'name' : 'Welsh',                              u'flag' : '/++resource++language-flags/cy.gif'},
u'da' : {u'native' : 'Dansk', u'name' : 'Danish',                               u'flag' : u'/++resource++country-flags/dk.gif'},
u'de' : {u'native' : 'Deutsch', u'name' : 'German',                             u'flag' : u'/++resource++country-flags/de.gif'},
u'dz' : {u'native' : 'Bhutani', u'name' : 'Indian Bhutani'},
u'el' : {u'native' : 'Ελληνικά', u'name' : 'Greek',                             u'flag' : u'/++resource++country-flags/gr.gif'},
u'en' : {u'native' : 'English', u'name' : 'English',                            u'flag' : u'/++resource++country-flags/gb.gif'},
u'eo' : {u'native' : 'Esperanto', u'name' : 'Esperanto',                        u'flag' : '/++resource++language-flags/eo.gif'},
u'es' : {u'native' : 'Español', u'name' : 'Spanish',                            u'flag' : u'/++resource++country-flags/es.gif'},
u'et' : {u'native' : 'Eesti', u'name' : 'Estonian',                             u'flag' : u'/++resource++country-flags/ee.gif'},
u'eu' : {u'native' : 'Euskara', u'name' : 'Basque',                             u'flag' : '/++resource++language-flags/eu.gif'},
u'fa' : {u'native' : 'فارسی', u'name' : 'Persian'},
u'fi' : {u'native' : 'Suomi', u'name' : 'Finnish',                              u'flag' : u'/++resource++country-flags/fi.gif'},
u'fj' : {u'native' : 'Fiji', u'name' : 'Fiji',                                  u'flag' : u'/++resource++country-flags/fj.gif'},
u'fo' : {u'native' : 'Føroyska', u'name' : 'Faroese',                           u'flag' : u'/++resource++country-flags/fo.gif'},
u'fr' : {u'native' : 'Français', u'name' : 'French',                            u'flag' : u'/++resource++country-flags/fr.gif'},
u'fy' : {u'native' : 'Frysk', u'name' : 'Frisian'},
u'ga' : {u'native' : 'Gaeilge', u'name' : 'Irish Gaelic'},
u'gd' : {u'native' : 'Gàidhlig', u'name' : 'Scottish Gaelic'},
u'gl' : {u'native' : 'Galego', u'name' : 'Galician'},
u'gn' : {u'native' : 'Guarani', u'name' : 'Guarani'},
u'gu' : {u'native' : 'ગુજરાતી', u'name' : 'Gujarati'},
u'gv' : {u'native' : 'Gaelg', u'name' : 'Manx Gaelic'},
u'ha' : {u'native' : 'هَوُس', u'name' : 'Hausa'},
u'he' : {u'native' : 'עברית', u'name' : 'Hebrew',                               u'flag' : u'/++resource++country-flags/il.gif'},
u'hi' : {u'native' : 'हिंदी', u'name' : 'Hindi',                                u'flag' : u'/++resource++country-flags/in.gif'},
u'hr' : {u'native' : 'Hrvatski', u'name' : 'Croatian',                          u'flag' : u'/++resource++country-flags/hr.gif'},
u'hu' : {u'native' : 'Magyar', u'name' : 'Hungarian',                           u'flag' : u'/++resource++country-flags/hu.gif'},
u'hy' : {u'native' : 'Հայերէն', u'name' : 'Armenian',                           u'flag' : u'/++resource++country-flags/am.gif'},
u'ia' : {u'native' : 'Interlingua', u'name' : 'Interlingua'},
u'id' : {u'native' : 'Bahasa Indonesia', u'name' : 'Indonesian',                u'flag' : u'/++resource++country-flags/id.gif'},
u'ie' : {u'native' : 'Interlingue', u'name' : 'Interlingue'},
u'ik' : {u'native' : 'Inupiak', u'name' : 'Inupiak'},
u'is' : {u'native' : 'Íslenska', u'name' : 'Icelandic',                         u'flag' : u'/++resource++country-flags/is.gif'},
u'it' : {u'native' : 'Italiano', u'name' : 'Italian',                           u'flag' : u'/++resource++country-flags/it.gif'},
u'iu' : {u'native' : 'ᐃᓄᒃᑎᑐᑦ', u'name' : 'Inuktitut'},
u'ja' : {u'native' : '日本語', u'name' : 'Japanese',                               u'flag' : u'/++resource++country-flags/jp.gif'},
u'jw' : {u'native' : 'Javanese', u'name' : 'Javanese'},
u'ka' : {u'native' : 'ქართული', u'name' : 'Georgian',                           u'flag' : u'/++resource++country-flags/ge.gif'},
u'kk' : {u'native' : 'ﻗﺎﺯﺍﻗﺸﺎ', u'name' : 'Kazakh',                             u'flag' : u'/++resource++country-flags/kz.gif'},
u'kl' : {u'native' : 'Greenlandic', u'name' : 'Greenlandic',                    u'flag' : u'/++resource++country-flags/gl.gif'},
u'km' : {u'native' : 'ខ្មែរ', u'name' : 'Cambodian/Khmer',                      u'flag' : u'/++resource++country-flags/kh.gif'},
u'kn' : {u'native' : 'ಕನ್ನಡ', u'name' : 'Kannada',                              u'flag' : u'/++resource++country-flags/in.gif'},
u'ko' : {u'native' : '한국어', u'name' : 'Korean',                                 u'flag' : u'/++resource++country-flags/kr.gif'},
u'ks' : {u'native' : 'काऽशुर', u'name' : 'Kashmiri',                            u'flag' : u'/++resource++country-flags/in.gif'},
u'ku' : {u'native' : 'Kurdí', u'name' : 'Kurdish'},
u'kw' : {u'native' : 'Kernewek', u'name' : 'Cornish'},
u'ky' : {u'native' : 'Кыргыз', u'name' : 'Kirghiz'},
u'la' : {u'native' : 'Latin', u'name' : 'Latin',                                u'flag' : u'/++resource++country-flags/va.gif'},
u'lb' : {u'native' : 'Lëtzebuergesch', u'name' : 'Luxemburgish',                u'flag' : u'/++resource++country-flags/lu.gif'},
u'li' : {u'native' : 'Limburgs', u'name' : 'Limburgish'},
u'ln' : {u'native' : 'Lingala', u'name' : 'Lingala'},
u'lo' : {u'native' : 'ພາສາລາວ', u'name' : 'Laotian',                            u'flag' : u'/++resource++country-flags/la.gif'},
u'lt' : {u'native' : 'Lietuviskai', u'name' : 'Lithuanian',                     u'flag' : u'/++resource++country-flags/lt.gif'},
u'lv' : {u'native' : 'Latviešu', u'name' : 'Latvian'},
u'me' : {u'native' : 'Crnogorski jezik', u'name' : 'Montenegrin'},
u'mg' : {u'native' : 'Malagasy', u'name' : 'Madagascarian',                     u'flag' : u'/++resource++country-flags/mg.gif'},
u'mi' : {u'native' : 'Maori', u'name' : 'Maori'},
u'mk' : {u'native' : 'Македонски', u'name' : 'Macedonian',                      u'flag' : u'/++resource++country-flags/mk.gif'},
u'ml' : {u'native' : 'മലയാളം', u'name' : 'Malayalam'},
u'mn' : {u'native' : 'Монгол', u'name' : 'Mongolian',                           u'flag' : u'/++resource++country-flags/mn.gif'},
u'mo' : {u'native' : 'Moldavian', u'name' : 'Moldavian',                        u'flag' : u'/++resource++country-flags/md.gif'},
u'mr' : {u'native' : 'मराठी', u'name' : 'Marathi'},
u'ms' : {u'native' : 'Bahasa Melayu', u'name' : 'Malay'},
u'mt' : {u'native' : 'Malti', u'name' : 'Maltese',                              u'flag' : u'/++resource++country-flags/mt.gif'},
u'my' : {u'native' : 'Burmese', u'name' : 'Burmese'},
u'na' : {u'native' : 'Nauru', u'name' : 'Nauruan',                              u'flag' : u'/++resource++country-flags/nr.gif'},
u'ne' : {u'native' : 'नेपाली', u'name' : 'Nepali'},
u'nl' : {u'native' : 'Nederlands', u'name' : 'Dutch',                           u'flag' : u'/++resource++country-flags/nl.gif'},
u'no' : {u'native' : 'Norsk', u'name' : 'Norwegian',                            u'flag' : u'/++resource++country-flags/no.gif'},
u'nn' : {u'native' : 'Nynorsk', u'name' : 'Nynorsk',                            u'flag' : u'/++resource++country-flags/no.gif'},
u'oc' : {u'native' : 'Occitan', u'name' : 'Occitan'},
u'om' : {u'native' : 'Oromo', u'name' : 'Oromo'},
u'or' : {u'native' : 'ଓଡ଼ିଆ', u'name' : 'Oriya'},
u'pa' : {u'native' : 'ਪੰਜਾਬੀ', u'name' : 'Punjabi'},
u'pl' : {u'native' : 'Polski', u'name' : 'Polish',                              u'flag' : u'/++resource++country-flags/pl.gif'},
u'ps' : {u'native' : 'پښتو', u'name' : 'Pashto'},
u'pt' : {u'native' : 'Português', u'name' : 'Portuguese',                       u'flag' : u'/++resource++country-flags/pt.gif'},
u'qu' : {u'native' : 'Quechua', u'name' : 'Quechua'},
u'rm' : {u'native' : 'Rhaeto-Romance', u'name' : 'Rhaeto-Romance'},
u'rn' : {u'native' : 'Kirundi', u'name' : 'Kirundi'},
u'ro' : {u'native' : 'Română', u'name' : 'Romanian',                            u'flag' : u'/++resource++country-flags/ro.gif'},
u'ru' : {u'native' : 'Русский', u'name' : 'Russian',                            u'flag' : u'/++resource++country-flags/ru.gif'},
u'rw' : {u'native' : 'Kiyarwanda', u'name' : 'Kiyarwanda'},
u'sa' : {u'native' : 'संस्कृत', u'name' : 'Sanskrit'},
u'sd' : {u'native' : 'Sindhi', u'name' : 'Sindhi',                              u'flag' : u'/++resource++country-flags/pk.gif'},
u'se' : {u'native' : 'Northern Sámi', u'name' : 'Northern Sámi'},
u'sg' : {u'native' : 'Sangho', u'name' : 'Sangho',                              u'flag' : u'/++resource++country-flags/cf.gif'},
u'sh' : {u'native' : 'Serbo-Croatian', u'name' : 'Serbo-Croatian'},
u'si' : {u'native' : 'Singhalese', u'name' : 'Singhalese'},
u'sk' : {u'native' : 'Slovenčina', u'name' : 'Slovak',                          u'flag' : u'/++resource++country-flags/sk.gif'},
u'sl' : {u'native' : 'Slovenščina', u'name' : 'Slovenian',                      u'flag' : u'/++resource++country-flags/si.gif'},
u'sm' : {u'native' : 'Samoan', u'name' : 'Samoan'},
u'sn' : {u'native' : 'Shona', u'name' : 'Shona'},
u'so' : {u'native' : 'Somali', u'name' : 'Somali',                              u'flag' : u'/++resource++country-flags/so.gif'},
u'sq' : {u'native' : 'Shqip', u'name' : 'Albanian',                             u'flag' : u'/++resource++country-flags/al.gif'},
u'sr' : {u'native' : 'српски', u'name' : 'Serbian',                             u'flag' : u'/++resource++country-flags/cs.gif'},
u'ss' : {u'native' : 'Siswati', u'name' : 'Siswati'},
u'st' : {u'native' : 'Sesotho', u'name' : 'Sesotho'},
u'su' : {u'native' : 'Sudanese', u'name' : 'Sudanese',                          u'flag' : u'/++resource++country-flags/sd.gif'},
u'sv' : {u'native' : 'Svenska', u'name' : 'Swedish',                            u'flag' : u'/++resource++country-flags/se.gif'},
u'sw' : {u'native' : 'Swahili', u'name' : 'Swahili'},
u'ta' : {u'native' : 'தமிழ', u'name' : 'Tamil'},
u'te' : {u'native' : 'తెలుగు', u'name' : 'Telugu'},
u'tg' : {u'native' : 'Тоҷики', u'name' : 'Tadjik',                              u'flag' : u'/++resource++country-flags/tj.gif'},
u'th' : {u'native' : 'ไทย', u'name' : 'Thai',                                   u'flag' : u'/++resource++country-flags/th.gif'},
u'ti' : {u'native' : 'ትግርኛ', u'name' : 'Tigrinya'},
u'tk' : {u'native' : 'түркmенче', u'name' : 'Turkmen',                          u'flag' : u'/++resource++country-flags/tm.gif'},
u'tl' : {u'native' : 'Tagalog', u'name' : 'Tagalog'},
u'tn' : {u'native' : 'Setswana', u'name' : 'Setswana',                          u'flag' : u'/++resource++country-flags/bw.gif'},
u'to' : {u'native' : 'Tonga', u'name' : 'Tonga'},
u'tr' : {u'native' : 'Türkçe', u'name' : 'Turkish',                             u'flag' : u'/++resource++country-flags/tr.gif'},
u'ts' : {u'native' : 'Tsonga', u'name' : 'Tsonga'},
u'tt' : {u'native' : 'татарча', u'name' : 'Tatar'},
u'tw' : {u'native' : 'Twi', u'name' : 'Twi'},
u'ug' : {u'native' : 'Uigur', u'name' : 'Uigur'},
u'uk' : {u'native' : 'Українська', u'name' : 'Ukrainian',                       u'flag' : u'/++resource++country-flags/ua.gif'},
u'ur' : {u'native' : 'اردو', u'name' : 'Urdu'},
u'uz' : {u'native' : 'Ўзбекча', u'name' : 'Uzbek',                              u'flag' : u'/++resource++country-flags/uz.gif'},
u'vi' : {u'native' : 'Tiếng Việt', u'name' : 'Vietnamese',                      u'flag' : u'/++resource++country-flags/vn.gif'},
u'vo' : {u'native' : 'Volapük', u'name' : 'Volapük'},
u'wa' : {u'native' : 'Walon', u'name' : 'Walloon'},
u'wo' : {u'native' : 'Wolof', u'name' : 'Wolof'},
u'xh' : {u'native' : 'isiXhosa', u'name' : 'Xhosa'},
u'yi' : {u'native' : 'ײִדיש', u'name' : 'Yiddish',                              u'flag' : u'/++resource++country-flags/il.gif'},
u'yo' : {u'native' : 'Yorùbá', u'name' : 'Yorouba'},
u'za' : {u'native' : 'Zhuang', u'name' : 'Zhuang'},
u'zh' : {u'native' : '中文', u'name' : 'Chinese',                                 u'flag' : u'/++resource++country-flags/cn.gif'},
u'zu' : {u'native' : 'isiZulu', u'name' : 'Zulu',                               u'flag' : u'/++resource++country-flags/za.gif'}
}

# convert the utf-8 encoded values to unicode
for code in _languagelist:
    value = _languagelist[code]
    if u'name' in value:
        value[u'name'] = unicode(value[u'name'], 'utf-8')
    if u'native' in value:
        value[u'native'] = unicode(value[u'native'], 'utf-8')

_combinedlanguagelist = {
u'ar-ae' : {u'name' : 'Arabic (United Arab Emirates)',                          u'flag' : u'/++resource++country-flags/ae.gif'},
u'ar-bh' : {u'name' : 'Arabic (Bahrain)',                                       u'flag' : u'/++resource++country-flags/bh.gif'},
u'ar-dz' : {u'name' : 'Arabic (Algeria)',                                       u'flag' : u'/++resource++country-flags/dz.gif'},
u'ar-eg' : {u'name' : 'Arabic (Egypt)',                                         u'flag' : u'/++resource++country-flags/eg.gif'},
u'ar-il' : {u'name' : 'Arabic (Israel)',                                        u'flag' : u'/++resource++country-flags/il.gif'},
u'ar-iq' : {u'name' : 'Arabic (Iraq)',                                          u'flag' : u'/++resource++country-flags/iq.gif'},
u'ar-jo' : {u'name' : 'Arabic (Jordan)',                                        u'flag' : u'/++resource++country-flags/jo.gif'},
u'ar-kw' : {u'name' : 'Arabic (Kuwait)',                                        u'flag' : u'/++resource++country-flags/kw.gif'},
u'ar-lb' : {u'name' : 'Arabic (Lebanon)',                                       u'flag' : u'/++resource++country-flags/lb.gif'},
u'ar-ly' : {u'name' : 'Arabic (Libya)',                                         u'flag' : u'/++resource++country-flags/ly.gif'},
u'ar-ma' : {u'name' : 'Arabic (Morocco)',                                       u'flag' : u'/++resource++country-flags/ma.gif'},
u'ar-mr' : {u'name' : 'Arabic (Mauritania)',                                    u'flag' : u'/++resource++country-flags/mr.gif'},
u'ar-om' : {u'name' : 'Arabic (Oman)',                                          u'flag' : u'/++resource++country-flags/om.gif'},
u'ar-ps' : {u'name' : 'Arabic (Palestinian West Bank and Gaza)',                u'flag' : u'/++resource++country-flags/ps.gif'},
u'ar-qa' : {u'name' : 'Arabic (Qatar)',                                         u'flag' : u'/++resource++country-flags/qa.gif'},
u'ar-sa' : {u'name' : 'Arabic (Saudi Arabia)',                                  u'flag' : u'/++resource++country-flags/sa.gif'},
u'ar-sd' : {u'name' : 'Arabic (Sudan)',                                         u'flag' : u'/++resource++country-flags/ly.gif'},
u'ar-so' : {u'name' : 'Arabic (Somalia)',                                       u'flag' : u'/++resource++country-flags/so.gif'},
u'ar-sy' : {u'name' : 'Arabic (Syria)',                                         u'flag' : u'/++resource++country-flags/sy.gif'},
u'ar-td' : {u'name' : 'Arabic (Chad)',                                          u'flag' : u'/++resource++country-flags/td.gif'},
u'ar-tn' : {u'name' : 'Arabic (Tunisia)',                                       u'flag' : u'/++resource++country-flags/ly.gif'},
u'ar-ye' : {u'name' : 'Arabic (Yemen)',                                         u'flag' : u'/++resource++country-flags/ye.gif'},
u'bn-bd' : {u'name' : 'Bengali (Bangladesh)',                                   u'flag' : u'/++resource++country-flags/bd.gif'},
u'bn-in' : {u'name' : 'Bengali (India)',                                        u'flag' : u'/++resource++country-flags/in.gif'},
u'bn-sg' : {u'name' : 'Bengali (Singapore)',                                    u'flag' : u'/++resource++country-flags/sg.gif'},
u'ch-gu' : {u'name' : 'Chamorro (Guam)',                                        u'flag' : u'/++resource++country-flags/gu.gif'},
u'ch-mp' : {u'name' : 'Chamorro (Northern Mariana Islands)',                    u'flag' : u'/++resource++country-flags/mp.gif'},
u'cs-cz' : {u'name' : 'Czech (Czech republic)', u'native': 'Čeština (Česká republika)', u'flag' : u'/++resource++country-flags/cz.gif'},
u'da-dk' : {u'name' : 'Danish (Denmark)',                                       u'flag' : u'/++resource++country-flags/dk.gif'},
u'da-gl' : {u'name' : 'Danish (Greenland)',                                     u'flag' : u'/++resource++country-flags/gl.gif'},
u'de-at' : {u'name' : 'German (Austria)', u'native' : 'Deutsch (Österreich)',   u'flag' : u'/++resource++country-flags/at.gif'},
u'de-be' : {u'name' : 'German (Belgium)',                                       u'flag' : u'/++resource++country-flags/de.gif'},
u'de-ch' : {u'name' : 'German (Switzerland)',                                   u'flag' : u'/++resource++country-flags/ch.gif'},
u'de-de' : {u'name' : 'German (Germany)',                                       u'flag' : u'/++resource++country-flags/de.gif'},
u'de-dk' : {u'name' : 'German (Denmark)',                                       u'flag' : u'/++resource++country-flags/de.gif'},
u'de-li' : {u'name' : 'German (Liechtenstein)',                                 u'flag' : u'/++resource++country-flags/li.gif'},
u'de-lu' : {u'name' : 'German (Luxembourg)',                                    u'flag' : u'/++resource++country-flags/de.gif'},
u'el-cy' : {u'name' : 'Greek (Cyprus)',                                         u'flag' : u'/++resource++country-flags/cy.gif'},
u'el-gr' : {u'name' : 'Greek (Greece)',                                         u'flag' : u'/++resource++country-flags/gr.gif'},
u'en-ag' : {u'name' : 'English (Antigua and Barbuda)',                          u'flag' : u'/++resource++country-flags/ag.gif'},
u'en-ai' : {u'name' : 'English (Anguilla)',                                     u'flag' : u'/++resource++country-flags/ai.gif'},
u'en-as' : {u'name' : 'English (American Samoa)',                               u'flag' : u'/++resource++country-flags/as.gif'},
u'en-au' : {u'name' : 'English (Australia)',                                    u'flag' : u'/++resource++country-flags/au.gif'},
u'en-bb' : {u'name' : 'English (Barbados)',                                     u'flag' : u'/++resource++country-flags/bb.gif'},
u'en-bm' : {u'name' : 'English (Bermuda)',                                      u'flag' : u'/++resource++country-flags/bm.gif'},
u'en-bn' : {u'name' : 'English (Brunei)',                                       u'flag' : u'/++resource++country-flags/bn.gif'},
u'en-bs' : {u'name' : 'English (Bahamas)',                                      u'flag' : u'/++resource++country-flags/bs.gif'},
u'en-bw' : {u'name' : 'English (Botswana)',                                     u'flag' : u'/++resource++country-flags/bw.gif'},
u'en-bz' : {u'name' : 'English (Belize)',                                       u'flag' : u'/++resource++country-flags/bz.gif'},
u'en-ca' : {u'name' : 'English (Canada)',                                       u'flag' : u'/++resource++country-flags/ca.gif'},
u'en-ck' : {u'name' : 'English (Cook Islands)',                                 u'flag' : u'/++resource++country-flags/ck.gif'},
u'en-cm' : {u'name' : 'English (Cameroon)',                                     u'flag' : u'/++resource++country-flags/cm.gif'},
u'en-dm' : {u'name' : 'English (Dominica)',                                     u'flag' : u'/++resource++country-flags/dm.gif'},
u'en-er' : {u'name' : 'English (Eritrea)',                                      u'flag' : u'/++resource++country-flags/er.gif'},
u'en-et' : {u'name' : 'English (Ethiopia)',                                     u'flag' : u'/++resource++country-flags/et.gif'},
u'en-fj' : {u'name' : 'English (Fiji)',                                         u'flag' : u'/++resource++country-flags/fj.gif'},
u'en-fk' : {u'name' : 'English (Falkland Islands)',                             u'flag' : u'/++resource++country-flags/fk.gif'},
u'en-fm' : {u'name' : 'English (Micronesia)',                                   u'flag' : u'/++resource++country-flags/fm.gif'},
u'en-gb' : {u'name' : 'English (United Kingdom)',                               u'flag' : u'/++resource++country-flags/gb.gif'},
u'en-gd' : {u'name' : 'English (Grenada)',                                      u'flag' : u'/++resource++country-flags/gd.gif'},
u'en-gh' : {u'name' : 'English (Ghana)',                                        u'flag' : u'/++resource++country-flags/gh.gif'},
u'en-gi' : {u'name' : 'English (Gibraltar)',                                    u'flag' : u'/++resource++country-flags/gi.gif'},
u'en-gm' : {u'name' : 'English (Gambia)',                                       u'flag' : u'/++resource++country-flags/gm.gif'},
u'en-gu' : {u'name' : 'English (Guam)',                                         u'flag' : u'/++resource++country-flags/gu.gif'},
u'en-gy' : {u'name' : 'English (Guyana)',                                       u'flag' : u'/++resource++country-flags/gy.gif'},
u'en-ie' : {u'name' : 'English (Ireland)',                                      u'flag' : u'/++resource++country-flags/ie.gif'},
u'en-il' : {u'name' : 'English (Israel)',                                       u'flag' : u'/++resource++country-flags/gb.gif'},
u'en-io' : {u'name' : 'English (British Indian Ocean Territory)',               u'flag' : u'/++resource++country-flags/io.gif'},
u'en-jm' : {u'name' : 'English (Jamaica)',                                      u'flag' : u'/++resource++country-flags/jm.gif'},
u'en-ke' : {u'name' : 'English (Kenya)',                                        u'flag' : u'/++resource++country-flags/ke.gif'},
u'en-ki' : {u'name' : 'English (Kiribati)',                                     u'flag' : u'/++resource++country-flags/ki.gif'},
u'en-kn' : {u'name' : 'English (St. Kitts-Nevis)',                              u'flag' : u'/++resource++country-flags/kn.gif'},
u'en-ky' : {u'name' : 'English (Cayman Islands)',                               u'flag' : u'/++resource++country-flags/ky.gif'},
u'en-lc' : {u'name' : 'English (St. Lucia)',                                    u'flag' : u'/++resource++country-flags/lc.gif'},
u'en-lr' : {u'name' : 'English (Liberia)',                                      u'flag' : u'/++resource++country-flags/lr.gif'},
u'en-ls' : {u'name' : 'English (Lesotho)',                                      u'flag' : u'/++resource++country-flags/ls.gif'},
u'en-mp' : {u'name' : 'English (Northern Mariana Islands)',                     u'flag' : u'/++resource++country-flags/mp.gif'},
u'en-ms' : {u'name' : 'English (Montserrat)',                                   u'flag' : u'/++resource++country-flags/ms.gif'},
u'en-mt' : {u'name' : 'English (Malta)',                                        u'flag' : u'/++resource++country-flags/mt.gif'},
u'en-mu' : {u'name' : 'English (Mauritius)',                                    u'flag' : u'/++resource++country-flags/mu.gif'},
u'en-mw' : {u'name' : 'English (Malawi)',                                       u'flag' : u'/++resource++country-flags/mw.gif'},
u'en-na' : {u'name' : 'English (Namibia)',                                      u'flag' : u'/++resource++country-flags/na.gif'},
u'en-nf' : {u'name' : 'English (Norfolk Island)',                               u'flag' : u'/++resource++country-flags/nf.gif'},
u'en-ng' : {u'name' : 'English (Nigeria)',                                      u'flag' : u'/++resource++country-flags/ng.gif'},
u'en-nr' : {u'name' : 'English (Nauru)',                                        u'flag' : u'/++resource++country-flags/nr.gif'},
u'en-nu' : {u'name' : 'English (Niue)',                                         u'flag' : u'/++resource++country-flags/nu.gif'},
u'en-nz' : {u'name' : 'English (New Zealand)',                                  u'flag' : u'/++resource++country-flags/nz.gif'},
u'en-pg' : {u'name' : 'English (Papua New Guinea)',                             u'flag' : u'/++resource++country-flags/pg.gif'},
u'en-ph' : {u'name' : 'English (Philippines)',                                  u'flag' : u'/++resource++country-flags/ph.gif'},
u'en-pk' : {u'name' : 'English (Pakistan)',                                     u'flag' : u'/++resource++country-flags/pk.gif'},
u'en-pn' : {u'name' : 'English (Pitcairn)',                                     u'flag' : u'/++resource++country-flags/pn.gif'},
u'en-pr' : {u'name' : 'English (Puerto Rico)',                                  u'flag' : u'/++resource++country-flags/pr.gif'},
u'en-pw' : {u'name' : 'English (Palau)',                                        u'flag' : u'/++resource++country-flags/pw.gif'},
u'en-rw' : {u'name' : 'English (Rwanda)',                                       u'flag' : u'/++resource++country-flags/rw.gif'},
u'en-sb' : {u'name' : 'English (Solomon Islands)',                              u'flag' : u'/++resource++country-flags/sb.gif'},
u'en-sc' : {u'name' : 'English (Seychelles)',                                   u'flag' : u'/++resource++country-flags/sc.gif'},
u'en-sg' : {u'name' : 'English (Singapore)',                                    u'flag' : u'/++resource++country-flags/sg.gif'},
u'en-sh' : {u'name' : 'English (St. Helena)',                                   u'flag' : u'/++resource++country-flags/sh.gif'},
u'en-sl' : {u'name' : 'English (Sierra Leone)',                                 u'flag' : u'/++resource++country-flags/sl.gif'},
u'en-so' : {u'name' : 'English (Somalia)',                                      u'flag' : u'/++resource++country-flags/so.gif'},
u'en-sz' : {u'name' : 'English (Swaziland)',                                    u'flag' : u'/++resource++country-flags/sz.gif'},
u'en-tc' : {u'name' : 'English (Turks and Caicos Islands)',                     u'flag' : u'/++resource++country-flags/tc.gif'},
u'en-tk' : {u'name' : 'English (Tokelau)',                                      u'flag' : u'/++resource++country-flags/tk.gif'},
u'en-to' : {u'name' : 'English (Tonga)',                                        u'flag' : u'/++resource++country-flags/to.gif'},
u'en-tt' : {u'name' : 'English (Trinidad and Tobago)',                          u'flag' : u'/++resource++country-flags/tt.gif'},
u'en-ug' : {u'name' : 'English (Uganda)',                                       u'flag' : u'/++resource++country-flags/ug.gif'},
u'en-us' : {u'name' : 'English (USA)',                                          u'flag' : u'/++resource++country-flags/us.gif'},
u'en-vc' : {u'name' : 'English (St. Vincent and the Grenadi)',                  u'flag' : u'/++resource++country-flags/vc.gif'},
u'en-vg' : {u'name' : 'English (British Virgin Islands)',                       u'flag' : u'/++resource++country-flags/vg.gif'},
u'en-vi' : {u'name' : 'English (U.S. Virgin Islands)',                          u'flag' : u'/++resource++country-flags/vi.gif'},
u'en-vu' : {u'name' : 'English (Vanuatu)',                                      u'flag' : u'/++resource++country-flags/vu.gif'},
u'en-ws' : {u'name' : 'English (Western Samoa)',                                u'flag' : u'/++resource++country-flags/ws.gif'},
u'en-za' : {u'name' : 'English (South Africa)',                                 u'flag' : u'/++resource++country-flags/za.gif'},
u'en-zm' : {u'name' : 'English (Zambia)',                                       u'flag' : u'/++resource++country-flags/zm.gif'},
u'en-zw' : {u'name' : 'English (Zimbabwe)',                                     u'flag' : u'/++resource++country-flags/zw.gif'},
u'es-ar' : {u'name' : 'Spanish (Argentina)',                                    u'flag' : u'/++resource++country-flags/ar.gif'},
u'es-bo' : {u'name' : 'Spanish (Bolivia)',                                      u'flag' : u'/++resource++country-flags/bo.gif'},
u'es-cl' : {u'name' : 'Spanish (Chile)',                                        u'flag' : u'/++resource++country-flags/cl.gif'},
u'es-co' : {u'name' : 'Spanish (Colombia)',                                     u'flag' : u'/++resource++country-flags/co.gif'},
u'es-cr' : {u'name' : 'Spanish (Costa Rica)',                                   u'flag' : u'/++resource++country-flags/cr.gif'},
u'es-cu' : {u'name' : 'Spanish (Cuba)',                                         u'flag' : u'/++resource++country-flags/cu.gif'},
u'es-do' : {u'name' : 'Spanish (Dominican Republic)',                           u'flag' : u'/++resource++country-flags/do.gif'},
u'es-ec' : {u'name' : 'Spanish (Ecuador)',                                      u'flag' : u'/++resource++country-flags/ec.gif'},
u'es-es' : {u'name' : 'Spanish (Spain)',                                        u'flag' : u'/++resource++country-flags/es.gif'},
u'es-gq' : {u'name' : 'Spanish (Equatorial Guinea)',                            u'flag' : u'/++resource++country-flags/gq.gif'},
u'es-gt' : {u'name' : 'Spanish (Guatemala)',                                    u'flag' : u'/++resource++country-flags/gt.gif'},
u'es-hn' : {u'name' : 'Spanish (Honduras)',                                     u'flag' : u'/++resource++country-flags/hn.gif'},
u'es-mx' : {u'name' : 'Spanish (Mexico)',                                       u'flag' : u'/++resource++country-flags/mx.gif'},
u'es-ni' : {u'name' : 'Spanish (Nicaragua)',                                    u'flag' : u'/++resource++country-flags/ni.gif'},
u'es-pa' : {u'name' : 'Spanish (Panama)',                                       u'flag' : u'/++resource++country-flags/pa.gif'},
u'es-pe' : {u'name' : 'Spanish (Peru)',                                         u'flag' : u'/++resource++country-flags/pe.gif'},
u'es-pr' : {u'name' : 'Spanish (Puerto Rico)',                                  u'flag' : u'/++resource++country-flags/pr.gif'},
u'es-py' : {u'name' : 'Spanish (Paraguay)',                                     u'flag' : u'/++resource++country-flags/py.gif'},
u'es-sv' : {u'name' : 'Spanish (El Salvador)',                                  u'flag' : u'/++resource++country-flags/sv.gif'},
u'es-us' : {u'name' : 'Spanish (USA)',                                          u'flag' : u'/++resource++country-flags/us.gif'},
u'es-uy' : {u'name' : 'Spanish (Uruguay)',                                      u'flag' : u'/++resource++country-flags/uy.gif'},
u'es-ve' : {u'name' : 'Spanish (Venezuela)',                                    u'flag' : u'/++resource++country-flags/ve.gif'},
u'fr-ad' : {u'name' : 'French (Andorra)',                                       u'flag' : u'/++resource++country-flags/ad.gif'},
u'fr-be' : {u'name' : 'French (Belgium)',                                       u'flag' : u'/++resource++country-flags/be.gif'},
u'fr-bf' : {u'name' : 'French (Burkina Faso)',                                  u'flag' : u'/++resource++country-flags/bf.gif'},
u'fr-bi' : {u'name' : 'French (Burundi)',                                       u'flag' : u'/++resource++country-flags/bi.gif'},
u'fr-bj' : {u'name' : 'French (Benin)',                                         u'flag' : u'/++resource++country-flags/bj.gif'},
u'fr-ca' : {u'name' : 'French (Canada)',                                        u'flag' : u'/++resource++country-flags/ca.gif'},
u'fr-cd' : {u'name' : 'French (Democratic Republic of Congo)',                  u'flag' : u'/++resource++country-flags/cd.gif'},
u'fr-cf' : {u'name' : 'French (Central African Republic)',                      u'flag' : u'/++resource++country-flags/cf.gif'},
u'fr-cg' : {u'name' : 'French (Congo)',                                         u'flag' : u'/++resource++country-flags/cg.gif'},
u'fr-ch' : {u'name' : 'French (Switzerland)',                                   u'flag' : u'/++resource++country-flags/ch.gif'},
u'fr-ci' : {u'name' : 'French (Cote d\'Ivoire)',                                u'flag' : u'/++resource++country-flags/ci.gif'},
u'fr-cm' : {u'name' : 'French (Cameroon)',                                      u'flag' : u'/++resource++country-flags/cm.gif'},
u'fr-dj' : {u'name' : 'French (Djibouti)',                                      u'flag' : u'/++resource++country-flags/dj.gif'},
u'fr-fr' : {u'name' : 'French (France)',                                        u'flag' : u'/++resource++country-flags/fr.gif'},
u'fr-ga' : {u'name' : 'French (Gabon)',                                         u'flag' : u'/++resource++country-flags/ga.gif'},
u'fr-gb' : {u'name' : 'French (United Kingdom)',                                u'flag' : u'/++resource++country-flags/gb.gif'},
u'fr-gf' : {u'name' : 'French (French Guiana)',                                 u'flag' : u'/++resource++country-flags/gf.gif'},
u'fr-gn' : {u'name' : 'French (Guinea)',                                        u'flag' : u'/++resource++country-flags/gn.gif'},
u'fr-gp' : {u'name' : 'French (Guadeloupe)',                                    u'flag' : u'/++resource++country-flags/gp.gif'},
u'fr-ht' : {u'name' : 'French (Haiti)',                                         u'flag' : u'/++resource++country-flags/ht.gif'},
u'fr-it' : {u'name' : 'French (Italy)',                                         u'flag' : u'/++resource++country-flags/it.gif'},
u'fr-km' : {u'name' : 'French (Comoros Islands)',                               u'flag' : u'/++resource++country-flags/km.gif'},
u'fr-lb' : {u'name' : 'French (Lebanon)',                                       u'flag' : u'/++resource++country-flags/lb.gif'},
u'fr-lu' : {u'name' : 'French (Luxembourg)',                                    u'flag' : u'/++resource++country-flags/lu.gif'},
u'fr-mc' : {u'name' : 'French (Monaco)',                                        u'flag' : u'/++resource++country-flags/mc.gif'},
u'fr-mg' : {u'name' : 'French (Madagascar)',                                    u'flag' : u'/++resource++country-flags/mg.gif'},
u'fr-ml' : {u'name' : 'French (Mali)',                                          u'flag' : u'/++resource++country-flags/ml.gif'},
u'fr-mq' : {u'name' : 'French (Martinique)',                                    u'flag' : u'/++resource++country-flags/mq.gif'},
u'fr-nc' : {u'name' : 'French (New Caledonia)',                                 u'flag' : u'/++resource++country-flags/nc.gif'},
u'fr-pf' : {u'name' : 'French (French Polynesia)',                              u'flag' : u'/++resource++country-flags/pf.gif'},
u'fr-pm' : {u'name' : 'French (St. Pierre and Miquelon)',                       u'flag' : u'/++resource++country-flags/pm.gif'},
u'fr-re' : {u'name' : 'French (Reunion)',                                       u'flag' : u'/++resource++country-flags/re.gif'},
u'fr-rw' : {u'name' : 'French (Rwanda)',                                        u'flag' : u'/++resource++country-flags/rw.gif'},
u'fr-sc' : {u'name' : 'French (Seychelles)',                                    u'flag' : u'/++resource++country-flags/sc.gif'},
u'fr-td' : {u'name' : 'French (Chad)',                                          u'flag' : u'/++resource++country-flags/td.gif'},
u'fr-tg' : {u'name' : 'French (Togo)',                                          u'flag' : u'/++resource++country-flags/tg.gif'},
u'fr-vu' : {u'name' : 'French (Vanuatu)',                                       u'flag' : u'/++resource++country-flags/vu.gif'},
u'fr-wf' : {u'name' : 'French (Wallis and Futuna)',                             u'flag' : u'/++resource++country-flags/wf.gif'},
u'fr-yt' : {u'name' : 'French (Mayotte)',                                       u'flag' : u'/++resource++country-flags/yt.gif'},
u'hr-ba' : {u'name' : 'Croatian (Bosnia-Herzegovina)',                          u'flag' : u'/++resource++country-flags/ba.gif'},
u'hr-hr' : {u'name' : 'Croatian (Croatia)',                                     u'flag' : u'/++resource++country-flags/hr.gif'},
u'hu-hu' : {u'name' : 'Hungarian (Hungary)',                                    u'flag' : u'/++resource++country-flags/hu.gif'},
u'hu-si' : {u'name' : 'Hungarian (Slovenia)',                                   u'flag' : u'/++resource++country-flags/hu.gif'},
u'it-ch' : {u'name' : 'Italian (Switzerland)',                                  u'flag' : u'/++resource++country-flags/it.gif'},
u'it-hr' : {u'name' : 'Italian (Croatia)',                                      u'flag' : u'/++resource++country-flags/it.gif'},
u'it-it' : {u'name' : 'Italian (Italy)',                                        u'flag' : u'/++resource++country-flags/it.gif'},
u'it-si' : {u'name' : 'Italian (Slovenia)',                                     u'flag' : u'/++resource++country-flags/it.gif'},
u'it-sm' : {u'name' : 'Italian (San Marino)',                                   u'flag' : u'/++resource++country-flags/sm.gif'},
u'ko-kp' : {u'name' : 'Korean (Korea, North)',                                  u'flag' : u'/++resource++country-flags/kp.gif'},
u'ko-kr' : {u'name' : 'Korean (Korea, South)',                                  u'flag' : u'/++resource++country-flags/kr.gif'},
u'ln-cd' : {u'name' : 'Lingala (Democratic Republic of Congo)',                 u'flag' : u'/++resource++country-flags/cd.gif'},
u'ln-cg' : {u'name' : 'Lingala (Congo)',                                        u'flag' : u'/++resource++country-flags/cg.gif'},
u'ms-bn' : {u'name' : 'Malay (Brunei)',                                         u'flag' : u'/++resource++country-flags/bn.gif'},
u'ms-my' : {u'name' : 'Malay (Malaysia)',                                       u'flag' : u'/++resource++country-flags/my.gif'},
u'ms-sg' : {u'name' : 'Malay (Singapore)',                                      u'flag' : u'/++resource++country-flags/sg.gif'},
u'nl-an' : {u'name' : 'Dutch (Netherlands Antilles)',                           u'flag' : u'/++resource++country-flags/an.gif'},
u'nl-aw' : {u'name' : 'Dutch (Aruba)',                                          u'flag' : u'/++resource++country-flags/aw.gif'},
u'nl-be' : {u'name' : 'Dutch (Belgium)',                                        u'flag' : u'/++resource++country-flags/be.gif'},
u'nl-nl' : {u'name' : 'Dutch (Netherlands)',                                    u'flag' : u'/++resource++country-flags/nl.gif'},
u'nl-sr' : {u'name' : 'Dutch (Suriname)',                                       u'flag' : u'/++resource++country-flags/sr.gif'},
u'pt-ao' : {u'name' : 'Portuguese (Angola)', u'native': 'Português (Angola)',   u'flag' : u'/++resource++country-flags/ao.gif'},
u'pt-br' : {u'name' : 'Portuguese (Brazil)', u'native' : 'Português (Brasil)',  u'flag' : u'/++resource++country-flags/br.gif'},
u'pt-cv' : {u'name' : 'Portuguese (Ilhas Cabo Verde)', u'native': 'Português (Cabo Verde)', u'flag' : u'/++resource++country-flags/cv.gif'},
u'pt-gw' : {u'name' : 'Portuguese (Guiné-Bissau)', u'native': 'Português (Guiné-Bissau)', u'flag' : u'/++resource++country-flags/gw.gif'},
u'pt-mz' : {u'name' : 'Portuguese (Moçambique)', u'native': 'Português (Moçambique)', u'flag' : u'/++resource++country-flags/mz.gif'},
u'pt-pt' : {u'name' : 'Portuguese (Portugal)', u'native': 'Português (Portugal)', u'flag' : u'/++resource++country-flags/pt.gif'},
u'pt-st' : {u'name' : 'Portuguese (São Tomé e Príncipe)', u'native': 'Português (São Tomé e Príncipe)', u'flag' : u'/++resource++country-flags/st.gif'},
u'sd-in' : {u'name' : 'Sindhi (India)',                                         u'flag' : u'/++resource++country-flags/in.gif'},
u'sd-pk' : {u'name' : 'Sindhi (Pakistan)',                                      u'flag' : u'/++resource++country-flags/pk.gif'},
u'sr-ba' : {u'name' : 'Serbian (Bosnia-Herzegovina)',                           u'flag' : u'/++resource++country-flags/ba.gif'},
u'ss-sz' : {u'name' : 'Swati (Swaziland)',                                      u'flag' : u'/++resource++country-flags/sz.gif'},
u'ss-za' : {u'name' : 'Swati (South Africa)',                                   u'flag' : u'/++resource++country-flags/za.gif'},
u'sv-fi' : {u'name' : 'Swedish (Finland)',                                      u'flag' : u'/++resource++country-flags/se.gif'},
u'sv-se' : {u'name' : 'Swedish (Sweden)',                                       u'flag' : u'/++resource++country-flags/se.gif'},
u'sw-ke' : {u'name' : 'Swahili (Kenya)',                                        u'flag' : u'/++resource++country-flags/ke.gif'},
u'sw-tz' : {u'name' : 'Swahili (Tanzania)',                                     u'flag' : u'/++resource++country-flags/tz.gif'},
u'ta-in' : {u'name' : 'Tamil (India)',                                          u'flag' : u'/++resource++country-flags/in.gif'},
u'ta-sg' : {u'name' : 'Tamil (Singapore)',                                      u'flag' : u'/++resource++country-flags/sg.gif'},
u'tn-bw' : {u'name' : 'Tswana (Botswana)',                                      u'flag' : u'/++resource++country-flags/bw.gif'},
u'tn-za' : {u'name' : 'Tswana (South Africa)',                                  u'flag' : u'/++resource++country-flags/za.gif'},
u'tr-bg' : {u'name' : 'Turkish (Bulgaria)',                                     u'flag' : u'/++resource++country-flags/tr.gif'},
u'tr-cy' : {u'name' : 'Turkish (Cyprus)',                                       u'flag' : u'/++resource++country-flags/tr.gif'},
u'tr-tr' : {u'name' : 'Turkish (Turkey)',                                       u'flag' : u'/++resource++country-flags/tr.gif'},
u'ur-in' : {u'name' : 'Urdu (India)',                                           u'flag' : u'/++resource++country-flags/in.gif'},
u'ur-pk' : {u'name' : 'Urdu (Pakistan)',                                        u'flag' : u'/++resource++country-flags/pk.gif'},
u'zh-cn' : {u'name' : 'Chinese (China)', u'native' : '简体中文(中国)',                u'flag' : u'/++resource++country-flags/cn.gif'},
u'zh-hk' : {u'name' : 'Chinese (Hongkong)', u'native' : '繁體中文(香港)',             u'flag' : u'/++resource++country-flags/hk.gif'},
u'zh-sg' : {u'name' : 'Chinese (Singapore)', u'native' : '简体中文(新加坡)',           u'flag' : u'/++resource++country-flags/sg.gif'},
u'zh-tw' : {u'name' : 'Chinese (Taiwan)', u'native' : '繁體中文(臺灣)',               u'flag' : u'/++resource++country-flags/tw.gif'}
}

# convert the utf-8 encoded values to unicode
for code in _combinedlanguagelist:
    value = _combinedlanguagelist[code]
    if u'name' in value:
        value[u'name'] = unicode(value[u'name'], 'utf-8')
    if u'native' in value:
        value[u'native'] = unicode(value[u'native'], 'utf-8')
