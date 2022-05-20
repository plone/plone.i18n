from .interfaces import ICountryAvailability
from zope.interface import implementer


@implementer(ICountryAvailability)
class CountryAvailability:
    """A list of available coutries."""

    def getAvailableCountries(self):
        """Return a sequence of country tags for available countries."""
        return list(_countrylist.keys())

    def getCountries(self):
        """Return a sequence of Country objects for available countries."""
        return _countrylist.copy()

    def getCountryListing(self):
        """Return a sequence of country code and country name tuples."""
        return [(code, _countrylist[code]["name"]) for code in _countrylist]


countries = CountryAvailability()

# This is a dictionary of dictonaries:
#
# 'country-code' : {
#     u'name' : 'English name',
#     u'flag' : u'countryflag/*.gif',
# }
#
# This list follows ISO 3166-1. In addition the following reservations are
# part of the list for historical reasons: an

_countrylist = {
    "ad": {"name": "Andorra", "flag": "countryflag/ad"},
    "ae": {
        "name": "United Arab Emirates",
        "flag": "countryflag/ae",
    },
    "af": {
        "name": "Afghanistan",
        "flag": "countryflag/af",
    },
    "ag": {
        "name": "Antigua and Barbuda",
        "flag": "countryflag/ag",
    },
    "ai": {
        "name": "Anguilla",
        "flag": "countryflag/ai",
    },
    "al": {"name": "Albania", "flag": "countryflag/al"},
    "am": {"name": "Armenia", "flag": "countryflag/am"},
    "an": {
        "name": "Netherlands Antilles",
        "flag": "countryflag/an",
    },
    "ao": {"name": "Angola", "flag": "countryflag/ao"},
    "aq": {
        "name": "Antarctica",
        "flag": "countryflag/aq",
    },
    "ar": {
        "name": "Argentina",
        "flag": "countryflag/ar",
    },
    "as": {
        "name": "American Samoa",
        "flag": "countryflag/as",
    },
    "at": {"name": "Austria", "flag": "countryflag/at"},
    "au": {
        "name": "Australia",
        "flag": "countryflag/au",
    },
    "aw": {"name": "Aruba", "flag": "countryflag/aw"},
    "ax": {
        "name": "Oland Islands",
        "flag": "countryflag/ax",
    },
    "az": {
        "name": "Azerbaijan",
        "flag": "countryflag/az",
    },
    "ba": {
        "name": "Bosnia and Herzegovina",
        "flag": "countryflag/ba",
    },
    "bb": {
        "name": "Barbados",
        "flag": "countryflag/bb",
    },
    "bd": {
        "name": "Bangladesh",
        "flag": "countryflag/bd",
    },
    "be": {"name": "Belgium", "flag": "countryflag/be"},
    "bf": {
        "name": "Burkina Faso",
        "flag": "countryflag/bf",
    },
    "bg": {
        "name": "Bulgaria",
        "flag": "countryflag/bg",
    },
    "bh": {"name": "Bahrain", "flag": "countryflag/bh"},
    "bi": {"name": "Burundi", "flag": "countryflag/bi"},
    "bj": {"name": "Benin", "flag": "countryflag/bj"},
    "bl": {
        "name": "Saint Barthélemy",
        "flag": "countryflag/bl",
    },
    "bm": {"name": "Bermuda", "flag": "countryflag/bm"},
    "bn": {
        "name": "Brunei Darussalam",
        "flag": "countryflag/bn",
    },
    "bo": {"name": "Bolivia", "flag": "countryflag/bo"},
    "bq": {
        "name": "Bonaire, Sint Eustatius and Saba",
        "flag": "countryflag/bq",
    },
    "br": {"name": "Brazil", "flag": "countryflag/br"},
    "bs": {"name": "Bahamas", "flag": "countryflag/bs"},
    "bt": {"name": "Bhutan", "flag": "countryflag/bt"},
    "bv": {
        "name": "Bouvet Island",
        "flag": "countryflag/bv",
    },
    "bw": {
        "name": "Botswana",
        "flag": "countryflag/bw",
    },
    "by": {"name": "Belarus", "flag": "countryflag/by"},
    "bz": {"name": "Belize", "flag": "countryflag/bz"},
    "ca": {"name": "Canada", "flag": "countryflag/ca"},
    "cc": {
        "name": "Cocos (Keeling) Islands",
        "flag": "countryflag/cc",
    },
    "cd": {
        "name": "Congo The Democratic Republic of",
        "flag": "countryflag/cd",
    },
    "cf": {
        "name": "Central African Republic",
        "flag": "countryflag/cf",
    },
    "cg": {"name": "Congo", "flag": "countryflag/cg"},
    "ch": {
        "name": "Switzerland",
        "flag": "countryflag/ch",
    },
    "ci": {
        "name": "Cote d'Ivoire",
        "flag": "countryflag/ci",
    },
    "ck": {
        "name": "Cook Islands",
        "flag": "countryflag/ck",
    },
    "cl": {"name": "Chile", "flag": "countryflag/cl"},
    "cm": {
        "name": "Cameroon",
        "flag": "countryflag/cm",
    },
    "cn": {"name": "China", "flag": "countryflag/cn"},
    "co": {
        "name": "Colombia",
        "flag": "countryflag/co",
    },
    "cr": {
        "name": "Costa Rica",
        "flag": "countryflag/cr",
    },
    "cs": {
        "name": "Serbia and Montenegro",
        "flag": "countryflag/cs",
    },
    "cu": {"name": "Cuba", "flag": "countryflag/cu"},
    "cv": {
        "name": "Cape Verde",
        "flag": "countryflag/cv",
    },
    "cw": {"name": "Curaçao", "flag": "countryflag/cw.png"},
    "cx": {
        "name": "Christmas Island",
        "flag": "countryflag/cx",
    },
    "cy": {"name": "Cyprus", "flag": "countryflag/cy"},
    "cz": {
        "name": "Czech Republic",
        "flag": "countryflag/cz",
    },
    "de": {"name": "Germany", "flag": "countryflag/de"},
    "dj": {
        "name": "Djibouti",
        "flag": "countryflag/dj",
    },
    "dk": {"name": "Denmark", "flag": "countryflag/dk"},
    "dm": {
        "name": "Dominica",
        "flag": "countryflag/dm",
    },
    "do": {
        "name": "Dominican Republic",
        "flag": "countryflag/do",
    },
    "dz": {"name": "Algeria", "flag": "countryflag/dz"},
    "ec": {"name": "Ecuador", "flag": "countryflag/ec"},
    "ee": {"name": "Estonia", "flag": "countryflag/ee"},
    "eg": {"name": "Egypt", "flag": "countryflag/eg"},
    "eh": {
        "name": "Western Sahara",
        "flag": "countryflag/eh",
    },
    "er": {"name": "Eritrea", "flag": "countryflag/er"},
    "es": {"name": "Spain", "flag": "countryflag/es"},
    "et": {
        "name": "Ethiopia",
        "flag": "countryflag/et",
    },
    "fi": {"name": "Finland", "flag": "countryflag/fi"},
    "fj": {"name": "Fiji", "flag": "countryflag/fj"},
    "fk": {
        "name": "Falkland Islands (Malvinas)",
        "flag": "countryflag/fk",
    },
    "fm": {
        "name": "Micronesia Federated States of",
        "flag": "countryflag/fm",
    },
    "fo": {
        "name": "Faroe Islands",
        "flag": "countryflag/fo",
    },
    "fr": {"name": "France", "flag": "countryflag/fr"},
    "ga": {"name": "Gabon", "flag": "countryflag/ga"},
    "gb": {
        "name": "United Kingdom",
        "flag": "countryflag/gb",
    },
    "gd": {"name": "Grenada", "flag": "countryflag/gd"},
    "ge": {"name": "Georgia", "flag": "countryflag/ge"},
    "gf": {
        "name": "French Guiana",
        "flag": "countryflag/gf",
    },
    "gg": {
        "name": "Guernsey",
        "flag": "countryflag/gg",
    },
    "gh": {"name": "Ghana", "flag": "countryflag/gh"},
    "gi": {
        "name": "Gibraltar",
        "flag": "countryflag/gi",
    },
    "gl": {
        "name": "Greenland",
        "flag": "countryflag/gl",
    },
    "gm": {"name": "Gambia", "flag": "countryflag/gm"},
    "gn": {"name": "Guinea", "flag": "countryflag/gn"},
    "gp": {
        "name": "Guadeloupe",
        "flag": "countryflag/gp",
    },
    "gq": {
        "name": "Equatorial Guinea",
        "flag": "countryflag/gq",
    },
    "gr": {"name": "Greece", "flag": "countryflag/gr"},
    "gs": {
        "name": "South Georgia and the South Sandwich Islands",
        "flag": "countryflag/gs",
    },
    "gt": {
        "name": "Guatemala",
        "flag": "countryflag/gt",
    },
    "gu": {"name": "Guam", "flag": "countryflag/gu"},
    "gw": {
        "name": "Guinea-Bissau",
        "flag": "countryflag/gw",
    },
    "gy": {"name": "Guyana", "flag": "countryflag/gy"},
    "hk": {
        "name": "Hong Kong",
        "flag": "countryflag/hk",
    },
    "hm": {
        "name": "Heard Island and McDonald Islands",
        "flag": "countryflag/hm",
    },
    "hn": {
        "name": "Honduras",
        "flag": "countryflag/hn",
    },
    "hr": {"name": "Croatia", "flag": "countryflag/hr"},
    "ht": {"name": "Haiti", "flag": "countryflag/ht"},
    "hu": {"name": "Hungary", "flag": "countryflag/hu"},
    "id": {
        "name": "Indonesia",
        "flag": "countryflag/id",
    },
    "ie": {"name": "Ireland", "flag": "countryflag/ie"},
    "il": {"name": "Israel", "flag": "countryflag/il"},
    "im": {
        "name": "Isle of Man",
        "flag": "countryflag/im",
    },
    "in": {"name": "India", "flag": "countryflag/in"},
    "io": {
        "name": "British Indian Ocean Territory",
        "flag": "countryflag/io",
    },
    "iq": {"name": "Iraq", "flag": "countryflag/iq"},
    "ir": {
        "name": "Iran Islamic Republic of",
        "flag": "countryflag/ir",
    },
    "is": {"name": "Iceland", "flag": "countryflag/is"},
    "it": {"name": "Italy", "flag": "countryflag/it"},
    "je": {"name": "Jersey", "flag": "countryflag/je"},
    "jm": {"name": "Jamaica", "flag": "countryflag/jm"},
    "jo": {"name": "Jordan", "flag": "countryflag/jo"},
    "jp": {"name": "Japan", "flag": "countryflag/jp"},
    "ke": {"name": "Kenya", "flag": "countryflag/ke"},
    "kg": {
        "name": "Kyrgyzstan",
        "flag": "countryflag/kg",
    },
    "kh": {
        "name": "Cambodia",
        "flag": "countryflag/kh",
    },
    "ki": {
        "name": "Kiribati",
        "flag": "countryflag/ki",
    },
    "km": {"name": "Comoros", "flag": "countryflag/km"},
    "kn": {
        "name": "Saint Kitts and Nevis",
        "flag": "countryflag/kn",
    },
    "kp": {
        "name": "Korea Democratic People's Republic of",
        "flag": "countryflag/kp",
    },
    "kr": {
        "name": "Korea Republic of",
        "flag": "countryflag/kr",
    },
    "kw": {"name": "Kuwait", "flag": "countryflag/kw"},
    "ky": {
        "name": "Cayman Islands",
        "flag": "countryflag/ky",
    },
    "kz": {
        "name": "Kazakhstan",
        "flag": "countryflag/kz",
    },
    "la": {
        "name": "Lao People's Democratic Republic",
        "flag": "countryflag/la",
    },
    "lb": {"name": "Lebanon", "flag": "countryflag/lb"},
    "lc": {
        "name": "Saint Lucia",
        "flag": "countryflag/lc",
    },
    "li": {
        "name": "Liechtenstein",
        "flag": "countryflag/li",
    },
    "lk": {
        "name": "Sri Lanka",
        "flag": "countryflag/lk",
    },
    "lr": {"name": "Liberia", "flag": "countryflag/lr"},
    "ls": {"name": "Lesotho", "flag": "countryflag/ls"},
    "lt": {
        "name": "Lithuania",
        "flag": "countryflag/lt",
    },
    "lu": {
        "name": "Luxembourg",
        "flag": "countryflag/lu",
    },
    "lv": {"name": "Latvia", "flag": "countryflag/lv"},
    "ly": {
        "name": "Libyan Arab Jamahiriya",
        "flag": "countryflag/ly",
    },
    "ma": {"name": "Morocco", "flag": "countryflag/ma"},
    "mc": {"name": "Monaco", "flag": "countryflag/mc"},
    "md": {
        "name": "Moldova Republic of",
        "flag": "countryflag/md",
    },
    "me": {
        "name": "Montenegro",
        "flag": "countryflag/me",
    },
    "mf": {
        "name": "Saint Martin (French part)",
        "flag": "countryflag/mf.png",
    },
    "mg": {
        "name": "Madagascar",
        "flag": "countryflag/mg",
    },
    "mh": {
        "name": "Marshall Islands",
        "flag": "countryflag/mh",
    },
    "mk": {
        "name": "Macedonia the former Yugoslavian Republic of",
        "flag": "countryflag/mk",
    },
    "ml": {"name": "Mali", "flag": "countryflag/ml"},
    "mm": {"name": "Myanmar", "flag": "countryflag/mm"},
    "mn": {
        "name": "Mongolia",
        "flag": "countryflag/mn",
    },
    "mo": {"name": "Macao", "flag": "countryflag/mo"},
    "mp": {
        "name": "Northern Mariana Islands",
        "flag": "countryflag/mp",
    },
    "mq": {
        "name": "Martinique",
        "flag": "countryflag/mq",
    },
    "mr": {
        "name": "Mauritania",
        "flag": "countryflag/mr",
    },
    "ms": {
        "name": "Montserrat",
        "flag": "countryflag/ms",
    },
    "mt": {"name": "Malta", "flag": "countryflag/mt"},
    "mu": {
        "name": "Mauritius",
        "flag": "countryflag/mu",
    },
    "mv": {
        "name": "Maldives",
        "flag": "countryflag/mv",
    },
    "mw": {"name": "Malawi", "flag": "countryflag/mw"},
    "mx": {"name": "Mexico", "flag": "countryflag/mx"},
    "my": {
        "name": "Malaysia",
        "flag": "countryflag/my",
    },
    "mz": {
        "name": "Mozambique",
        "flag": "countryflag/mz",
    },
    "na": {"name": "Namibia", "flag": "countryflag/na"},
    "nc": {
        "name": "New Caledonia",
        "flag": "countryflag/nc",
    },
    "ne": {"name": "Niger", "flag": "countryflag/ne"},
    "nf": {
        "name": "Norfolk Island",
        "flag": "countryflag/nf",
    },
    "ng": {"name": "Nigeria", "flag": "countryflag/ng"},
    "ni": {
        "name": "Nicaragua",
        "flag": "countryflag/ni",
    },
    "nl": {
        "name": "Netherlands",
        "flag": "countryflag/nl",
    },
    "no": {"name": "Norway", "flag": "countryflag/no"},
    "np": {"name": "Nepal", "flag": "countryflag/np"},
    "nr": {"name": "Nauru", "flag": "countryflag/nr"},
    "nu": {"name": "Niue", "flag": "countryflag/nu"},
    "nz": {
        "name": "New Zealand",
        "flag": "countryflag/nz",
    },
    "om": {"name": "Oman", "flag": "countryflag/om"},
    "pa": {"name": "Panama", "flag": "countryflag/pa"},
    "pe": {"name": "Peru", "flag": "countryflag/pe"},
    "pf": {
        "name": "French Polynesia",
        "flag": "countryflag/pf",
    },
    "pg": {
        "name": "Papua New Guinea",
        "flag": "countryflag/pg",
    },
    "ph": {
        "name": "Philippines",
        "flag": "countryflag/ph",
    },
    "pk": {
        "name": "Pakistan",
        "flag": "countryflag/pk",
    },
    "pl": {"name": "Poland", "flag": "countryflag/pl"},
    "pm": {
        "name": "Saint Pierre and Miquelon",
        "flag": "countryflag/pm",
    },
    "pn": {
        "name": "Pitcairn",
        "flag": "countryflag/pn",
    },
    "pr": {
        "name": "Puerto Rico",
        "flag": "countryflag/pr",
    },
    "ps": {
        "name": "Palestinian Territory occupied",
        "flag": "countryflag/ps",
    },
    "pt": {
        "name": "Portugal",
        "flag": "countryflag/pt",
    },
    "pw": {"name": "Palau", "flag": "countryflag/pw"},
    "py": {
        "name": "Paraguay",
        "flag": "countryflag/py",
    },
    "qa": {"name": "Qatar", "flag": "countryflag/qa"},
    "re": {"name": "Reunion", "flag": "countryflag/re"},
    "ro": {"name": "Romania", "flag": "countryflag/ro"},
    "rs": {"name": "Serbia", "flag": "countryflag/rs"},
    "ru": {
        "name": "Russian Federation",
        "flag": "countryflag/ru",
    },
    "rw": {"name": "Rwanda", "flag": "countryflag/rw"},
    "sa": {
        "name": "Saudi Arabia",
        "flag": "countryflag/sa",
    },
    "sb": {
        "name": "Solomon Islands",
        "flag": "countryflag/sb",
    },
    "sc": {
        "name": "Seychelles",
        "flag": "countryflag/sc",
    },
    "sd": {"name": "Sudan", "flag": "countryflag/sd"},
    "se": {"name": "Sweden", "flag": "countryflag/se"},
    "sg": {
        "name": "Singapore",
        "flag": "countryflag/sg",
    },
    "sh": {
        "name": "Saint Helena",
        "flag": "countryflag/sh",
    },
    "si": {
        "name": "Slovenia",
        "flag": "countryflag/si",
    },
    "sj": {
        "name": "Svalbard and Jan Mayen",
        "flag": "countryflag/sj",
    },
    "sk": {
        "name": "Slovakia",
        "flag": "countryflag/sk",
    },
    "sl": {
        "name": "Sierra Leone",
        "flag": "countryflag/sl",
    },
    "sm": {
        "name": "San Marino",
        "flag": "countryflag/sm",
    },
    "sn": {"name": "Senegal", "flag": "countryflag/sn"},
    "so": {"name": "Somalia", "flag": "countryflag/so"},
    "sr": {
        "name": "Suriname",
        "flag": "countryflag/sr",
    },
    "ss": {
        "name": "South Sudan",
        "flag": "countryflag/ss.png",
    },
    "st": {
        "name": "Sao Tome and Principe",
        "flag": "countryflag/st",
    },
    "sv": {
        "name": "El Salvador",
        "flag": "countryflag/sv",
    },
    "sx": {
        "name": "Sint Maarten (Dutch part)",
        "flag": "countryflag/sx.png",
    },
    "sy": {
        "name": "Syrian Arab Republic",
        "flag": "countryflag/sy",
    },
    "sz": {
        "name": "Swaziland",
        "flag": "countryflag/sz",
    },
    "tc": {
        "name": "Turks and Caicos Islands",
        "flag": "countryflag/tc",
    },
    "td": {"name": "Chad", "flag": "countryflag/td"},
    "tf": {
        "name": "French Southern Territories",
        "flag": "countryflag/tf",
    },
    "tg": {"name": "Togo", "flag": "countryflag/tg"},
    "th": {
        "name": "Thailand",
        "flag": "countryflag/th",
    },
    "tj": {
        "name": "Tajikistan",
        "flag": "countryflag/tj",
    },
    "tk": {"name": "Tokelau", "flag": "countryflag/tk"},
    "tl": {
        "name": "Timor-Leste",
        "flag": "countryflag/tl",
    },
    "tm": {
        "name": "Turkmenistan",
        "flag": "countryflag/tm",
    },
    "tn": {"name": "Tunisia", "flag": "countryflag/tn"},
    "to": {"name": "Tonga", "flag": "countryflag/to"},
    "tr": {"name": "Turkey", "flag": "countryflag/tr"},
    "tt": {
        "name": "Trinidad and Tobago",
        "flag": "countryflag/tt",
    },
    "tv": {"name": "Tuvalu", "flag": "countryflag/tv"},
    "tw": {"name": "Taiwan", "flag": "countryflag/tw"},
    "tz": {
        "name": "Tanzania United Republic of",
        "flag": "countryflag/tz",
    },
    "ua": {"name": "Ukraine", "flag": "countryflag/ua"},
    "ug": {"name": "Uganda", "flag": "countryflag/ug"},
    "um": {
        "name": "United States Minor Outlying Islands",
        "flag": "countryflag/um",
    },
    "us": {
        "name": "United States",
        "flag": "countryflag/us",
    },
    "uy": {"name": "Uruguay", "flag": "countryflag/uy"},
    "uz": {
        "name": "Uzbekistan",
        "flag": "countryflag/uz",
    },
    "va": {
        "name": "Holy See (Vatican City State)",
        "flag": "countryflag/va",
    },
    "vc": {
        "name": "Saint Vincent and the Grenadines",
        "flag": "countryflag/vc",
    },
    "ve": {
        "name": "Venezuela",
        "flag": "countryflag/ve",
    },
    "vg": {
        "name": "Virgin Islands British",
        "flag": "countryflag/vg",
    },
    "vi": {
        "name": "Virgin Islands U.S.",
        "flag": "countryflag/vi",
    },
    "vn": {
        "name": "Viet Nam",
        "flag": "countryflag/vn",
    },
    "vu": {"name": "Vanuatu", "flag": "countryflag/vu"},
    "wf": {
        "name": "Wallis and Futuna",
        "flag": "countryflag/wf",
    },
    "ws": {"name": "Samoa", "flag": "countryflag/ws"},
    "ye": {"name": "Yemen", "flag": "countryflag/ye"},
    "yt": {"name": "Mayotte", "flag": "countryflag/yt"},
    "za": {
        "name": "South Africa",
        "flag": "countryflag/za",
    },
    "zm": {"name": "Zambia", "flag": "countryflag/zm"},
    "zw": {
        "name": "Zimbabwe",
        "flag": "countryflag/zw",
    },
    "xk": {"name": "Kosovo", "flag": "countryflag/xk"},
}
