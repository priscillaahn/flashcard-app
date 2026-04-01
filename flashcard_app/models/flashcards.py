import random
import uuid
from dataclasses import dataclass, field
from typing import Literal

from flashcard_app.models.parts_of_speech import PartOfSpeech, PARTS_OF_SPEECH, get_pos


@dataclass
class CardSide:
    """Defines one side of a flash card."""
    text: str
    language: str

@dataclass
class Card:
    """Flash card with a front and back side. Optional tags can be assigned."""
    front: CardSide
    back: CardSide
    part_of_speech: str | None = None
    tags: list[str] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    @property
    def translation(self) -> str:
        """Returns translation direction, e.g. 'en to ko'."""
        return f"{self.front.language} to {self.back.language}"

    @property
    def display_pos(self) -> PartOfSpeech | None:
        """Display front of card's part of speech using back of card's language"""
        if self.part_of_speech is None:
            return None
        return get_pos(self.part_of_speech, self.back.language)
    
    def reverse(self) -> "Card":
        """Flip sides of card so the languages are reversed."""
        return Card(
            front=self.back,
            back=self.front,
            part_of_speech=self.part_of_speech,
            tags=self.tags,
            id=self.id
        )


@dataclass
class Deck:
    """Deck of flash cards."""
    name: str
    description: str | None = None
    cards: list[Card] = field(default_factory=list, repr=False)

    def __post_init__(self):
        """
        Sorts cards alphabetically by the front card text when deck is initialized.
        """
        self.sort()

    def __len__(self) -> int:
        """Allows for`len(deck)` instead of `len(deck.cards)`."""
        return len(self.cards)
    
    def __contains__(self, card: Card) -> bool:
        """Allows for `card in deck` instead of `card in deck.cards`."""
        return card in self.cards
    
    def __repr__(self) -> str:
        """Dataclass already handles __repr__ but this avoids printing the whole list of cards."""
        return f"Deck(name={self.name}, cards={len(self.cards)})"
    
    def sort(self, by: Literal["front", "back"] = "front", reverse: bool = False) -> None:
        """
        Sorts cards in place.
        
        Args:
            by: Which side of the card to sort by. Options include:
                - front: sort by the front text (default).
                - back: sort by the back text.
            reverse: Direction of sort. Options include:
                - False: alphabetical order, A -> Z (default).
                - True: reverse alphabetical order, Z -> A.
        """
        key = lambda c: c.front.text if by == "front" else c.back.text
        self.cards.sort(key=key, reverse=reverse)

    def shuffle(self) -> None:
        """Shuffles cards in place."""
        random.shuffle(self.cards)

    def add_card(self, card: Card) -> None:
        """Permanently adds card to the deck."""
        self.cards.append(card)

    def delete_card(self, card_name: str) -> bool:
        """Permanently removes a card from the deck. Returns True if found and deleted."""
        card = next(
            (c for c in self.cards if card_name in (c.front.text, c.back.text)),
            None
        )
        if card:
            self.cards.remove(card)
            return True
        return False
