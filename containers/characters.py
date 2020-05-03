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
        # TODO: Add inventory printing

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