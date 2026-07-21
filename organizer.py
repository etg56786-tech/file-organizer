import pathlib as p
import shutil as shut
extensions = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"]
}

def scan_folder(folder_p):
    folder = p.Path(folder_p)

    if not folder.exists():
        print("The folder does not exist!")
        return

    for item in folder.iterdir():
        if item.is_file():
            category = categorize(item)

            category_folder = folder / category

            create_folder(category_folder)
            move_file(item, category_folder)
        if item.is_dir():
            print(f"FOLDER: {item}")

def categorize(file):
    extension = file.suffix.lower()

    for category, ex in extensions.items():
        if extension in ex:
            return category
    return "Other"



def create_folder(folder):
    if folder.exists():
        folder.mkdir()

def move_file(file, destination):
    shut.move(file, destination)

def check_dupe(file, destination):
    if file.name in destination:
        print("Duplicate detected!")

