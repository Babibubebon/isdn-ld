from rdflib import Namespace
from rdflib.namespace import RDF, RDFS, XSD, ClosedNamespace

SCHEMA = Namespace("http://schema.org/")
ISDN_RES = Namespace("https://metadata.moe/isdn/res/")


ISDN = ClosedNamespace(
    "https://metadata.moe/ns/isdn/",
    [
        # Classes
        "DoujinProduct",
        "ComiketGenre",
        "CCode",
        ## 形態
        "Book",
        "DoujinGoods",
        "Music",
        "Software",
        "Hardware",
        "FigurativeProduct",
        "Wearable",
        "Flyer",
        "EventCatalog",
        ## 大分類
        "OriginalWork",
        "DerivativeWork",
        # Properties
        "isdn",
        "isdnPrefix",
        "isdnRegistrationGroup",
        "isdnRegistrationGroupName",
        "isdnRegistrant",
        "isdnPublication",
        "isdnCheckDigit",
        "derivationType",
        "ratingGender",
        "ratingAge",
        "cCodeTargetAudience",
        "cCodePublicationForm",
        "cCodeContentCategory",
        "bookJanCodeSecondRow",
        "productStyle",
        "printingMethod",
        "bindingMethod",
        "carrierType",
        "carrierExtent",
    ],
)

ISDN_GRAPH = ClosedNamespace(
    "https://metadata.moe/isdn/graph/", ["ageUnrestricted", "ageRestricted15", "ageRestricted18"]
)


__all__ = [
    "RDF",
    "RDFS",
    "XSD",
    "SCHEMA",
    "ISDN",
    "ISDN_RES",
    "ISDN_GRAPH",
]
