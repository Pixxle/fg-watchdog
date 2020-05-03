from __future__ import annotations
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging
from dataclasses import dataclass

class Attributes:

    def __init__(self, xmltree: ET.Element) -> Attributes:
        attributes = self.find(xmltree)
        self.tag = xmltree.tag
        self.name = attributes["name"]
        self.owner = attributes["owner"]

    @staticmethod
    def find(xmltree: ET.Element) -> Dict[AnyStr, AnyStr]:
        owner = xmltree.find("holder")
        name = xmltree.find("name")

        attributes = {
                "owner": owner.attrib["name"] if owner is not None else "",
                "name": name.text if name is not None else ""
        }

        return attributes

    def update(self, xmltree: ET.Element) -> None:
        logging.debug(f"Update Attributes: {self.name} -> Start")

        attributes = self.find(xmltree)

        if attributes["owner"] != self.owner:
            logging.info(f"Update owner {self.name}: {self.owner} ->  {attributes['owner']}")
            self.owner = attributes["owner"]
        if attributes["name"] != self.name:
            logging.info(f"Update name: {self.name} -> {attributes['name']}")
            self.name = attributes["name"]

        logging.debug(f"Update Attributes: {self.name} -> Stop")