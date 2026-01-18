from typing import Dict

def get_response_format_for_entities(
) -> Dict:
    """
    TODO
    """
    return {
        "response_format": {
            "type": "json_schema",
            "json_schema" : {
                "name": "entity_extraction",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "people": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "locations": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "companies": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "events": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "required": [
                        "people",
                        "locations",
                        "companies",
                        "events",
                    ],
                    "additionalProperties": False
                }
            }
        }
    }


def get_response_format_for_topics(
) -> Dict:
    """
    TODO
    """
    return {
        "response_format": {
            "type": "json_schema",
            "json_schema" : {
                "name": "topic_extraction",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "topics": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                    },
                    "required": [
                        "topics",
                    ],
                    "additionalProperties": False
                }
            }
        }
    }


def get_response_format_for_evergreen(
) -> Dict:
    """
    TODO
    """
    return {
        "response_format": {
            "type": "json_schema",
            "json_schema" : {
                "name": "evergreen_classification",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "evergreen": {
                            "type": "integer",
                            "enum": [
                                0,
                                1,
                                2,
                            ],
                        },
                    },
                    "required": [
                        "evergreen",
                    ],
                    "additionalProperties": False
                }
            }
        }
    }


def get_response_format_for_sentiment(
) -> Dict:
    """
    TODO
    """
    return {
        "response_format": {
            "type": "json_schema",
            "json_schema" : {
                "name": "sentiment_classification",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "sentiment": {
                            "type": "string",
                            "enum": [
                                "Positive",
                                "Neutral",
                                "Negative",
                            ],
                        },
                    },
                    "required": [
                        "sentiment",
                    ],
                    "additionalProperties": False
                }
            }
        }
    }



def get_response_format_for_evergreen(
) -> Dict:
    """
    TODO
    """
    return {
        "response_format": {
            "type": "json_schema",
            "json_schema" : {
                "name": "evergreen_classification",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "evergreen": {
                            "type": "integer",
                            "enum": [
                                0,
                                1,
                                2,
                            ],
                        },
                    },
                    "required": [
                        "evergreen",
                    ],
                    "additionalProperties": False
                }
            }
        }
    }


def get_response_format_for_angles(
) -> Dict:
    """
    TODO
    """
    return {
        "response_format": {
            "type": "json_schema",
            "json_schema" : {
                "name": "angle_classification",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "angles": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": [
                                    "News / Reportage",
                                    "Explainer",
                                    "Analytical",
                                    "Investigative",
                                    "Opinion / Commentary",
                                    "Human Story / Profile",
                                    "Practical / How-to",
                                    "Review / Critique",
                                    "Data-driven",
                                    "Longform / Feature",
                                    "Lifestyle / Popular Science",
                                    "Marketing / Branded",
                                    "Other",
                                ]
                            }
                        },
                    },
                    "required": [
                        "angles",
                    ],
                    "additionalProperties": False
                }
            }
        }
    }


def get_response_format_for_disqus(
) -> Dict:
    """
    TODO
    """
    return {
        "response_format": {
            "type": "json_schema",
            "json_schema" : {
                "name": "topics_classification",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "topics": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": [
                                    "Alternatívna medicína",
                                    "Automobilový priemysel",
                                    "Bezpečnosť",
                                    "Bývanie",
                                    "Celebrity",
                                    "Cestovanie",
                                    "Dane",
                                    "Diplomacia",
                                    "Domácnosť",
                                    "Doprava",
                                    "Ekonomika",
                                    "Energia",
                                    "Film",
                                    "Financie",
                                    "Generácie",
                                    "História",
                                    "Hobby",
                                    "Hudba",
                                    "IT",
                                    "Inflácia",
                                    "Inovácie",
                                    "Klimatické zmeny",
                                    "Kriminalita",
                                    "Kuchyňa",
                                    "Kultúra",
                                    "Literatúra",
                                    "Marketing",
                                    "Médiá",
                                    "Nevera",
                                    "Náboženstvo",
                                    "Obchod",
                                    "Očkovanie",
                                    "Peniaze",
                                    "Podnikanie",
                                    "Pokrytectvo",
                                    "Politika",
                                    "Poľnohospodárstvo",
                                    "Priemysel",
                                    "Práca",
                                    "Právo",
                                    "Príroda",
                                    "Psychológia",
                                    "Rastliny",
                                    "Rodina",
                                    "Sex",
                                    "Spoločnosť",
                                    "Technológie",
                                    "Tradície",
                                    "Umenie",
                                    "Veda",
                                    "Vesmír",
                                    "Vláda",
                                    "Vojenské otázky",
                                    "Vzdelávanie",
                                    "Vzťahy",
                                    "Výživa",
                                    "Zamestnanie",
                                    "Zdravie",
                                    "Zdravotníctvo",
                                    "Zvieratá",
                                    "Záhrada",
                                    "Škandály",
                                    "Školstvo",
                                    "Šport",
                                    "Životné prostredie",
                                    "Životný štýl",
                                ]
                            }
                        },
                    },
                    "required": [
                        "topics",
                    ],
                    "additionalProperties": False
                }
            }
        }
    }
