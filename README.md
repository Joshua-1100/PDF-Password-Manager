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
<img width="681" height="427" alt="1_select_files" src="https://github.com/user-attachments/assets/56c1fab6-4648-4aa4-bcfe-dc7e154b303c" />
 
Add password to unprotected file(s). Click show password if desired.
Run
<img width="657" height="707" alt="2_addPassword" src="https://github.com/user-attachments/assets/369ad7b0-def4-4b55-a4b5-f677a6cf5a1f" />
Results show is lower window.
  <img width="512" height="172" alt="3_results" src="https://github.com/user-attachments/assets/29a65de9-5f62-4771-9695-aaf2c08a872a" />
The app preserves the original and creates a protected version.
<img width="342" height="205" alt="4_filePreservations" src="https://github.com/user-attachments/assets/ea8975a7-3e48-4b8b-8bdd-e4e0b6b3df46" />

Unlocking files is a similar process.
<img width="508" height="518" alt="5_unlockFiles" src="https://github.com/user-attachments/assets/2630da4c-61ff-4c67-bfcf-7f50a1a81b74" /> 
 
As with protecting files, unlocking preserves original files and makes copies.
<img width="432" height="155" alt="6_results" src="https://github.com/user-attachments/assets/6b6c6d7d-3ea1-4035-bd42-86d84a076a06" />
<img width="340" height="138" alt="7_unlockedPreserved" src="https://github.com/user-attachments/assets/e029d439-9813-4780-8cca-ba2c3ffa3d58" />

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
