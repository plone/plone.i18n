from plone.i18n.locales.interfaces import ICountryAvailability
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
#     u'flag' : u'/++resource++country-flags/*.gif',
# }
#
# This list follows ISO 3166-1. In addition the following reservations are
# part of the list for historical reasons: an

_countrylist = {
    "ad": {"name": "Andorra", "flag": "/++resource++country-flags/ad.gif"},
    "ae": {
        "name": "United Arab Emirates",
        "flag": "/++resource++country-flags/ae.gif",
    },
    "af": {
        "name": "Afghanistan",
        "flag": "/++resource++country-flags/af.gif",
    },
    "ag": {
        "name": "Antigua and Barbuda",
        "flag": "/++resource++country-flags/ag.gif",
    },
    "ai": {
        "name": "Anguilla",
        "flag": "/++resource++country-flags/ai.gif",
    },
    "al": {"name": "Albania", "flag": "/++resource++country-flags/al.gif"},
    "am": {"name": "Armenia", "flag": "/++resource++country-flags/am.gif"},
    "an": {
        "name": "Netherlands Antilles",
        "flag": "/++resource++country-flags/an.gif",
    },
    "ao": {"name": "Angola", "flag": "/++resource++country-flags/ao.gif"},
    "aq": {
        "name": "Antarctica",
        "flag": "/++resource++country-flags/aq.gif",
    },
    "ar": {
        "name": "Argentina",
        "flag": "/++resource++country-flags/ar.gif",
    },
    "as": {
        "name": "American Samoa",
        "flag": "/++resource++country-flags/as.gif",
    },
    "at": {"name": "Austria", "flag": "/++resource++country-flags/at.gif"},
    "au": {
        "name": "Australia",
        "flag": "/++resource++country-flags/au.gif",
    },
    "aw": {"name": "Aruba", "flag": "/++resource++country-flags/aw.gif"},
    "ax": {
        "name": "Oland Islands",
        "flag": "/++resource++country-flags/ax.gif",
    },
    "az": {
        "name": "Azerbaijan",
        "flag": "/++resource++country-flags/az.gif",
    },
    "ba": {
        "name": "Bosnia and Herzegovina",
        "flag": "/++resource++country-flags/ba.gif",
    },
    "bb": {
        "name": "Barbados",
        "flag": "/++resource++country-flags/bb.gif",
    },
    "bd": {
        "name": "Bangladesh",
        "flag": "/++resource++country-flags/bd.gif",
    },
    "be": {"name": "Belgium", "flag": "/++resource++country-flags/be.gif"},
    "bf": {
        "name": "Burkina Faso",
        "flag": "/++resource++country-flags/bf.gif",
    },
    "bg": {
        "name": "Bulgaria",
        "flag": "/++resource++country-flags/bg.gif",
    },
    "bh": {"name": "Bahrain", "flag": "/++resource++country-flags/bh.gif"},
    "bi": {"name": "Burundi", "flag": "/++resource++country-flags/bi.gif"},
    "bj": {"name": "Benin", "flag": "/++resource++country-flags/bj.gif"},
    "bl": {
        "name": "Saint Barthélemy",
        "flag": "/++resource++country-flags/bl.gif",
    },
    "bm": {"name": "Bermuda", "flag": "/++resource++country-flags/bm.gif"},
    "bn": {
        "name": "Brunei Darussalam",
        "flag": "/++resource++country-flags/bn.gif",
    },
    "bo": {"name": "Bolivia", "flag": "/++resource++country-flags/bo.gif"},
    "bq": {
        "name": "Bonaire, Sint Eustatius and Saba",
        "flag": "/++resource++country-flags/bq.gif",
    },
    "br": {"name": "Brazil", "flag": "/++resource++country-flags/br.gif"},
    "bs": {"name": "Bahamas", "flag": "/++resource++country-flags/bs.gif"},
    "bt": {"name": "Bhutan", "flag": "/++resource++country-flags/bt.gif"},
    "bv": {
        "name": "Bouvet Island",
        "flag": "/++resource++country-flags/bv.gif",
    },
    "bw": {
        "name": "Botswana",
        "flag": "/++resource++country-flags/bw.gif",
    },
    "by": {"name": "Belarus", "flag": "/++resource++country-flags/by.gif"},
    "bz": {"name": "Belize", "flag": "/++resource++country-flags/bz.gif"},
    "ca": {"name": "Canada", "flag": "/++resource++country-flags/ca.gif"},
    "cc": {
        "name": "Cocos (Keeling) Islands",
        "flag": "/++resource++country-flags/cc.gif",
    },
    "cd": {
        "name": "Congo The Democratic Republic of",
        "flag": "/++resource++country-flags/cd.gif",
    },
    "cf": {
        "name": "Central African Republic",
        "flag": "/++resource++country-flags/cf.gif",
    },
    "cg": {"name": "Congo", "flag": "/++resource++country-flags/cg.gif"},
    "ch": {
        "name": "Switzerland",
        "flag": "/++resource++country-flags/ch.gif",
    },
    "ci": {
        "name": "Cote d'Ivoire",
        "flag": "/++resource++country-flags/ci.gif",
    },
    "ck": {
        "name": "Cook Islands",
        "flag": "/++resource++country-flags/ck.gif",
    },
    "cl": {"name": "Chile", "flag": "/++resource++country-flags/cl.gif"},
    "cm": {
        "name": "Cameroon",
        "flag": "/++resource++country-flags/cm.gif",
    },
    "cn": {"name": "China", "flag": "/++resource++country-flags/cn.gif"},
    "co": {
        "name": "Colombia",
        "flag": "/++resource++country-flags/co.gif",
    },
    "cr": {
        "name": "Costa Rica",
        "flag": "/++resource++country-flags/cr.gif",
    },
    "cs": {
        "name": "Serbia and Montenegro",
        "flag": "/++resource++country-flags/cs.gif",
    },
    "cu": {"name": "Cuba", "flag": "/++resource++country-flags/cu.gif"},
    "cv": {
        "name": "Cape Verde",
        "flag": "/++resource++country-flags/cv.gif",
    },
    "cw": {"name": "Curaçao", "flag": "/++resource++country-flags/cw.png"},
    "cx": {
        "name": "Christmas Island",
        "flag": "/++resource++country-flags/cx.gif",
    },
    "cy": {"name": "Cyprus", "flag": "/++resource++country-flags/cy.gif"},
    "cz": {
        "name": "Czech Republic",
        "flag": "/++resource++country-flags/cz.gif",
    },
    "de": {"name": "Germany", "flag": "/++resource++country-flags/de.gif"},
    "dj": {
        "name": "Djibouti",
        "flag": "/++resource++country-flags/dj.gif",
    },
    "dk": {"name": "Denmark", "flag": "/++resource++country-flags/dk.gif"},
    "dm": {
        "name": "Dominica",
        "flag": "/++resource++country-flags/dm.gif",
    },
    "do": {
        "name": "Dominican Republic",
        "flag": "/++resource++country-flags/do.gif",
    },
    "dz": {"name": "Algeria", "flag": "/++resource++country-flags/dz.gif"},
    "ec": {"name": "Ecuador", "flag": "/++resource++country-flags/ec.gif"},
    "ee": {"name": "Estonia", "flag": "/++resource++country-flags/ee.gif"},
    "eg": {"name": "Egypt", "flag": "/++resource++country-flags/eg.gif"},
    "eh": {
        "name": "Western Sahara",
        "flag": "/++resource++country-flags/eh.gif",
    },
    "er": {"name": "Eritrea", "flag": "/++resource++country-flags/er.gif"},
    "es": {"name": "Spain", "flag": "/++resource++country-flags/es.gif"},
    "et": {
        "name": "Ethiopia",
        "flag": "/++resource++country-flags/et.gif",
    },
    "fi": {"name": "Finland", "flag": "/++resource++country-flags/fi.gif"},
    "fj": {"name": "Fiji", "flag": "/++resource++country-flags/fj.gif"},
    "fk": {
        "name": "Falkland Islands (Malvinas)",
        "flag": "/++resource++country-flags/fk.gif",
    },
    "fm": {
        "name": "Micronesia Federated States of",
        "flag": "/++resource++country-flags/fm.gif",
    },
    "fo": {
        "name": "Faroe Islands",
        "flag": "/++resource++country-flags/fo.gif",
    },
    "fr": {"name": "France", "flag": "/++resource++country-flags/fr.gif"},
    "ga": {"name": "Gabon", "flag": "/++resource++country-flags/ga.gif"},
    "gb": {
        "name": "United Kingdom",
        "flag": "/++resource++country-flags/gb.gif",
    },
    "gd": {"name": "Grenada", "flag": "/++resource++country-flags/gd.gif"},
    "ge": {"name": "Georgia", "flag": "/++resource++country-flags/ge.gif"},
    "gf": {
        "name": "French Guiana",
        "flag": "/++resource++country-flags/gf.gif",
    },
    "gg": {
        "name": "Guernsey",
        "flag": "/++resource++country-flags/gg.gif",
    },
    "gh": {"name": "Ghana", "flag": "/++resource++country-flags/gh.gif"},
    "gi": {
        "name": "Gibraltar",
        "flag": "/++resource++country-flags/gi.gif",
    },
    "gl": {
        "name": "Greenland",
        "flag": "/++resource++country-flags/gl.gif",
    },
    "gm": {"name": "Gambia", "flag": "/++resource++country-flags/gm.gif"},
    "gn": {"name": "Guinea", "flag": "/++resource++country-flags/gn.gif"},
    "gp": {
        "name": "Guadeloupe",
        "flag": "/++resource++country-flags/gp.gif",
    },
    "gq": {
        "name": "Equatorial Guinea",
        "flag": "/++resource++country-flags/gq.gif",
    },
    "gr": {"name": "Greece", "flag": "/++resource++country-flags/gr.gif"},
    "gs": {
        "name": "South Georgia and the South Sandwich Islands",
        "flag": "/++resource++country-flags/gs.gif",
    },
    "gt": {
        "name": "Guatemala",
        "flag": "/++resource++country-flags/gt.gif",
    },
    "gu": {"name": "Guam", "flag": "/++resource++country-flags/gu.gif"},
    "gw": {
        "name": "Guinea-Bissau",
        "flag": "/++resource++country-flags/gw.gif",
    },
    "gy": {"name": "Guyana", "flag": "/++resource++country-flags/gy.gif"},
    "hk": {
        "name": "Hong Kong",
        "flag": "/++resource++country-flags/hk.gif",
    },
    "hm": {
        "name": "Heard Island and McDonald Islands",
        "flag": "/++resource++country-flags/hm.gif",
    },
    "hn": {
        "name": "Honduras",
        "flag": "/++resource++country-flags/hn.gif",
    },
    "hr": {"name": "Croatia", "flag": "/++resource++country-flags/hr.gif"},
    "ht": {"name": "Haiti", "flag": "/++resource++country-flags/ht.gif"},
    "hu": {"name": "Hungary", "flag": "/++resource++country-flags/hu.gif"},
    "id": {
        "name": "Indonesia",
        "flag": "/++resource++country-flags/id.gif",
    },
    "ie": {"name": "Ireland", "flag": "/++resource++country-flags/ie.gif"},
    "il": {"name": "Israel", "flag": "/++resource++country-flags/il.gif"},
    "im": {
        "name": "Isle of Man",
        "flag": "/++resource++country-flags/im.gif",
    },
    "in": {"name": "India", "flag": "/++resource++country-flags/in.gif"},
    "io": {
        "name": "British Indian Ocean Territory",
        "flag": "/++resource++country-flags/io.gif",
    },
    "iq": {"name": "Iraq", "flag": "/++resource++country-flags/iq.gif"},
    "ir": {
        "name": "Iran Islamic Republic of",
        "flag": "/++resource++country-flags/ir.gif",
    },
    "is": {"name": "Iceland", "flag": "/++resource++country-flags/is.gif"},
    "it": {"name": "Italy", "flag": "/++resource++country-flags/it.gif"},
    "je": {"name": "Jersey", "flag": "/++resource++country-flags/je.gif"},
    "jm": {"name": "Jamaica", "flag": "/++resource++country-flags/jm.gif"},
    "jo": {"name": "Jordan", "flag": "/++resource++country-flags/jo.gif"},
    "jp": {"name": "Japan", "flag": "/++resource++country-flags/jp.gif"},
    "ke": {"name": "Kenya", "flag": "/++resource++country-flags/ke.gif"},
    "kg": {
        "name": "Kyrgyzstan",
        "flag": "/++resource++country-flags/kg.gif",
    },
    "kh": {
        "name": "Cambodia",
        "flag": "/++resource++country-flags/kh.gif",
    },
    "ki": {
        "name": "Kiribati",
        "flag": "/++resource++country-flags/ki.gif",
    },
    "km": {"name": "Comoros", "flag": "/++resource++country-flags/km.gif"},
    "kn": {
        "name": "Saint Kitts and Nevis",
        "flag": "/++resource++country-flags/kn.gif",
    },
    "kp": {
        "name": "Korea Democratic People's Republic of",
        "flag": "/++resource++country-flags/kp.gif",
    },
    "kr": {
        "name": "Korea Republic of",
        "flag": "/++resource++country-flags/kr.gif",
    },
    "kw": {"name": "Kuwait", "flag": "/++resource++country-flags/kw.gif"},
    "ky": {
        "name": "Cayman Islands",
        "flag": "/++resource++country-flags/ky.gif",
    },
    "kz": {
        "name": "Kazakhstan",
        "flag": "/++resource++country-flags/kz.gif",
    },
    "la": {
        "name": "Lao People's Democratic Republic",
        "flag": "/++resource++country-flags/la.gif",
    },
    "lb": {"name": "Lebanon", "flag": "/++resource++country-flags/lb.gif"},
    "lc": {
        "name": "Saint Lucia",
        "flag": "/++resource++country-flags/lc.gif",
    },
    "li": {
        "name": "Liechtenstein",
        "flag": "/++resource++country-flags/li.gif",
    },
    "lk": {
        "name": "Sri Lanka",
        "flag": "/++resource++country-flags/lk.gif",
    },
    "lr": {"name": "Liberia", "flag": "/++resource++country-flags/lr.gif"},
    "ls": {"name": "Lesotho", "flag": "/++resource++country-flags/ls.gif"},
    "lt": {
        "name": "Lithuania",
        "flag": "/++resource++country-flags/lt.gif",
    },
    "lu": {
        "name": "Luxembourg",
        "flag": "/++resource++country-flags/lu.gif",
    },
    "lv": {"name": "Latvia", "flag": "/++resource++country-flags/lv.gif"},
    "ly": {
        "name": "Libyan Arab Jamahiriya",
        "flag": "/++resource++country-flags/ly.gif",
    },
    "ma": {"name": "Morocco", "flag": "/++resource++country-flags/ma.gif"},
    "mc": {"name": "Monaco", "flag": "/++resource++country-flags/mc.gif"},
    "md": {
        "name": "Moldova Republic of",
        "flag": "/++resource++country-flags/md.gif",
    },
    "me": {
        "name": "Montenegro",
        "flag": "/++resource++country-flags/me.gif",
    },
    "mf": {
        "name": "Saint Martin (French part)",
        "flag": "/++resource++country-flags/mf.png",
    },
    "mg": {
        "name": "Madagascar",
        "flag": "/++resource++country-flags/mg.gif",
    },
    "mh": {
        "name": "Marshall Islands",
        "flag": "/++resource++country-flags/mh.gif",
    },
    "mk": {
        "name": "Macedonia the former Yugoslavian Republic of",
        "flag": "/++resource++country-flags/mk.gif",
    },
    "ml": {"name": "Mali", "flag": "/++resource++country-flags/ml.gif"},
    "mm": {"name": "Myanmar", "flag": "/++resource++country-flags/mm.gif"},
    "mn": {
        "name": "Mongolia",
        "flag": "/++resource++country-flags/mn.gif",
    },
    "mo": {"name": "Macao", "flag": "/++resource++country-flags/mo.gif"},
    "mp": {
        "name": "Northern Mariana Islands",
        "flag": "/++resource++country-flags/mp.gif",
    },
    "mq": {
        "name": "Martinique",
        "flag": "/++resource++country-flags/mq.gif",
    },
    "mr": {
        "name": "Mauritania",
        "flag": "/++resource++country-flags/mr.gif",
    },
    "ms": {
        "name": "Montserrat",
        "flag": "/++resource++country-flags/ms.gif",
    },
    "mt": {"name": "Malta", "flag": "/++resource++country-flags/mt.gif"},
    "mu": {
        "name": "Mauritius",
        "flag": "/++resource++country-flags/mu.gif",
    },
    "mv": {
        "name": "Maldives",
        "flag": "/++resource++country-flags/mv.gif",
    },
    "mw": {"name": "Malawi", "flag": "/++resource++country-flags/mw.gif"},
    "mx": {"name": "Mexico", "flag": "/++resource++country-flags/mx.gif"},
    "my": {
        "name": "Malaysia",
        "flag": "/++resource++country-flags/my.gif",
    },
    "mz": {
        "name": "Mozambique",
        "flag": "/++resource++country-flags/mz.gif",
    },
    "na": {"name": "Namibia", "flag": "/++resource++country-flags/na.gif"},
    "nc": {
        "name": "New Caledonia",
        "flag": "/++resource++country-flags/nc.gif",
    },
    "ne": {"name": "Niger", "flag": "/++resource++country-flags/ne.gif"},
    "nf": {
        "name": "Norfolk Island",
        "flag": "/++resource++country-flags/nf.gif",
    },
    "ng": {"name": "Nigeria", "flag": "/++resource++country-flags/ng.gif"},
    "ni": {
        "name": "Nicaragua",
        "flag": "/++resource++country-flags/ni.gif",
    },
    "nl": {
        "name": "Netherlands",
        "flag": "/++resource++country-flags/nl.gif",
    },
    "no": {"name": "Norway", "flag": "/++resource++country-flags/no.gif"},
    "np": {"name": "Nepal", "flag": "/++resource++country-flags/np.gif"},
    "nr": {"name": "Nauru", "flag": "/++resource++country-flags/nr.gif"},
    "nu": {"name": "Niue", "flag": "/++resource++country-flags/nu.gif"},
    "nz": {
        "name": "New Zealand",
        "flag": "/++resource++country-flags/nz.gif",
    },
    "om": {"name": "Oman", "flag": "/++resource++country-flags/om.gif"},
    "pa": {"name": "Panama", "flag": "/++resource++country-flags/pa.gif"},
    "pe": {"name": "Peru", "flag": "/++resource++country-flags/pe.gif"},
    "pf": {
        "name": "French Polynesia",
        "flag": "/++resource++country-flags/pf.gif",
    },
    "pg": {
        "name": "Papua New Guinea",
        "flag": "/++resource++country-flags/pg.gif",
    },
    "ph": {
        "name": "Philippines",
        "flag": "/++resource++country-flags/ph.gif",
    },
    "pk": {
        "name": "Pakistan",
        "flag": "/++resource++country-flags/pk.gif",
    },
    "pl": {"name": "Poland", "flag": "/++resource++country-flags/pl.gif"},
    "pm": {
        "name": "Saint Pierre and Miquelon",
        "flag": "/++resource++country-flags/pm.gif",
    },
    "pn": {
        "name": "Pitcairn",
        "flag": "/++resource++country-flags/pn.gif",
    },
    "pr": {
        "name": "Puerto Rico",
        "flag": "/++resource++country-flags/pr.gif",
    },
    "ps": {
        "name": "Palestinian Territory occupied",
        "flag": "/++resource++country-flags/ps.gif",
    },
    "pt": {
        "name": "Portugal",
        "flag": "/++resource++country-flags/pt.gif",
    },
    "pw": {"name": "Palau", "flag": "/++resource++country-flags/pw.gif"},
    "py": {
        "name": "Paraguay",
        "flag": "/++resource++country-flags/py.gif",
    },
    "qa": {"name": "Qatar", "flag": "/++resource++country-flags/qa.gif"},
    "re": {"name": "Reunion", "flag": "/++resource++country-flags/re.gif"},
    "ro": {"name": "Romania", "flag": "/++resource++country-flags/ro.gif"},
    "rs": {"name": "Serbia", "flag": "/++resource++country-flags/rs.gif"},
    "ru": {
        "name": "Russian Federation",
        "flag": "/++resource++country-flags/ru.gif",
    },
    "rw": {"name": "Rwanda", "flag": "/++resource++country-flags/rw.gif"},
    "sa": {
        "name": "Saudi Arabia",
        "flag": "/++resource++country-flags/sa.gif",
    },
    "sb": {
        "name": "Solomon Islands",
        "flag": "/++resource++country-flags/sb.gif",
    },
    "sc": {
        "name": "Seychelles",
        "flag": "/++resource++country-flags/sc.gif",
    },
    "sd": {"name": "Sudan", "flag": "/++resource++country-flags/sd.gif"},
    "se": {"name": "Sweden", "flag": "/++resource++country-flags/se.gif"},
    "sg": {
        "name": "Singapore",
        "flag": "/++resource++country-flags/sg.gif",
    },
    "sh": {
        "name": "Saint Helena",
        "flag": "/++resource++country-flags/sh.gif",
    },
    "si": {
        "name": "Slovenia",
        "flag": "/++resource++country-flags/si.gif",
    },
    "sj": {
        "name": "Svalbard and Jan Mayen",
        "flag": "/++resource++country-flags/sj.gif",
    },
    "sk": {
        "name": "Slovakia",
        "flag": "/++resource++country-flags/sk.gif",
    },
    "sl": {
        "name": "Sierra Leone",
        "flag": "/++resource++country-flags/sl.gif",
    },
    "sm": {
        "name": "San Marino",
        "flag": "/++resource++country-flags/sm.gif",
    },
    "sn": {"name": "Senegal", "flag": "/++resource++country-flags/sn.gif"},
    "so": {"name": "Somalia", "flag": "/++resource++country-flags/so.gif"},
    "sr": {
        "name": "Suriname",
        "flag": "/++resource++country-flags/sr.gif",
    },
    "ss": {
        "name": "South Sudan",
        "flag": "/++resource++country-flags/ss.png",
    },
    "st": {
        "name": "Sao Tome and Principe",
        "flag": "/++resource++country-flags/st.gif",
    },
    "sv": {
        "name": "El Salvador",
        "flag": "/++resource++country-flags/sv.gif",
    },
    "sx": {
        "name": "Sint Maarten (Dutch part)",
        "flag": "/++resource++country-flags/sx.png",
    },
    "sy": {
        "name": "Syrian Arab Republic",
        "flag": "/++resource++country-flags/sy.gif",
    },
    "sz": {
        "name": "Swaziland",
        "flag": "/++resource++country-flags/sz.gif",
    },
    "tc": {
        "name": "Turks and Caicos Islands",
        "flag": "/++resource++country-flags/tc.gif",
    },
    "td": {"name": "Chad", "flag": "/++resource++country-flags/td.gif"},
    "tf": {
        "name": "French Southern Territories",
        "flag": "/++resource++country-flags/tf.gif",
    },
    "tg": {"name": "Togo", "flag": "/++resource++country-flags/tg.gif"},
    "th": {
        "name": "Thailand",
        "flag": "/++resource++country-flags/th.gif",
    },
    "tj": {
        "name": "Tajikistan",
        "flag": "/++resource++country-flags/tj.gif",
    },
    "tk": {"name": "Tokelau", "flag": "/++resource++country-flags/tk.gif"},
    "tl": {
        "name": "Timor-Leste",
        "flag": "/++resource++country-flags/tl.gif",
    },
    "tm": {
        "name": "Turkmenistan",
        "flag": "/++resource++country-flags/tm.gif",
    },
    "tn": {"name": "Tunisia", "flag": "/++resource++country-flags/tn.gif"},
    "to": {"name": "Tonga", "flag": "/++resource++country-flags/to.gif"},
    "tr": {"name": "Turkey", "flag": "/++resource++country-flags/tr.gif"},
    "tt": {
        "name": "Trinidad and Tobago",
        "flag": "/++resource++country-flags/tt.gif",
    },
    "tv": {"name": "Tuvalu", "flag": "/++resource++country-flags/tv.gif"},
    "tw": {"name": "Taiwan", "flag": "/++resource++country-flags/tw.gif"},
    "tz": {
        "name": "Tanzania United Republic of",
        "flag": "/++resource++country-flags/tz.gif",
    },
    "ua": {"name": "Ukraine", "flag": "/++resource++country-flags/ua.gif"},
    "ug": {"name": "Uganda", "flag": "/++resource++country-flags/ug.gif"},
    "um": {
        "name": "United States Minor Outlying Islands",
        "flag": "/++resource++country-flags/um.gif",
    },
    "us": {
        "name": "United States",
        "flag": "/++resource++country-flags/us.gif",
    },
    "uy": {"name": "Uruguay", "flag": "/++resource++country-flags/uy.gif"},
    "uz": {
        "name": "Uzbekistan",
        "flag": "/++resource++country-flags/uz.gif",
    },
    "va": {
        "name": "Holy See (Vatican City State)",
        "flag": "/++resource++country-flags/va.gif",
    },
    "vc": {
        "name": "Saint Vincent and the Grenadines",
        "flag": "/++resource++country-flags/vc.gif",
    },
    "ve": {
        "name": "Venezuela",
        "flag": "/++resource++country-flags/ve.gif",
    },
    "vg": {
        "name": "Virgin Islands British",
        "flag": "/++resource++country-flags/vg.gif",
    },
    "vi": {
        "name": "Virgin Islands U.S.",
        "flag": "/++resource++country-flags/vi.gif",
    },
    "vn": {
        "name": "Viet Nam",
        "flag": "/++resource++country-flags/vn.gif",
    },
    "vu": {"name": "Vanuatu", "flag": "/++resource++country-flags/vu.gif"},
    "wf": {
        "name": "Wallis and Futuna",
        "flag": "/++resource++country-flags/wf.gif",
    },
    "ws": {"name": "Samoa", "flag": "/++resource++country-flags/ws.gif"},
    "ye": {"name": "Yemen", "flag": "/++resource++country-flags/ye.gif"},
    "yt": {"name": "Mayotte", "flag": "/++resource++country-flags/yt.gif"},
    "za": {
        "name": "South Africa",
        "flag": "/++resource++country-flags/za.gif",
    },
    "zm": {"name": "Zambia", "flag": "/++resource++country-flags/zm.gif"},
    "zw": {
        "name": "Zimbabwe",
        "flag": "/++resource++country-flags/zw.gif",
    },
    "xk": {"name": "Kosovo", "flag": "/++resource++country-flags/xk.gif"},
}

# convert the utf-8 encoded values to unicode
for code in _countrylist:
    value = _countrylist[code]
    if "name" in value:
        value["name"] = value["name"]
