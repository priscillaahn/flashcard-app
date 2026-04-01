from dataclasses import dataclass


@dataclass(frozen=True)
class PartOfSpeech():
    """Part of Speech label and abbreviations"""
    label: str
    abbrev: str


# According to ISO 2-letter language code
PARTS_OF_SPEECH: dict[str, dict[str, PartOfSpeech]] = {
    "en": {
        "adjective": PartOfSpeech("adjective", "adj."),
        "adverb": PartOfSpeech("adverb", "adv."),
        "conjunction": PartOfSpeech("conjunction", "conj."),
        "determiner": PartOfSpeech("determiner", "det."),
        "interjection": PartOfSpeech("interjection", "interj."),
        "noun": PartOfSpeech("noun", "n."),
        "numeral": PartOfSpeech("numeral", "num."),
        "particle": PartOfSpeech("particle", "part."), 
        "preposition": PartOfSpeech("preposition", "prep."),
        "pronoun": PartOfSpeech("pronoun", "pron."),
        "verb": PartOfSpeech("verb", "v."),
    },
    "ko": {
        "adjective": PartOfSpeech("형용사", "형"),
        "adverb": PartOfSpeech("부사", "부"),
        "determiner": PartOfSpeech("관형사", "관"),
        "interjection": PartOfSpeech("감탄사", "감"),
        "noun": PartOfSpeech("명사", "명"),
        "numeral": PartOfSpeech("수사", "수"),
        "particle": PartOfSpeech("조사", "조"), 
        "pronoun": PartOfSpeech("대명사", "대"),
        "verb": PartOfSpeech("동사", "동"),
    },
    "bg": {
        "adjective": PartOfSpeech("прилагателно", "прил."),
        "adverb": PartOfSpeech("наречие", "нар."),
        "conjunction": PartOfSpeech("съюз", "съюз"),
        "interjection": PartOfSpeech("междуметие", "межд."),
        "noun": PartOfSpeech("съществително", "същ."),
        "numeral": PartOfSpeech("числително", "числ."),
        "preposition": PartOfSpeech("предлог", "предл."),
        "pronoun": PartOfSpeech("местоимение", "мест."),
        "verb": PartOfSpeech("глагол", "гл."),
    },
}


def get_pos(part_of_speech: str, language: str) -> PartOfSpeech:
    """Look up part of speech label and abbreviations by language code."""
    result = PARTS_OF_SPEECH.get(language, {}).get(part_of_speech)
    if result is None:
        raise KeyError(
            f"No part of speech label found for language='{language}', pos='{part_of_speech}'"
        )
    return result