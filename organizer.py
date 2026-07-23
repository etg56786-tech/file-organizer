import pathlib as p
import shutil as shut
import json
import logging

CONFIG_FILE = p.Path(__file__).parent / "config.json"
LOG_FILE = p.Path(__file__).parent / "organizer.log"
#hard links config.json to the variable, didnt know why it was showing FileNotFoundError.

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
) #configuration for logs, might move to config.json

logging.info("Initialized!")

with open(CONFIG_FILE) as file:
    config = json.load(file)

def scan_folder(folder_p):
    folder = p.Path(folder_p)

    if not folder.exists():
        print("The folder does not exist!")
        return

    for item in folder.iterdir():
        if item.is_dir():
            print(f"FOLDER: {item}")
            continue
            
        if item.is_file():
            
            category = categorize(item)

            category_folder = folder / category

            create_folder(category_folder)
            new = check_dupe(item, category_folder)
            move_file(item, new)
        

def categorize(file):
    extension = file.suffix.lower()

    for category, ex in config["extensions"].items():
        if extension in ex:
            return category
    return "Other"



def create_folder(folder):
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)

        logging.info(f"FOLDER CREATED: {folder}")

def move_file(file, destination):
    shut.move(file, destination)
    logging.info(f"MOVED {file} INTO {destination}")

def check_dupe(file, destination):
    counter = 1

    new_file = destination / file.name

    while new_file.exists():
        new_file = destination / f"{file.stem} ({counter}){file.suffix}"
        counter += 1
    
    return new_file

