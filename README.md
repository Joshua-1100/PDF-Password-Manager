# PDF-Password-Manager
A free, lightweight desktop tool for adding or removing passwords from PDF files — no cloud upload required. Built with Python and Tkinter.
   
________________________________________
Features
•	Add a password to one or more PDFs at the same time
•	Remove a password from one or more PDFs at the same time
•	Browse to any folder to select files — not limited to a single directory
•	Saves output files alongside the originals with a clear suffix (_protected / _unlocked)
•	Ressult log showing per-file success or failure
•	Show/hide password toggle
•	Runs 100% locally — your files never leave your machine
________________________________________
Screenshots
Launch the app and select file(s)
 
Add password to unprotected file(s). Click show password if desired.
Run
 
Results show is lower window.
 
The app preserves the original and creates a protected version.
 
Unlocking files is a similar process.
 
 
As with protecting files, unlocking preserves original files and makes copies.
 

________________________________________
Requirements
•	Python 3.8 or higher
•	pypdf
Tkinter is included with most standard Python installations.
________________________________________
Installation
1. Clone the repo
git clone https://github.com/Joshua-1100/PDF-Password-Manager
cd pdf-password-manager
2. Install the dependency
pip install pypdf
3. Run the app
python pdf_password_manager.py
________________________________________
Usage
1.	Choose Add password or Remove password
2.	Click Browse… to select one or more PDF files
3.	Enter the password
4.	Click Run
Output files are saved in the same folder as the originals:
Action	Input	Output
Protect	report.pdf	report_protected.pdf
Unlock	report_protected.pdf	report_protected_unlocked.pdf
________________________________________
Building a Standalone .exe (Windows)
If you want to share the tool without requiring Python to be installed:
pip install pyinstaller
pyinstaller --onefile --windowed pdf_password_manager.py
The .exe will appear in the dist/ folder.
________________________________________
Project Structure
pdf-password-manager/
├── pdf_password_manager.py   # Main application
├── README.md
└── LICENSE
________________________________________
Why This Project
I built this to solve a recurring need: quickly protecting or unlocking PDF files without uploading them to an online service where there could be a risk to private information. The original version was a command-line script limited to the working directory. This 2025-05-19 version adds a proper file browser GUI and batch processing so it works on files anywhere on your system.
Key things practiced:
•	File I/O and PDF manipulation with pypdf
•	Building a desktop GUI with tkinter and ttk
•	Error handling for real-world edge cases (wrong password, unencrypted file, etc.)
•	Packaging Python scripts as standalone executables with PyInstaller
________________________________________
License
MIT — free to use, modify, and distribute.
