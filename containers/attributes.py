from __future__ import annotations
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging
from dataclasses import dataclass

@dataclass
class Attributes:
    name: AnyStr
    owner: AnyStr
    tag: AnyStr

    @staticmethod
    def find(xmltree: ET.Element) -> Dict[AnyStr, AnyStr]:
        owner = xmltree.find("holder")
        name = xmltree.find("name")

        attributes = {
                "owner": owner.attrib["name"] if owner is not None else "",
                "name": name.text if name is not None else ""
        }

        return attributes


    def update_attributes(self, xmltree: ET.Element) -> None:
        logging.debug(f"Update Attributes: {self.name} -> Start")

        owner = xmltree.find("holder")
        name = xmltree.find("name")

        self.set_attributes(
            owner.attrib["name"] if owner is not None else "",
            name.text if name is not None else ""
        )

        logging.debug(f"Update Attributes: {self.name} -> Stop")

    
    def set_attributes(self, owner:AnyStr, name:AnyStr):
        if owner is not self.owner:
            logging.info(f"Update owner {self.name}: {self.owner} ->  {owner}")
            self.owner = owner
        if name is not self.name:
            logging.info(f"Update name: {self.name} -> {name}")
            self.name = name
