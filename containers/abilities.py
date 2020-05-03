from __future__ import annotations
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging
from dataclasses import dataclass

class Abilities:
    '''Class for keeping track of Character Abilities'''

    def __init__(self, xmltree: ET.Element) -> Abilities:
        abilities = xmltree.find('abilities')

        self.charisma = self.Charisma(abilities)
        self.constitution = self.Constitution(abilities)
        self.dexterity = self.Dexterity(abilities)
        self.intelligence = self.Intelligence(abilities)
        self.strength = self.Strength(abilities)
        self.wisdom = self.Wisdom(abilities)

    class Charisma:
        def __init__(self, xmltree: ET.Element):
            values = self.find(xmltree)
            self.bonus = values["bonus"]
            self.save = values["save"]
            self.savemod = values["savemod"]
            self.saveprof = values["saveprof"]
            self.score = values["score"]
        
        def find(self, xmltree: ET.Element) -> Dict[AnyStr, int]:
            charisma = xmltree.find("charisma")
            bonus = charisma.find("bonus")
            save = charisma.find("save")
            savemod = charisma.find("savemodifier")
            saveprof = charisma.find("saveprof")
            score = charisma.find("score")
            return {
                "bonus": bonus.text if bonus is not None else 0,
                "save": save.text if save is not None else 0,
                "savemod": savemod.text if savemod is not None else 0,
                "saveprof": saveprof.text if saveprof is not None else 0,
                "score": score.text if score is not None else 0
            }

        def update(self, xmltree: ET.Element) -> None:
            pass
        

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
            bonus = constitution.find("bonus")
            save = constitution.find("save")
            savemod = constitution.find("savemodifier")
            saveprof = constitution.find("saveprof")
            score = constitution.find("score")
            return {
                "bonus": bonus.text if bonus is not None else 0,
                "save": save.text if save is not None else 0,
                "savemod": savemod.text if savemod is not None else 0,
                "saveprof": saveprof.text if saveprof is not None else 0,
                "score": score.text if score is not None else 0
            }

        def update(self, xmltree: ET.Element) -> None:
            pass
    
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
            bonus = dexterity.find("bonus")
            save = dexterity.find("save")
            savemod = dexterity.find("savemodifier")
            saveprof = dexterity.find("saveprof")
            score = dexterity.find("score")
            return {
                "bonus": bonus.text if bonus is not None else 0,
                "save": save.text if save is not None else 0,
                "savemod": savemod.text if savemod is not None else 0,
                "saveprof": saveprof.text if saveprof is not None else 0,
                "score": score.text if score is not None else 0
            }
        
        def update(self, xmltree: ET.Element) -> None:
            pass

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
            bonus = intelligence.find("bonus")
            save = intelligence.find("save")
            savemod = intelligence.find("savemodifier")
            saveprof = intelligence.find("saveprof")
            score = intelligence.find("score")
            return {
                "bonus": bonus.text if bonus is not None else 0,
                "save": save.text if save is not None else 0,
                "savemod": savemod.text if savemod is not None else 0,
                "saveprof": saveprof.text if saveprof is not None else 0,
                "score": score.text if score is not None else 0
            }

        def update(self, xmltree: ET.Element) -> None:
            pass

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
            bonus = strength.find("bonus")
            save = strength.find("save")
            savemod = strength.find("savemodifier")
            saveprof = strength.find("saveprof")
            score = strength.find("score")
            return {
                "bonus": bonus.text if bonus is not None else 0,
                "save": save.text if save is not None else 0,
                "savemod": savemod.text if savemod is not None else 0,
                "saveprof": saveprof.text if saveprof is not None else 0,
                "score": score.text if score is not None else 0
            }

        def update(self, xmltree: ET.Element) -> None:
            pass

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
            bonus = wisdom.find("bonus")
            save = wisdom.find("save")
            savemod = wisdom.find("savemodifier")
            saveprof = wisdom.find("saveprof")
            score = wisdom.find("score")
            return {
                "bonus": bonus.text if bonus is not None else 0,
                "save": save.text if save is not None else 0,
                "savemod": savemod.text if savemod is not None else 0,
                "saveprof": saveprof.text if saveprof is not None else 0,
                "score": score.text if score is not None else 0
            }

        def update(self, xmltree: ET.Element) -> None:
            pass