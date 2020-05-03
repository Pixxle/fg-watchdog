from __future__ import annotations
from typing import List, Dict, AnyStr
import xml.etree.ElementTree as ET
from argparse import ArgumentParser
from pathlib import Path, PureWindowsPath
from time import sleep
import logging
import hashlib
import os
import sys
import pprint

class Inventory:
    '''Class for keeping track of Inventory Items'''
    def __init__(self, xmltree: ET.Element) -> Inventory:
        self.items = self.find(xmltree)

    def find(self, xmltree: ET.Element) -> List[Dict[AnyStr, AnyStr]]:
        inventory = xmltree.find('inventorylist')
        items = []
        for item in inventory.getchildren():
            if "id-" in item.tag:
                _i = {
                    "tag": item.tag,
                    "carried":item.find('carried').text if item.find('carried') is not None else 0,
                    "cost":item.find('cost').text if item.find('cost') is not None else 0,
                    "count": item.find('count').text if item.find('count') is not None else 0,
                    "isidentified": item.find('isidentified').text if item.find('isidentified') is not None else 0,
                    "location" : item.find('location').text if item.find('location') is not None else "",
                    "locked": item.find('locked').text if item.find('locked') is not None else 0,
                    "name": item.find('name').text if item.find('name') is not None else "",
                    "subtype": item.find('subtype').text if item.find('subtype') is not None else "",
                    "type": item.find('type').text if item.find('type') is not None else "",
                    "weight": item.find('weight').text if item.find('weight') is not None else 0.00
                }
                items.append(_i)

        return items

    def update(self, owner:AnyStr, name:AnyStr, xmltree: ET.Element) -> None:
        items = self.find(xmltree)
        for _i in self.items:
            
            if _i["tag"] not in [x["tag"] for x in items]:
                logging.info(f"Update Item for {name}, owned by {owner}, {_i}")
                logging.info("{")
                for key in _i:
                    logging.info(f"{key}:{_i[key]},")
                logging.info("} -> Removed")
                continue

            new = next(x for x in items if x["tag"] == _i["tag"])
            if _i == new:
                continue

            logging.info(f"Update Item for {name}, owned by {owner}:")
            for key in _i:
                logging.info(f"{key}: {_i[key]} -> {new[key]}")

        for item in items:
            if item["tag"] not in [x["tag"] for x in self.items]:
                logging.info(f"Update Item for {name}, owned by {owner}:")
                logging.info("{")
                for key in _i:
                    logging.info(f"{key}: {item[key]},")
                logging.info("} -> Added")

        self.items = items
