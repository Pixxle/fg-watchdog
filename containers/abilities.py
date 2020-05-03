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
            pass
        
        @staticmethod
        def find(xmltree: ET.Element) -> Dict[AnyStr, int]:
            pass

        def update(self, xmltree: ET.Element) -> None:
            pass
        

    class Constitution:
        def __init__(self, xmltree: ET.Element):
            pass
    
    class Dexterity:
        def __init__(self, xmltree: ET.Element):
            pass

    class Intelligence:
        def __init__(self, xmltree: ET.Element):
            pass

    class Strength:
        def __init__(self, xmltree: ET.Element):
            pass

    class Wisdom:
        def __init__(self, xmltree: ET.Element):
            pass