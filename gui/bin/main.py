import re
import os

from pydantic import BaseModel
from random import choice, randint
from json import load

current_dir = os.path.dirname(os.path.realpath(__file__))


class Random:
    data = {}
    filenames = {
        "professions.json": "profession",
        "biology.json": "biology",
        "health.json": "health",
        "hobby.json": "hobby",
        "baggage.json": "baggage",
        "facts.json": "facts",
        "special_cards.json": "special_cards",
        "disasters.json": "disaster"
    }

    def generate_player_stats(self) -> dict:
        for filename in self.filenames.keys():
            with open(os.path.join(current_dir, filename), "r", encoding="utf-8") as file:
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
    disaster: str


if __name__ == '__main__':
    print(Player(**Random().generate_player_stats()))
