import xml.etree.ElementTree as ET
from argparse import ArgumentParser
from pathlib import Path, PureWindowsPath
import logging
from helpers.repeater import RepeatedTimer

from containers.characters import Character

DB = PureWindowsPath("C:\\Users\\denni\\AppData\\Roaming\\Fantasy Grounds\\campaigns\\The Weave\\db.xml")

repeaters = {}
characters = {}

def setup( interval: int = 10 ):
    tree = ET.parse(DB)
    charactertree = tree.getroot().find("charsheet")
    characters = Character.generate_characters_from_tree(charactertree)

    # Create update timer
    for character in characters:
        repeaters[character] = RepeatedTimer(
            interval, 
            characters[character].update, 
            ET.parse(DB).getroot().find("charsheet")
        )

def configure_logging():
    FORMAT = '%(asctime)-15s %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

if __name__ == "__main__":
    configure_logging()
    setup()