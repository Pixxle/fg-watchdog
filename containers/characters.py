from __future__ import annotations
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging
from dataclasses import dataclass
from containers.money import Money
from containers.attributes import Attributes

class Character:
    def __init__(self, attr: Dict[AnyStr, AnyStr], money: Dict[AnyStr, int]):
        self.attributes = Attributes(
            name=attr["name"], 
            owner=attr["owner"],
            tag=attr["tag"]
        )

        self.money = Money(
            cp = money["cp"],
            sp = money["sp"],
            gp = money["gp"]
        )

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
        self.attributes.update_attributes(xmltree)
        self.money.update_gold(self.attributes.name, xmltree)

        logging.debug(f"Update Character: {self.attributes.name} -> Stop")

    @staticmethod
    def generate_characters_from_tree(xmltree: ET.Element) -> Dict[AnyStr, Character]:
        results = {}
        for _character in xmltree.getchildren():
            
            attributes = Attributes.find(_character)
            attributes["tag"] = _character.tag

            money = Money.find(_character)

            results[attributes["tag"]] = Character(attributes, money)

        logging.info("Character load from DB completed, characters:")
        for tag in results:
            results[tag].log()

        return results