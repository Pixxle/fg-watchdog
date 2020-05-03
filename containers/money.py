from __future__ import annotations
from dataclasses import dataclass
import xml.etree.ElementTree as ET
from typing import List, Dict, AnyStr
import logging


class Money:
    '''Class for keeping track of gold'''
    def __init__(self, xmltree:ET.Element) -> Money:
        
        money = self.find(xmltree)
        self.cp = money["cp"]
        self.sp = money["sp"]
        self.gp = money["gp"]

    def find(self, xmltree: ET.Element) -> Dict[AnyStr, int]:
        coins = xmltree.find("coins")

        # Quick return scenario if the player has no coins
        if coins is None:
            return { "cp" : 0, "sp" : 0, "gp" : 0 }
        
        money = {}
        for coin in coins.getchildren():
            if "slot" in coin.tag:
                amount = coin.find("amount").text if coin.find("amount") is not None else 0
                name = coin.find("name").text.lower() if coin.find("name") is not None else None
                
                if name is not None:
                    money[name] = int(amount)

        if not "cp" in money:
            money["cp"] = 0
        if not "sp" in money:
            money["sp"] = 0
        if not "gp" in money:
            money["gp"] = 0

        return money

    def update(self, owner:AnyStr, name:AnyStr, xmltree: ET.Element) -> None:
        logging.debug(f"Update gold: {name} -> Start")

        money = self.find(xmltree)

        if money["cp"] is not self.cp:
            logging.info(f"Updated copper for {name}, owned by {owner}, {self.cp} -> {money['cp']}")
            self.cp = money["cp"]
        if money["sp"] is not self.sp:
            logging.info(f"Updated silver: {name}, owned by {owner} , {self.sp} -> {money['sp']}")
            self.sp = money["sp"]
        if money["gp"] is not self.gp:
            logging.info(f"Updated gold: {name}, owned by {owner}, {self.gp} -> {money['gp']}")
            self.gp = money["gp"]


        logging.debug(f"Update gold: {name} -> Stop")
        