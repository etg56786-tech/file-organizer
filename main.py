import organizer
print(dir(organizer))
from pathlib import Path

def main():
    
    folder = input("Enter folder path: ")
    fold_name = Path.home() / folder
    organizer.scan_folder(fold_name)


if __name__ == "__main__":
    main()