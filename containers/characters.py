from __future__ import annotations
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging
from dataclasses import dataclass

class Character:
    def __init__(self, attr: Dict[AnyStr, AnyStr], money: Dict[AnyStr, int]):
        self.attributes = Character.Attributes(
            name=attr["name"], 
            owner=attr["owner"],
            tag=attr["tag"]
        )
        self.money = Character.Money(
            cp = money["cp"],
            sp = money["sp"],
            gp = money["gp"]
        )

    @dataclass
    class Attributes:
        name: AnyStr
        owner: AnyStr
        tag: AnyStr

    @dataclass
    class Money:
        '''Class for keeping track of gold'''
        cp: int
        sp: int
        gp: int

        def set_gold(self, name: AnyStr, cp: int = None, sp: int = None, gp: int = None):
            if cp != None and cp != self.cp:
                logging.info(f"Updated copper: {name}, {self.cp} -> {cp}")
                self.cp = cp
            if sp != None and sp != self.sp:
                logging.info(f"Updated silver: {name}, {self.sp} -> {sp}")
                self.sp = sp
            if gp != None and gp != self.gp:
                logging.info(f"Updated gold: {name}, {self.sp} -> {sp}")

    @staticmethod
    def generate_characters_from_tree(xmltree: ET.Element) -> Dict[AnyStr, Character]:
        results = {}
        for _character in xmltree.getchildren():
            attributes = {
                "owner": _character.find("holder").tag,
                "name": _character.find("name").text,
                "tag": _character.tag
            }
            money = {}
            coins = _character.find("coins")
            for coin in coins.getchildren():
                if "slot" in coin.tag:
                    amount = coin.find("amount").text
                    name = coin.find("name")
                    if name is not None:
                        money[name.text.lower()] = int(amount)

            if money != {}:
                results[attributes["name"]] = Character(attributes, money)

        return results