from __future__ import annotations
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging
from dataclasses import dataclass
from containers.money import Money
from containers.attributes import Attributes
from containers.abilities import Abilities

class Character:
    def __init__(self, attributes: Attributes, money: Money, abilities: Abilities):
        self.attributes = attributes
        self.money = money
        self.abilities = abilities

    def log(self):
        logging.info("-" * 10)
        logging.info(f"Character DB Tag: {self.attributes.tag}")
        logging.info(f"Character Owner: {self.attributes.owner}")
        logging.info(f"Character Name: {self.attributes.name}")
        logging.info(f"Character Money: {self.money.cp} CP; {self.money.sp} SP; {self.money.gp} GP")
        logging.info(f"""Charisma Scores: \t
            Bonus: {self.abilities.charisma.bonus} \
            Save: {self.abilities.charisma.save} \
            Savemod: {self.abilities.charisma.savemod} \
            Saveprof: {self.abilities.charisma.saveprof} \
            Score: {self.abilities.charisma.score}""")

        logging.info(f"""Constitution Scores: \t
            Bonus: {self.abilities.constitution.bonus} \
            Save: {self.abilities.constitution.save} \
            Savemod: {self.abilities.constitution.savemod} \
            Saveprof: {self.abilities.constitution.saveprof} \
            Score: {self.abilities.constitution.score}""")

        logging.info(f"""Dexterity Scores: \t
            Bonus: {self.abilities.dexterity.bonus} \
            Save: {self.abilities.dexterity.save} \
            Savemod: {self.abilities.dexterity.savemod} \
            Saveprof: {self.abilities.dexterity.saveprof} \
            Score: {self.abilities.dexterity.score}""")

        logging.info(f"""Intelligence Scores: \t
            Bonus: {self.abilities.intelligence.bonus} \
            Save: {self.abilities.intelligence.save} \
            Savemod: {self.abilities.intelligence.savemod} \
            Saveprof: {self.abilities.intelligence.saveprof} \
            Score: {self.abilities.intelligence.score}""")

        logging.info(f"""Strength Scores: \t
            Bonus: {self.abilities.strength.bonus} \
            Save: {self.abilities.strength.save} \
            Savemod: {self.abilities.strength.savemod} \
            Saveprof: {self.abilities.strength.saveprof} \
            Score: {self.abilities.strength.score}""")

        logging.info(f"""Wisdom Scores: \t
            Bonus: {self.abilities.wisdom.bonus} \
            Save: {self.abilities.wisdom.save} \
            Savemod: {self.abilities.wisdom.savemod} \
            Saveprof: {self.abilities.wisdom.saveprof} \
            Score: {self.abilities.wisdom.score}""")
        # TODO: Move logging to each class instead of owner class character

    def update(self, xmltree:ET.Element) -> None:
        logging.debug(f"Update Character: {self.attributes.name} -> Start")

        # Find its own node in the XML tree and pass that to all internal update functions
        xmltree = xmltree.find(self.attributes.tag)
        self.attributes.update(xmltree)
        self.money.update(
            self.attributes.owner,
            self.attributes.name, 
        xmltree)

        logging.debug(f"Update Character: {self.attributes.name} -> Stop")

    @staticmethod
    def generate_characters_from_tree(xmltree: ET.Element) -> Dict[AnyStr, Character]:
        results = {}
        for _character in xmltree.getchildren():

            attributes = Attributes(_character)
            money = Money(_character)
            abilities = Abilities(_character)

            results[_character.tag] = Character(
                attributes, 
                money,
                abilities
            )

        logging.info("Character load from DB completed, characters:")
        for tag in results:
            results[tag].log()

        return results