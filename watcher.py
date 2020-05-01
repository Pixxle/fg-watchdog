import xml.etree.ElementTree as ET
from argparse import ArgumentParser
from pathlib import Path, PureWindowsPath
import logging

from containers.characters import Character

DB = PureWindowsPath("C:\\Users\\denni\\AppData\\Roaming\\Fantasy Grounds\\campaigns\\The Weave\\db.xml")

characters = None

def setup( ):
    tree = ET.parse(DB)
    charactertree = tree.getroot().find("charsheet")
    characters = Character.generate_characters_from_tree(charactertree)

    for key in characters:
        print(characters[key].attributes.name)
        print(characters[key].money.gp)
        print(characters[key].attributes.tag)

def update(interval: int = 10 ):
    pass

if __name__ == "__main__":
    setup()