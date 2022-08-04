import re

from pydantic import BaseModel
from random import choice, randint
from json import load


class Random:
    data = {}
    filenames = {
        "professions.json": "profession",
        "biology.json": "biology",
        "health.json": "health",
        "hobby.json": "hobby",
        "baggage.json": "baggage",
        "facts.json": "facts",
        "special_cards.json": "special_cards"
    }

    def generate(self) -> dict:
        for filename in self.filenames.keys():
            with open(filename, "r", encoding="utf-8") as file:
                objects = dict(load(file))
                value = choice(objects[self.filenames[filename]])
                value = re.sub(r"AGE", str(randint(18, 90)), value)
                self.data.update(
                    {
                        self.filenames[filename]: value
                    }
                )
        return self.data


class Player(BaseModel):
    profession: str
    biology: str
    health: str
    hobby: str
    baggage: str
    facts: str
    special_cards: str
