# -*- coding: UTF-8 -*-

from plone.i18n.locales.interfaces import ICountryAvailability
from zope.interface import implementer

import six


@implementer(ICountryAvailability)
class CountryAvailability(object):
    """A list of available coutries."""

    def getAvailableCountries(self):
        """Return a sequence of country tags for available countries."""
        return list(_countrylist.keys())

    def getCountries(self):
        """Return a sequence of Country objects for available countries."""
        return _countrylist.copy()

    def getCountryListing(self):
        """Return a sequence of country code and country name tuples."""
        return [(code, _countrylist[code][u'name']) for code in _countrylist]


countries = CountryAvailability()

# This is a dictionary of dictonaries:
#
# 'country-code' : {
#     u'name' : 'English name',
#     u'flag' : u'countryflag/*',
# }
#
# This list follows ISO 3166-1. In addition the following reservations are
# part of the list for historical reasons: an

_countrylist = {
    u'ad': {u'name': 'Andorra', u'flag': u'countryflag/ad'},
    u'ae': {
        u'name': 'United Arab Emirates',
        u'flag': u'countryflag/ae',
    },
    u'af': {
        u'name': 'Afghanistan',
        u'flag': u'countryflag/af',
    },
    u'ag': {
        u'name': 'Antigua and Barbuda',
        u'flag': u'countryflag/ag',
    },
    u'ai': {
        u'name': 'Anguilla',
        u'flag': u'countryflag/ai',
    },
    u'al': {u'name': 'Albania', u'flag': u'countryflag/al'},
    u'am': {u'name': 'Armenia', u'flag': u'countryflag/am'},
    u'an': {
        u'name': 'Netherlands Antilles',
        u'flag': u'countryflag/an',
    },
    u'ao': {u'name': 'Angola', u'flag': u'countryflag/ao'},
    u'aq': {
        u'name': 'Antarctica',
        u'flag': u'countryflag/aq',
    },
    u'ar': {
        u'name': 'Argentina',
        u'flag': u'countryflag/ar',
    },
    u'as': {
        u'name': 'American Samoa',
        u'flag': u'countryflag/as',
    },
    u'at': {u'name': 'Austria', u'flag': u'countryflag/at'},
    u'au': {
        u'name': 'Australia',
        u'flag': u'countryflag/au',
    },
    u'aw': {u'name': 'Aruba', u'flag': u'countryflag/aw'},
    u'ax': {
        u'name': 'Oland Islands',
        u'flag': u'countryflag/ax',
    },
    u'az': {
        u'name': 'Azerbaijan',
        u'flag': u'countryflag/az',
    },
    u'ba': {
        u'name': 'Bosnia and Herzegovina',
        u'flag': u'countryflag/ba',
    },
    u'bb': {
        u'name': 'Barbados',
        u'flag': u'countryflag/bb',
    },
    u'bd': {
        u'name': 'Bangladesh',
        u'flag': u'countryflag/bd',
    },
    u'be': {u'name': 'Belgium', u'flag': u'countryflag/be'},
    u'bf': {
        u'name': 'Burkina Faso',
        u'flag': u'countryflag/bf',
    },
    u'bg': {
        u'name': 'Bulgaria',
        u'flag': u'countryflag/bg',
    },
    u'bh': {u'name': 'Bahrain', u'flag': u'countryflag/bh'},
    u'bi': {u'name': 'Burundi', u'flag': u'countryflag/bi'},
    u'bj': {u'name': 'Benin', u'flag': u'countryflag/bj'},
    u'bl': {
        u'name': 'Saint Barthélemy',
        u'flag': u'countryflag/bl',
    },
    u'bm': {u'name': 'Bermuda', u'flag': u'countryflag/bm'},
    u'bn': {
        u'name': 'Brunei Darussalam',
        u'flag': u'countryflag/bn',
    },
    u'bo': {u'name': 'Bolivia', u'flag': u'countryflag/bo'},
    u'bq': {
        u'name': 'Bonaire, Sint Eustatius and Saba',
        u'flag': u'countryflag/bq',
    },
    u'br': {u'name': 'Brazil', u'flag': u'countryflag/br'},
    u'bs': {u'name': 'Bahamas', u'flag': u'countryflag/bs'},
    u'bt': {u'name': 'Bhutan', u'flag': u'countryflag/bt'},
    u'bv': {
        u'name': 'Bouvet Island',
        u'flag': u'countryflag/bv',
    },
    u'bw': {
        u'name': 'Botswana',
        u'flag': u'countryflag/bw',
    },
    u'by': {u'name': 'Belarus', u'flag': u'countryflag/by'},
    u'bz': {u'name': 'Belize', u'flag': u'countryflag/bz'},
    u'ca': {u'name': 'Canada', u'flag': u'countryflag/ca'},
    u'cc': {
        u'name': 'Cocos (Keeling) Islands',
        u'flag': u'countryflag/cc',
    },
    u'cd': {
        u'name': 'Congo The Democratic Republic of',
        u'flag': u'countryflag/cd',
    },
    u'cf': {
        u'name': 'Central African Republic',
        u'flag': u'countryflag/cf',
    },
    u'cg': {u'name': 'Congo', u'flag': u'countryflag/cg'},
    u'ch': {
        u'name': 'Switzerland',
        u'flag': u'countryflag/ch',
    },
    u'ci': {
        u'name': "Cote d'Ivoire",
        u'flag': u'countryflag/ci',
    },
    u'ck': {
        u'name': 'Cook Islands',
        u'flag': u'countryflag/ck',
    },
    u'cl': {u'name': 'Chile', u'flag': u'countryflag/cl'},
    u'cm': {
        u'name': 'Cameroon',
        u'flag': u'countryflag/cm',
    },
    u'cn': {u'name': 'China', u'flag': u'countryflag/cn'},
    u'co': {
        u'name': 'Colombia',
        u'flag': u'countryflag/co',
    },
    u'cr': {
        u'name': 'Costa Rica',
        u'flag': u'countryflag/cr',
    },
    u'cs': {
        u'name': 'Serbia and Montenegro',
        u'flag': u'countryflag/cs',
    },
    u'cu': {u'name': 'Cuba', u'flag': u'countryflag/cu'},
    u'cv': {
        u'name': 'Cape Verde',
        u'flag': u'countryflag/cv',
    },
    u'cw': {u'name': 'Curaçao', u'flag': u'countryflag/cw.png'},
    u'cx': {
        u'name': 'Christmas Island',
        u'flag': u'countryflag/cx',
    },
    u'cy': {u'name': 'Cyprus', u'flag': u'countryflag/cy'},
    u'cz': {
        u'name': 'Czech Republic',
        u'flag': u'countryflag/cz',
    },
    u'de': {u'name': 'Germany', u'flag': u'countryflag/de'},
    u'dj': {
        u'name': 'Djibouti',
        u'flag': u'countryflag/dj',
    },
    u'dk': {u'name': 'Denmark', u'flag': u'countryflag/dk'},
    u'dm': {
        u'name': 'Dominica',
        u'flag': u'countryflag/dm',
    },
    u'do': {
        u'name': 'Dominican Republic',
        u'flag': u'countryflag/do',
    },
    u'dz': {u'name': 'Algeria', u'flag': u'countryflag/dz'},
    u'ec': {u'name': 'Ecuador', u'flag': u'countryflag/ec'},
    u'ee': {u'name': 'Estonia', u'flag': u'countryflag/ee'},
    u'eg': {u'name': 'Egypt', u'flag': u'countryflag/eg'},
    u'eh': {
        u'name': 'Western Sahara',
        u'flag': u'countryflag/eh',
    },
    u'er': {u'name': 'Eritrea', u'flag': u'countryflag/er'},
    u'es': {u'name': 'Spain', u'flag': u'countryflag/es'},
    u'et': {
        u'name': 'Ethiopia',
        u'flag': u'countryflag/et',
    },
    u'fi': {u'name': 'Finland', u'flag': u'countryflag/fi'},
    u'fj': {u'name': 'Fiji', u'flag': u'countryflag/fj'},
    u'fk': {
        u'name': 'Falkland Islands (Malvinas)',
        u'flag': u'countryflag/fk',
    },
    u'fm': {
        u'name': 'Micronesia Federated States of',
        u'flag': u'countryflag/fm',
    },
    u'fo': {
        u'name': 'Faroe Islands',
        u'flag': u'countryflag/fo',
    },
    u'fr': {u'name': 'France', u'flag': u'countryflag/fr'},
    u'ga': {u'name': 'Gabon', u'flag': u'countryflag/ga'},
    u'gb': {
        u'name': 'United Kingdom',
        u'flag': u'countryflag/gb',
    },
    u'gd': {u'name': 'Grenada', u'flag': u'countryflag/gd'},
    u'ge': {u'name': 'Georgia', u'flag': u'countryflag/ge'},
    u'gf': {
        u'name': 'French Guiana',
        u'flag': u'countryflag/gf',
    },
    u'gg': {
        u'name': 'Guernsey',
        u'flag': u'countryflag/gg',
    },
    u'gh': {u'name': 'Ghana', u'flag': u'countryflag/gh'},
    u'gi': {
        u'name': 'Gibraltar',
        u'flag': u'countryflag/gi',
    },
    u'gl': {
        u'name': 'Greenland',
        u'flag': u'countryflag/gl',
    },
    u'gm': {u'name': 'Gambia', u'flag': u'countryflag/gm'},
    u'gn': {u'name': 'Guinea', u'flag': u'countryflag/gn'},
    u'gp': {
        u'name': 'Guadeloupe',
        u'flag': u'countryflag/gp',
    },
    u'gq': {
        u'name': 'Equatorial Guinea',
        u'flag': u'countryflag/gq',
    },
    u'gr': {u'name': 'Greece', u'flag': u'countryflag/gr'},
    u'gs': {
        u'name': 'South Georgia and the South Sandwich Islands',
        u'flag': u'countryflag/gs',
    },
    u'gt': {
        u'name': 'Guatemala',
        u'flag': u'countryflag/gt',
    },
    u'gu': {u'name': 'Guam', u'flag': u'countryflag/gu'},
    u'gw': {
        u'name': 'Guinea-Bissau',
        u'flag': u'countryflag/gw',
    },
    u'gy': {u'name': 'Guyana', u'flag': u'countryflag/gy'},
    u'hk': {
        u'name': 'Hong Kong',
        u'flag': u'countryflag/hk',
    },
    u'hm': {
        u'name': 'Heard Island and McDonald Islands',
        u'flag': u'countryflag/hm',
    },
    u'hn': {
        u'name': 'Honduras',
        u'flag': u'countryflag/hn',
    },
    u'hr': {u'name': 'Croatia', u'flag': u'countryflag/hr'},
    u'ht': {u'name': 'Haiti', u'flag': u'countryflag/ht'},
    u'hu': {u'name': 'Hungary', u'flag': u'countryflag/hu'},
    u'id': {
        u'name': 'Indonesia',
        u'flag': u'countryflag/id',
    },
    u'ie': {u'name': 'Ireland', u'flag': u'countryflag/ie'},
    u'il': {u'name': 'Israel', u'flag': u'countryflag/il'},
    u'im': {
        u'name': 'Isle of Man',
        u'flag': u'countryflag/im',
    },
    u'in': {u'name': 'India', u'flag': u'countryflag/in'},
    u'io': {
        u'name': 'British Indian Ocean Territory',
        u'flag': u'countryflag/io',
    },
    u'iq': {u'name': 'Iraq', u'flag': u'countryflag/iq'},
    u'ir': {
        u'name': 'Iran Islamic Republic of',
        u'flag': u'countryflag/ir',
    },
    u'is': {u'name': 'Iceland', u'flag': u'countryflag/is'},
    u'it': {u'name': 'Italy', u'flag': u'countryflag/it'},
    u'je': {u'name': 'Jersey', u'flag': u'countryflag/je'},
    u'jm': {u'name': 'Jamaica', u'flag': u'countryflag/jm'},
    u'jo': {u'name': 'Jordan', u'flag': u'countryflag/jo'},
    u'jp': {u'name': 'Japan', u'flag': u'countryflag/jp'},
    u'ke': {u'name': 'Kenya', u'flag': u'countryflag/ke'},
    u'kg': {
        u'name': 'Kyrgyzstan',
        u'flag': u'countryflag/kg',
    },
    u'kh': {
        u'name': 'Cambodia',
        u'flag': u'countryflag/kh',
    },
    u'ki': {
        u'name': 'Kiribati',
        u'flag': u'countryflag/ki',
    },
    u'km': {u'name': 'Comoros', u'flag': u'countryflag/km'},
    u'kn': {
        u'name': 'Saint Kitts and Nevis',
        u'flag': u'countryflag/kn',
    },
    u'kp': {
        u'name': "Korea Democratic People's Republic of",
        u'flag': u'countryflag/kp',
    },
    u'kr': {
        u'name': 'Korea Republic of',
        u'flag': u'countryflag/kr',
    },
    u'kw': {u'name': 'Kuwait', u'flag': u'countryflag/kw'},
    u'ky': {
        u'name': 'Cayman Islands',
        u'flag': u'countryflag/ky',
    },
    u'kz': {
        u'name': 'Kazakhstan',
        u'flag': u'countryflag/kz',
    },
    u'la': {
        u'name': "Lao People's Democratic Republic",
        u'flag': u'countryflag/la',
    },
    u'lb': {u'name': 'Lebanon', u'flag': u'countryflag/lb'},
    u'lc': {
        u'name': 'Saint Lucia',
        u'flag': u'countryflag/lc',
    },
    u'li': {
        u'name': 'Liechtenstein',
        u'flag': u'countryflag/li',
    },
    u'lk': {
        u'name': 'Sri Lanka',
        u'flag': u'countryflag/lk',
    },
    u'lr': {u'name': 'Liberia', u'flag': u'countryflag/lr'},
    u'ls': {u'name': 'Lesotho', u'flag': u'countryflag/ls'},
    u'lt': {
        u'name': 'Lithuania',
        u'flag': u'countryflag/lt',
    },
    u'lu': {
        u'name': 'Luxembourg',
        u'flag': u'countryflag/lu',
    },
    u'lv': {u'name': 'Latvia', u'flag': u'countryflag/lv'},
    u'ly': {
        u'name': 'Libyan Arab Jamahiriya',
        u'flag': u'countryflag/ly',
    },
    u'ma': {u'name': 'Morocco', u'flag': u'countryflag/ma'},
    u'mc': {u'name': 'Monaco', u'flag': u'countryflag/mc'},
    u'md': {
        u'name': 'Moldova Republic of',
        u'flag': u'countryflag/md',
    },
    u'me': {
        u'name': 'Montenegro',
        u'flag': u'countryflag/me',
    },
    u'mf': {
        u'name': 'Saint Martin (French part)',
        u'flag': u'countryflag/mf.png',
    },
    u'mg': {
        u'name': 'Madagascar',
        u'flag': u'countryflag/mg',
    },
    u'mh': {
        u'name': 'Marshall Islands',
        u'flag': u'countryflag/mh',
    },
    u'mk': {
        u'name': 'Macedonia the former Yugoslavian Republic of',
        u'flag': u'countryflag/mk',
    },
    u'ml': {u'name': 'Mali', u'flag': u'countryflag/ml'},
    u'mm': {u'name': 'Myanmar', u'flag': u'countryflag/mm'},
    u'mn': {
        u'name': 'Mongolia',
        u'flag': u'countryflag/mn',
    },
    u'mo': {u'name': 'Macao', u'flag': u'countryflag/mo'},
    u'mp': {
        u'name': 'Northern Mariana Islands',
        u'flag': u'countryflag/mp',
    },
    u'mq': {
        u'name': 'Martinique',
        u'flag': u'countryflag/mq',
    },
    u'mr': {
        u'name': 'Mauritania',
        u'flag': u'countryflag/mr',
    },
    u'ms': {
        u'name': 'Montserrat',
        u'flag': u'countryflag/ms',
    },
    u'mt': {u'name': 'Malta', u'flag': u'countryflag/mt'},
    u'mu': {
        u'name': 'Mauritius',
        u'flag': u'countryflag/mu',
    },
    u'mv': {
        u'name': 'Maldives',
        u'flag': u'countryflag/mv',
    },
    u'mw': {u'name': 'Malawi', u'flag': u'countryflag/mw'},
    u'mx': {u'name': 'Mexico', u'flag': u'countryflag/mx'},
    u'my': {
        u'name': 'Malaysia',
        u'flag': u'countryflag/my',
    },
    u'mz': {
        u'name': 'Mozambique',
        u'flag': u'countryflag/mz',
    },
    u'na': {u'name': 'Namibia', u'flag': u'countryflag/na'},
    u'nc': {
        u'name': 'New Caledonia',
        u'flag': u'countryflag/nc',
    },
    u'ne': {u'name': 'Niger', u'flag': u'countryflag/ne'},
    u'nf': {
        u'name': 'Norfolk Island',
        u'flag': u'countryflag/nf',
    },
    u'ng': {u'name': 'Nigeria', u'flag': u'countryflag/ng'},
    u'ni': {
        u'name': 'Nicaragua',
        u'flag': u'countryflag/ni',
    },
    u'nl': {
        u'name': 'Netherlands',
        u'flag': u'countryflag/nl',
    },
    u'no': {u'name': 'Norway', u'flag': u'countryflag/no'},
    u'np': {u'name': 'Nepal', u'flag': u'countryflag/np'},
    u'nr': {u'name': 'Nauru', u'flag': u'countryflag/nr'},
    u'nu': {u'name': 'Niue', u'flag': u'countryflag/nu'},
    u'nz': {
        u'name': 'New Zealand',
        u'flag': u'countryflag/nz',
    },
    u'om': {u'name': 'Oman', u'flag': u'countryflag/om'},
    u'pa': {u'name': 'Panama', u'flag': u'countryflag/pa'},
    u'pe': {u'name': 'Peru', u'flag': u'countryflag/pe'},
    u'pf': {
        u'name': 'French Polynesia',
        u'flag': u'countryflag/pf',
    },
    u'pg': {
        u'name': 'Papua New Guinea',
        u'flag': u'countryflag/pg',
    },
    u'ph': {
        u'name': 'Philippines',
        u'flag': u'countryflag/ph',
    },
    u'pk': {
        u'name': 'Pakistan',
        u'flag': u'countryflag/pk',
    },
    u'pl': {u'name': 'Poland', u'flag': u'countryflag/pl'},
    u'pm': {
        u'name': 'Saint Pierre and Miquelon',
        u'flag': u'countryflag/pm',
    },
    u'pn': {
        u'name': 'Pitcairn',
        u'flag': u'countryflag/pn',
    },
    u'pr': {
        u'name': 'Puerto Rico',
        u'flag': u'countryflag/pr',
    },
    u'ps': {
        u'name': 'Palestinian Territory occupied',
        u'flag': u'countryflag/ps',
    },
    u'pt': {
        u'name': 'Portugal',
        u'flag': u'countryflag/pt',
    },
    u'pw': {u'name': 'Palau', u'flag': u'countryflag/pw'},
    u'py': {
        u'name': 'Paraguay',
        u'flag': u'countryflag/py',
    },
    u'qa': {u'name': 'Qatar', u'flag': u'countryflag/qa'},
    u're': {u'name': 'Reunion', u'flag': u'countryflag/re'},
    u'ro': {u'name': 'Romania', u'flag': u'countryflag/ro'},
    u'rs': {u'name': 'Serbia', u'flag': u'countryflag/rs'},
    u'ru': {
        u'name': 'Russian Federation',
        u'flag': u'countryflag/ru',
    },
    u'rw': {u'name': 'Rwanda', u'flag': u'countryflag/rw'},
    u'sa': {
        u'name': 'Saudi Arabia',
        u'flag': u'countryflag/sa',
    },
    u'sb': {
        u'name': 'Solomon Islands',
        u'flag': u'countryflag/sb',
    },
    u'sc': {
        u'name': 'Seychelles',
        u'flag': u'countryflag/sc',
    },
    u'sd': {u'name': 'Sudan', u'flag': u'countryflag/sd'},
    u'se': {u'name': 'Sweden', u'flag': u'countryflag/se'},
    u'sg': {
        u'name': 'Singapore',
        u'flag': u'countryflag/sg',
    },
    u'sh': {
        u'name': 'Saint Helena',
        u'flag': u'countryflag/sh',
    },
    u'si': {
        u'name': 'Slovenia',
        u'flag': u'countryflag/si',
    },
    u'sj': {
        u'name': 'Svalbard and Jan Mayen',
        u'flag': u'countryflag/sj',
    },
    u'sk': {
        u'name': 'Slovakia',
        u'flag': u'countryflag/sk',
    },
    u'sl': {
        u'name': 'Sierra Leone',
        u'flag': u'countryflag/sl',
    },
    u'sm': {
        u'name': 'San Marino',
        u'flag': u'countryflag/sm',
    },
    u'sn': {u'name': 'Senegal', u'flag': u'countryflag/sn'},
    u'so': {u'name': 'Somalia', u'flag': u'countryflag/so'},
    u'sr': {
        u'name': 'Suriname',
        u'flag': u'countryflag/sr',
    },
    u'ss': {
        u'name': 'South Sudan',
        u'flag': u'countryflag/ss.png',
    },
    u'st': {
        u'name': 'Sao Tome and Principe',
        u'flag': u'countryflag/st',
    },
    u'sv': {
        u'name': 'El Salvador',
        u'flag': u'countryflag/sv',
    },
    u'sx': {
        u'name': 'Sint Maarten (Dutch part)',
        u'flag': u'countryflag/sx.png',
    },
    u'sy': {
        u'name': 'Syrian Arab Republic',
        u'flag': u'countryflag/sy',
    },
    u'sz': {
        u'name': 'Swaziland',
        u'flag': u'countryflag/sz',
    },
    u'tc': {
        u'name': 'Turks and Caicos Islands',
        u'flag': u'countryflag/tc',
    },
    u'td': {u'name': 'Chad', u'flag': u'countryflag/td'},
    u'tf': {
        u'name': 'French Southern Territories',
        u'flag': u'countryflag/tf',
    },
    u'tg': {u'name': 'Togo', u'flag': u'countryflag/tg'},
    u'th': {
        u'name': 'Thailand',
        u'flag': u'countryflag/th',
    },
    u'tj': {
        u'name': 'Tajikistan',
        u'flag': u'countryflag/tj',
    },
    u'tk': {u'name': 'Tokelau', u'flag': u'countryflag/tk'},
    u'tl': {
        u'name': 'Timor-Leste',
        u'flag': u'countryflag/tl',
    },
    u'tm': {
        u'name': 'Turkmenistan',
        u'flag': u'countryflag/tm',
    },
    u'tn': {u'name': 'Tunisia', u'flag': u'countryflag/tn'},
    u'to': {u'name': 'Tonga', u'flag': u'countryflag/to'},
    u'tr': {u'name': 'Turkey', u'flag': u'countryflag/tr'},
    u'tt': {
        u'name': 'Trinidad and Tobago',
        u'flag': u'countryflag/tt',
    },
    u'tv': {u'name': 'Tuvalu', u'flag': u'countryflag/tv'},
    u'tw': {u'name': 'Taiwan', u'flag': u'countryflag/tw'},
    u'tz': {
        u'name': 'Tanzania United Republic of',
        u'flag': u'countryflag/tz',
    },
    u'ua': {u'name': 'Ukraine', u'flag': u'countryflag/ua'},
    u'ug': {u'name': 'Uganda', u'flag': u'countryflag/ug'},
    u'um': {
        u'name': 'United States Minor Outlying Islands',
        u'flag': u'countryflag/um',
    },
    u'us': {
        u'name': 'United States',
        u'flag': u'countryflag/us',
    },
    u'uy': {u'name': 'Uruguay', u'flag': u'countryflag/uy'},
    u'uz': {
        u'name': 'Uzbekistan',
        u'flag': u'countryflag/uz',
    },
    u'va': {
        u'name': 'Holy See (Vatican City State)',
        u'flag': u'countryflag/va',
    },
    u'vc': {
        u'name': 'Saint Vincent and the Grenadines',
        u'flag': u'countryflag/vc',
    },
    u've': {
        u'name': 'Venezuela',
        u'flag': u'countryflag/ve',
    },
    u'vg': {
        u'name': 'Virgin Islands British',
        u'flag': u'countryflag/vg',
    },
    u'vi': {
        u'name': 'Virgin Islands U.S.',
        u'flag': u'countryflag/vi',
    },
    u'vn': {
        u'name': 'Viet Nam',
        u'flag': u'countryflag/vn',
    },
    u'vu': {u'name': 'Vanuatu', u'flag': u'countryflag/vu'},
    u'wf': {
        u'name': 'Wallis and Futuna',
        u'flag': u'countryflag/wf',
    },
    u'ws': {u'name': 'Samoa', u'flag': u'countryflag/ws'},
    u'ye': {u'name': 'Yemen', u'flag': u'countryflag/ye'},
    u'yt': {u'name': 'Mayotte', u'flag': u'countryflag/yt'},
    u'za': {
        u'name': 'South Africa',
        u'flag': u'countryflag/za',
    },
    u'zm': {u'name': 'Zambia', u'flag': u'countryflag/zm'},
    u'zw': {
        u'name': 'Zimbabwe',
        u'flag': u'countryflag/zw',
    },
    u'xk': {u'name': 'Kosovo', u'flag': u'countryflag/xk'},
}

# convert the utf-8 encoded values to unicode
for code in _countrylist:
    value = _countrylist[code]
    if u'name' in value:
        if six.PY3:
            value[u'name'] = value[u'name']
        else:
            value[u'name'] = unicode(value[u'name'], 'utf-8')
