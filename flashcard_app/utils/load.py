from typing import Optional

import pandas as pd

from flashcard_app.models.flashcards import CardSide, Card, Deck
from flashcard_app.utils.language import standardize_language_input


def load_csv(csv_filepath: str) -> pd.DataFrame:
    """Loads csv as pandas dataframe."""
    try:
        data = pd.read_csv(csv_filepath)
        return data
    except Exception as e:
        raise RuntimeError(f"Failed to load CSV '{csv_filepath}'") from e

def convert_tags_to_list(tags_str: str) -> list[str]:
    """Convert comma-separated tags string from CSV to a list."""
    return [t.strip() for t in tags_str.split(",") if t.strip()]

def load_cards_from_csv(csv_filepath: str, lang_front: str, lang_back: str) -> list[Card]:
    """Creates a list of card objects from a csv."""
    data = load_csv(csv_filepath=csv_filepath)
    
    lang_tag_front = standardize_language_input(lang_front)
    lang_tag_back = standardize_language_input(lang_back)

    cards: list[Card] = []
    for row in data.itertuples(index=False):
        card = Card(
            front=CardSide(
                text=str(row.front),
                language=lang_tag_front,
            ),
            back=CardSide(
                text=str(row.back),
                language=lang_tag_back,
                ),
            part_of_speech=str(row.part_of_speech) if pd.notna(row.part_of_speech) else None,
            tags=convert_tags_to_list(str(row.tags)) if pd.notna(row.tags) else []
        )
        cards.append(card)
    
    return cards

def create_deck(
    cards: list[Card],
    name: str,
    description: Optional[str] = None,
) -> Deck:
    """Creates deck from a list of cards."""
    return Deck(
        name=name, description=description, cards=cards
    )

