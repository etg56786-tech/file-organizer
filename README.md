### 📂 File Organizer
A cross-platform file organization utility written in Python that sorts files into categorized folders by extension.
Designed to be simple and easily customizable.
## ✅ Features
• Automatic organizational of files in category folders via an input of a directory name
• Sorting files by extension (Please see config.json for all categories)
• Customizable categories (configurable in "config.json")
• Automatic creation of category folders
• Safe rename of files with equal names (Duplicate handling)
• All operations are logged in "organizer.log"
• Runs on both macOS and Windows OS
• Pure Python implementation, no additional installs
## 📁 Project structure
file-organizer/
├── main.py # Runs the application
├── organizer.py # The main logic, functions
├── config.json # Categories and other configurations
├── organizer.log # Logs
└── README.md #This file right here
## 💡 How it works
1. The user selects the folder to organize
2. The utility scans the folder content
3. Each file has its extension is matched against categories
4. Category folders are created if not existing
5. The files are moved to their category folders
6. The equal file names are automatically renamed to prevent duplication errors
7. All operations are logged in "organizer.log"
## 📂 Example:
### Before
Downloads/
├── cat.jpg
├── report.pdf
├── music.mp3
├── code.py
└── notes.txt
### After
Downloads/
├── Images/
│   └── cat.jpg
├── Documents/
│   ├── report.pdf
│   └── notes.txt
├── Music/
│   └── music.mp3
├── Programs/
│   └── code.py
└── Videos/

## 🛠 Configuration
No changes to the source code are needed to change the categories, just edit the "config.json" file.
{
"extensions": {
"Images": [".png", ".jpg", ".jpeg"],
"Documents": [".pdf", ".docx", ".txt"],
"Music": [".mp3", ".wav"],
"Videos": [".mp4", ".mov"],
"Downloads": [".dmg", ".pkg"]
}
}
## 🧱 Technologies used
• Python 3
• pathlib
• shutil
• json
• logging

## 🖥 Motivation
I wanted to practice making a useful project which allowed me to dive deep into unfamiliar modules I have never used and getting familiar with them, as well as practicing software design patterns, working with the file system, applying configuration and developing project structure.

## Designed and Made in Visual Studio Code by Ethan Chen.