import organizer

from pathlib import Path

def main():
    
    folder = input("Enter folder path: ")
    fold_name = Path.home() / folder
    organizer.scan_folder(fold_name)


if __name__ == "__main__":
    try:
        main()
    except:
        print("Due to some technical difficulties, your input could not be run.")