from plone.supermodel import model
from zope import schema

# Definition of Import PloneMessageFactory to create messages in the plone
# domain. We do a fresh re-definition here as to break the dependency on
# `Products.CMFPlone.PloneMessageFactory`.
from zope.i18nmessageid import MessageFactory
from zope.interface import Attribute
from zope.interface import Interface


_ = PloneMessageFactory = MessageFactory("plone")


class ILanguageUtility(Interface):
    """Marker interface for the portal_languages tool."""


class INegotiateLanguage(Interface):
    """Result of language negotiation"""

    language = Attribute("Language to use")
    default_language = Attribute("Default language")
    language_list = Attribute("List of language preferences in order")


class ILanguageSchema(Interface):
    model.fieldset(
        "general",
        label=_("General"),
        fields=[
            "default_language",
            "available_languages",
            "use_combined_language_codes",
            "display_flags",
            "always_show_selector",
        ],
    )

    default_language = schema.Choice(
        title=_("heading_site_language", default="Site language"),
        description=_(
            "description_site_language",
            default="The language used for the content and the UI of " "this site.",
        ),
        default="en",
        required=True,
        vocabulary="plone.app.vocabularies.AvailableContentLanguages",
    )

    available_languages = schema.List(
        title=_("heading_available_languages", default="Available languages"),
        description=_(
            "description_available_languages",
            default="The languages in which the site should be " "translatable.",
        ),
        required=True,
        default=["en"],
        missing_value=[],
        value_type=schema.Choice(
            vocabulary="plone.app.vocabularies.AvailableContentLanguages"
        ),
    )

    use_combined_language_codes = schema.Bool(
        title=_(
            "label_allow_combined_language_codes",
            default="Show country-specific language variants",
        ),
        description=_(
            "help_allow_combined_language_codes",
            default="Examples: pt-br (Brazilian Portuguese), "
            "en-us (American English) etc.",
        ),
        default=True,
        required=False,
    )

    display_flags = schema.Bool(
        title=_("label_display_flags", default="Show language flags"),
        description="",
        default=False,
        required=False,
    )

    always_show_selector = schema.Bool(
        title=_(
            "label_always_show_selector",
            default="Always show language selector",
        ),
        description="",
        default=False,
        required=False,
    )

    model.fieldset(
        "negotiation_scheme",
        label=_("Negotiation scheme", default="Negotiation scheme"),
        fields=[
            "use_content_negotiation",
            "use_path_negotiation",
            "use_cookie_negotiation",
            "authenticated_users_only",
            "set_cookie_always",
            "use_subdomain_negotiation",
            "use_cctld_negotiation",
            "use_request_negotiation",
        ],
    )
    use_content_negotiation = schema.Bool(
        title=_(
            "heading_language_of_the_content",
            default="Use the language of the content item",
        ),
        description=_(
            "description_language_of_the_content",
            default="Use the language of the content item.",
        ),
        default=False,
        required=False,
    )

    use_path_negotiation = schema.Bool(
        title=_(
            "heading_language_codes_in_URL",
            default="Use language codes in URL path for manual override",
        ),
        description=_(
            "description_language_codes_in_URL",
            default="Use language codes in URL path for manual override.",
        ),
        default=False,
        required=False,
    )

    use_cookie_negotiation = schema.Bool(
        title=_(
            "heading_cookie_manual_override",
            default=("Use cookie for manual override"),
        ),
        description=_(
            "description_cookie_manual_override",
            default=("Required for the language selector viewlet to be rendered."),
        ),
        default=False,
        required=False,
    )

    authenticated_users_only = schema.Bool(
        title=_(
            "heading_auth_cookie_manual_override",
            default="Authenticated users only",
        ),
        description=_(
            "description_auth_ookie_manual_override",
            default=("Related to: use cookie for manual override"),
        ),
        default=False,
        required=False,
    )

    set_cookie_always = schema.Bool(
        title=_(
            "heading_set_language_cookie_always",
            default=("Set the language cookie always"),
        ),
        description=_(
            "description_set_language_cookie_always",
            default=(
                "i.e. also when the 'set_language' request parameter is " "absent"
            ),
        ),
        default=False,
        required=False,
    )

    use_subdomain_negotiation = schema.Bool(
        title=_("heading_use_subdomain", default="Use subdomain"),
        description=_("description_use_subdomain", default="e.g.: de.plone.org"),
        default=False,
        required=False,
    )

    use_cctld_negotiation = schema.Bool(
        title=_("heading_top_level_domain", default="Use top-level domain"),
        description=_("description_top_level_domain", default="e.g.: www.plone.de"),
        default=False,
        required=False,
    )

    use_request_negotiation = schema.Bool(
        title=_(
            "heading_browser_language_request_negotiation",
            default="Use browser language request negotiation",
        ),
        description=_(
            "description_browser_language_request_negotiation",
            default="Use browser language request negotiation.",
        ),
        default=False,
        required=False,
    )
