from apps.Yugioh_Database.models import Monster_Card, Spell_Card, Trap_Card
import os
import json
from pathlib import Path

CARD_PATH = Path(os.getcwd()).resolve()
card_path = CARD_PATH / "en"


def add_cards():
    cards = os.listdir(card_path)
    for card in cards:
        with open(card_path / card, "r") as f:
            data = json.load(f)
            print(f"{f} is loaded!")
            if data["type"] == "monster":
                monster_card = Monster_Card.objects.create(
                    name=data["name"],
                    card_type=data["type"],
                    attack=data["atk"],
                    attribute=data["localizedAttribute"],
                    description=data["effectText"],
                )
                print(f"{monster_card.name} is created!")
            elif data["type"] == "spell":
                spell_card = Spell_Card.objects.create(
                    name=data["name"],
                    card_type=data["type"],
                    type=data["localizedAttribute"],
                    description=data["effectText"],
                )
                print(f"{spell_card.name} is created!")
            elif data["type"] == "trap":
                trap_card = Trap_Card.objects.create(
                    name=data["name"],
                    card_type=data["type"],
                    type=data["localizedAttribute"],
                    description=data["effectText"],
                )
                print(f"{trap_card.name} is created!")

# doesnt work because en folder was zipped to make a clean overview
# add_cards()
