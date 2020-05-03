from __future__ import annotations
from dataclasses import dataclass
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging


@dataclass
class Money:
    '''Class for keeping track of gold'''
    cp: int
    sp: int
    gp: int


    @staticmethod
    def find(xmltree: ET.Element) -> Dict[AnyStr, int]:
        coins = xmltree.find("coins")

        # Quick return scenario if the player has no coins
        if coins == None:
            return { "cp" : 0, "sp" : 0, "gp" : 0 }
        
        money = {}
        for coin in coins.getchildren():
            if "slot" in coin.tag:
                amount = coin.find("amount").text
                name = coin.find("name")
                if name is not None:
                    money[name.text.lower()] = int(amount)

        if not "cp" in money:
            money["cp"] = 0
        if not "sp" in money:
            money["sp"] = 0
        if not "gp" in money:
            money["gp"] = 0

        return money

    def update_gold(self, name:AnyStr, xmltree: ET.Element) -> None:
        logging.debug(f"Update gold: {name} -> Start")

        money = self.find(xmltree)
        self.set_gold(
            name,
            cp= money["cp"],
            sp= money["sp"],
            gp= money["gp"]
        )

        logging.debug(f"Update gold: {name} -> Stop")

    def set_gold(self, name: AnyStr, cp: int = None, sp: int = None, gp: int = None):
        if cp is not None and cp is not self.cp:
            logging.info(f"Updated copper: {name}, {self.cp} -> {cp}")
            self.cp = cp
        if sp is not None and sp is not self.sp:
            logging.info(f"Updated silver: {name}, {self.sp} -> {sp}")
            self.sp = sp
        if gp is not None and gp is not self.gp:
            logging.info(f"Updated gold: {name}, {self.gp} -> {gp}")
            self.gp = gp
