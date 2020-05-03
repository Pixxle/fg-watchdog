from __future__ import annotations
from typing import List, Dict, AnyStr
import xml.etree.ElementTree as ET
from argparse import ArgumentParser
from pathlib import Path, PureWindowsPath
from time import sleep
import logging
import hashlib

from containers.characters import Character

DB = PureWindowsPath("C:\\Users\\denni\\AppData\\Roaming\\Fantasy Grounds\\campaigns\\The End of Time\\db.xml")

characters = {}
checksum = ""
running = True

def get_file_checksum(filepath: AnyStr) -> AnyStr:
    with open(filepath, "rb") as _f:
        return hashlib.md5(
            _f.read()
            ).hexdigest()

def update_characters():
    global checksum

    new_checksum = get_file_checksum(DB)
    if new_checksum == checksum:
        return

    checksum = new_checksum
    print(checksum)

    _f = open(DB, 'r')
    tree = ET.parse(_f)
    charactertree = tree.getroot().find("charsheet")
    for character in characters:
        characters[character].update(charactertree)
    _f.close()

def setup():
    global characters, checksum

    checksum = get_file_checksum(DB)
    print(checksum)

    _f = open(DB, 'r')
    tree = ET.parse(_f)
    charactertree = tree.getroot().find("charsheet")
    characters = Character.generate_characters_from_tree(charactertree)
    _f.close()


def configure_logging():
    FORMAT = '%(asctime)-15s %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)

if __name__ == "__main__":
    configure_logging()
    setup()

    logging.info("-" * 10)
    logging.info("Load successful, starting to log events:")
    while running:
        update_characters()
        sleep(60)