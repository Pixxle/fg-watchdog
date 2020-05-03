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
from containers.characters import Character


DB = None
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
    logging.debug(f"Update previous DB Checksum: {checksum}")
    logging.debug(f"Update current DB Checksum: {new_checksum}")

    if new_checksum == checksum:
        logging.debug("Update DB Checksum still the same, waiting for change...")
        return

    checksum = new_checksum

    _f = open(DB, 'r')
    tree = ET.parse(_f)
    charactertree = tree.getroot().find("charsheet")
    for character in characters:
        characters[character].update(charactertree)
    _f.close()

def setup():
    global characters, checksum

    checksum = get_file_checksum(DB)

    logging.debug(f"Setup DB Checksum: {checksum}")

    _f = open(DB, 'r')
    tree = ET.parse(_f)
    charactertree = tree.getroot().find("charsheet")
    characters = Character.generate_characters_from_tree(charactertree)
    _f.close()

def set_database(database_path: AnyStr = None) -> None:
    global DB
    
    if database_path is not None:
        DB = Path(database_path)
        return


    appdata = os.getenv('APPDATA')
    base = Path(appdata) / 'Fantasy Grounds' / 'campaigns'
    
    campagins = [x for x in base.iterdir() if x.is_dir()]
    
    if len(campagins) == 1:
        DB = Path(campagins[0]) / 'db.xml'
        return

    for num, campaign in enumerate(campagins):
        print(f"{num}: {campaign}")
    
    user_input = input("Multiple campaigns found, Please select which one to monitor:")
    DB = Path(campagins[int(user_input)]) / 'db.xml'

def read_configuration() -> ArgumentParser:

    argparse = ArgumentParser("Simple event logger for Fantasy grounds.")
    argparse.add_argument("--db", 
        dest="db",
        required=False, 
        help="Set custom location of Fantasy Grounds Database, Use this if DB is stored in non-default location")
    argparse.add_argument("-l", "--loglevel", 
        dest="loglevel", 
        choices=["INFO", "DEBUG"], 
        default="INFO",
        help="Apply loglevel")
    argparse.add_argument("-i", "--interval",
        dest="interval",
        default=60,
        type=int,
        help="Interval to check for changes in database"
    )
    argparse = argparse.parse_args()

    configure_logging(argparse.loglevel)
    set_database(argparse.db)
    return argparse
    
def configure_logging(loglevel: str) -> None:

    FORMAT = '%(asctime)-15s %(levelname)s: %(message)s'
    if loglevel == "INFO":
        logging.basicConfig(format=FORMAT, level=logging.INFO)
    else:
        logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    logging.debug("Logging configured")

if __name__ == "__main__":
    args = read_configuration()
    setup()

    logging.info("-" * 10)
    logging.info("Load successful, starting to log events:")
    while running:
        update_characters()
        sleep(args.interval)