from __future__ import annotations
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging
from dataclasses import dataclass

class Abilities:
    '''Class for keeping track of Character Abilities'''

    @staticmethod
    def get_values(xmltree: ET.Element) -> Dict[AnyStr, AnyStr]:
        logging.debug(f"Find Values from {xmltree}")
        bonus = xmltree.find("bonus")
        save = xmltree.find("save")
        savemod = xmltree.find("savemodifier")
        saveprof = xmltree.find("saveprof")
        score = xmltree.find("score")
        return {
            "bonus": bonus.text if bonus is not None else 0,
            "save": save.text if save is not None else 0,
            "savemod": savemod.text if savemod is not None else 0,
            "saveprof": saveprof.text if saveprof is not None else 0,
            "score": score.text if score is not None else 0
        }

    def __init__(self, xmltree: ET.Element) -> Abilities:
        logging.debug(f"Init abilities from {xmltree}")
        abilities = xmltree.find('abilities')

        self.charisma = self.Charisma(abilities)
        self.constitution = self.Constitution(abilities)
        self.dexterity = self.Dexterity(abilities)
        self.intelligence = self.Intelligence(abilities)
        self.strength = self.Strength(abilities)
        self.wisdom = self.Wisdom(abilities)

    def update(self, owner: AnyStr, name: AnyStr, xmltree: ET.Element) -> None:
        xmltree = xmltree.find('abilities')

        self.charisma.update(owner, name, xmltree)
        self.constitution.update(owner, name, xmltree)
        self.dexterity.update(owner, name, xmltree)
        self.intelligence.update(owner, name, xmltree)
        self.strength.update(owner, name, xmltree)
        self.wisdom.update(owner, name, xmltree)

    class Charisma:
        def __init__(self, xmltree: ET.Element):
            logging.debug(f"Init Charisma from {xmltree}")

            values = self.find(xmltree)
            self.bonus = values["bonus"]
            self.save = values["save"]
            self.savemod = values["savemod"]
            self.saveprof = values["saveprof"]
            self.score = values["score"]
        
        def find(self, xmltree: ET.Element) -> Dict[AnyStr, int]:
            logging.debug(f"Find Charisma from {xmltree}")
            charisma = xmltree.find("charisma")
            return Abilities.get_values(charisma)

        def update(self, owner: AnyStr, name: AnyStr, xmltree: ET.Element) -> None:
            logging.debug(f"Update Charisma from {xmltree}")
            values = self.find(xmltree)
            if self.bonus != values["bonus"]:
                logging.info(f"Updated Charisma Bonus for {name}, owned by {owner}, {self.bonus} -> {values['bonus']}")
                self.bonus = values["bonus"]
            if self.save != values["save"]:
                logging.info(f"Updated Charisma Save for {name}, owned by {owner}, {self.save} -> {values['save']}")
                self.bonus = values["bonus"]
            if self.savemod != values["savemod"]:
                logging.info(f"Updated Charisma SaveMod for {name}, owned by {owner}, {self.savemod} -> {values['savemod']}")
                self.bonus = values["bonus"]
            if self.saveprof != values["saveprof"]:
                logging.info(f"Updated Charisma SaveProf for {name}, owned by {owner}, {self.saveprof} -> {values['saveprof']}")
                self.bonus = values["bonus"]
            if self.score != values["score"]:
                logging.info(f"Updated Charisma Score for {name}, owned by {owner}, {self.score} -> {values['score']}")
                self.bonus = values["bonus"]

    class Constitution:

        def __init__(self, xmltree: ET.Element):
            values = self.find(xmltree)
            self.bonus = values["bonus"]
            self.save = values["save"]
            self.savemod = values["savemod"]
            self.saveprof = values["saveprof"]
            self.score = values["score"]
        
        def find(self, xmltree: ET.Element) -> Dict[AnyStr, int]:
            constitution = xmltree.find("constitution")
            return Abilities.get_values(constitution)

        def update(self, owner: AnyStr, name: AnyStr, xmltree: ET.Element) -> None:
            values = self.find(xmltree)
            if self.bonus != values["bonus"]:
                logging.info(f"Updated Constitution Bonus for {name}, owned by {owner}, {self.bonus} -> {values['bonus']}")
                self.bonus = values["bonus"]
            if self.save != values["save"]:
                logging.info(f"Updated Constitution Save for {name}, owned by {owner}, {self.save} -> {values['save']}")
                self.bonus = values["bonus"]
            if self.savemod != values["savemod"]:
                logging.info(f"Updated Constitution SaveMod for {name}, owned by {owner}, {self.savemod} -> {values['savemod']}")
                self.bonus = values["bonus"]
            if self.saveprof != values["saveprof"]:
                logging.info(f"Updated Constitution SaveProf for {name}, owned by {owner}, {self.saveprof} -> {values['saveprof']}")
                self.bonus = values["bonus"]
            if self.score != values["score"]:
                logging.info(f"Updated Constitution Score for {name}, owned by {owner}, {self.score} -> {values['score']}")
                self.bonus = values["bonus"]
    
    class Dexterity:
        def __init__(self, xmltree: ET.Element):
            values = self.find(xmltree)
            self.bonus = values["bonus"]
            self.save = values["save"]
            self.savemod = values["savemod"]
            self.saveprof = values["saveprof"]
            self.score = values["score"]
        
        def find(self, xmltree: ET.Element) -> Dict[AnyStr, int]:
            dexterity = xmltree.find("dexterity")
            return Abilities.get_values(dexterity)
        
        def update(self, owner: AnyStr, name: AnyStr, xmltree: ET.Element) -> None:
            values = self.find(xmltree)
            if self.bonus != values["bonus"]:
                logging.info(f"Updated Dexterity Bonus for {name}, owned by {owner}, {self.bonus} -> {values['bonus']}")
                self.bonus = values["bonus"]
            if self.save != values["save"]:
                logging.info(f"Updated Dexterity Save for {name}, owned by {owner}, {self.save} -> {values['save']}")
                self.bonus = values["bonus"]
            if self.savemod != values["savemod"]:
                logging.info(f"Updated Dexterity SaveMod for {name}, owned by {owner}, {self.savemod} -> {values['savemod']}")
                self.bonus = values["bonus"]
            if self.saveprof != values["saveprof"]:
                logging.info(f"Updated Dexterity SaveProf for {name}, owned by {owner}, {self.saveprof} -> {values['saveprof']}")
                self.bonus = values["bonus"]
            if self.score != values["score"]:
                logging.info(f"Updated Dexterity Score for {name}, owned by {owner}, {self.score} -> {values['score']}")
                self.bonus = values["bonus"]

    class Intelligence:
        def __init__(self, xmltree: ET.Element):
            values = self.find(xmltree)
            self.bonus = values["bonus"]
            self.save = values["save"]
            self.savemod = values["savemod"]
            self.saveprof = values["saveprof"]
            self.score = values["score"]
        
        def find(self, xmltree: ET.Element) -> Dict[AnyStr, int]:
            intelligence = xmltree.find("intelligence")
            return Abilities.get_values(intelligence)

        def update(self, owner: AnyStr, name: AnyStr, xmltree: ET.Element) -> None:
            values = self.find(xmltree)
            if self.bonus != values["bonus"]:
                logging.info(f"Updated Intelligence Bonus for {name}, owned by {owner}, {self.bonus} -> {values['bonus']}")
                self.bonus = values["bonus"]
            if self.save != values["save"]:
                logging.info(f"Updated Intelligence Save for {name}, owned by {owner}, {self.save} -> {values['save']}")
                self.bonus = values["bonus"]
            if self.savemod != values["savemod"]:
                logging.info(f"Updated Intelligence SaveMod for {name}, owned by {owner}, {self.savemod} -> {values['savemod']}")
                self.bonus = values["bonus"]
            if self.saveprof != values["saveprof"]:
                logging.info(f"Updated Intelligence SaveProf for {name}, owned by {owner}, {self.saveprof} -> {values['saveprof']}")
                self.bonus = values["bonus"]
            if self.score != values["score"]:
                logging.info(f"Updated Intelligence Score for {name}, owned by {owner}, {self.score} -> {values['score']}")
                self.bonus = values["bonus"]

    class Strength:
        def __init__(self, xmltree: ET.Element):
            values = self.find(xmltree)
            self.bonus = values["bonus"]
            self.save = values["save"]
            self.savemod = values["savemod"]
            self.saveprof = values["saveprof"]
            self.score = values["score"]
        
        def find(self, xmltree: ET.Element) -> Dict[AnyStr, int]:
            strength = xmltree.find("strength")
            return Abilities.get_values(strength)

        def update(self, owner: AnyStr, name: AnyStr, xmltree: ET.Element) -> None:
            values = self.find(xmltree)
            if self.bonus != values["bonus"]:
                logging.info(f"Updated Strength Bonus for {name}, owned by {owner}, {self.bonus} -> {values['bonus']}")
                self.bonus = values["bonus"]
            if self.save != values["save"]:
                logging.info(f"Updated Strength Save for {name}, owned by {owner}, {self.save} -> {values['save']}")
                self.bonus = values["bonus"]
            if self.savemod != values["savemod"]:
                logging.info(f"Updated Strength SaveMod for {name}, owned by {owner}, {self.savemod} -> {values['savemod']}")
                self.bonus = values["bonus"]
            if self.saveprof != values["saveprof"]:
                logging.info(f"Updated Strength SaveProf for {name}, owned by {owner}, {self.saveprof} -> {values['saveprof']}")
                self.bonus = values["bonus"]
            if self.score != values["score"]:
                logging.info(f"Updated Strength Score for {name}, owned by {owner}, {self.score} -> {values['score']}")
                self.bonus = values["bonus"]

    class Wisdom:
        def __init__(self, xmltree: ET.Element):
            values = self.find(xmltree)
            self.bonus = values["bonus"]
            self.save = values["save"]
            self.savemod = values["savemod"]
            self.saveprof = values["saveprof"]
            self.score = values["score"]
        
        def find(self, xmltree: ET.Element) -> Dict[AnyStr, int]:
            wisdom = xmltree.find("wisdom")
            return Abilities.get_values(wisdom)

        def update(self, owner: AnyStr, name: AnyStr, xmltree: ET.Element) -> None:
            values = self.find(xmltree)
            if self.bonus != values["bonus"]:
                logging.info(f"Updated Wisdom Bonus for {name}, owned by {owner}, {self.bonus} -> {values['bonus']}")
                self.bonus = values["bonus"]
            if self.save != values["save"]:
                logging.info(f"Updated Wisdom Save for {name}, owned by {owner}, {self.save} -> {values['save']}")
                self.bonus = values["bonus"]
            if self.savemod != values["savemod"]:
                logging.info(f"Updated Wisdom SaveMod for {name}, owned by {owner}, {self.savemod} -> {values['savemod']}")
                self.bonus = values["bonus"]
            if self.saveprof != values["saveprof"]:
                logging.info(f"Updated Wisdom SaveProf for {name}, owned by {owner}, {self.saveprof} -> {values['saveprof']}")
                self.bonus = values["bonus"]
            if self.score != values["score"]:
                logging.info(f"Updated Wisdom Score for {name}, owned by {owner}, {self.score} -> {values['score']}")
                self.bonus = values["bonus"]