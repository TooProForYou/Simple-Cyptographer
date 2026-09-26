# Simple-Cryptographer
This repo consists of a Python Cryptography Application (CLI, GUI, EXECUTABLE)
The program is solely built on python and serves as a way to encrypt and decrypt messages.

This project is a basic encryption and decryption toolkit that supports 10 classical historical ciphers. A total of 2 versions could be find in the files, one offers a Procedural Command-Line Interface and the other offers a polished, Object-Oriented Graphical User Interface. The final executable represents the best version of the app yet.

## Core Features
- **Extensive Cipher Library** - Support for [10 distinct ciphers](#supported-ciphers)
- **Dual Interfaces** - Includes both, lightweight, text-based `CLI` version for quick terminal operations and a fully - featured `GUI` version
- **Object-Oriented Architecture** - The GUI version utilizes an `OOP` design, completely separating translation layer and graphical elements for maximum code reusability
- **Dynamic User Interface** - GUI intelligently adapts to the selected cipher from the dropdown
- **Custom Theme** - The GUI is highly inspired by Atomic One Dark Pro featuring a `nightly` theme
- **Clipboard Integration** - The output can be copied and pasted by the help of buttons, integrated seamlessly inside the GUI
- **Cipher Stacking** - Users can manually pass the output of one encryption process into another cipher to layer their token
  
## Supported Ciphers
Both versions of the applications share the exact same content and capabilities, boasting time and space efficiencies `(mostly O(*n*) time complexity)`
All of the supported Ciphers are given below:
- **Caesar** : Classic Substitution cipher, great example of numeric shift
- **A1Z26** : Converts letter into corresponding alphabetical index
- **Atbash** : Reverses the alphabets
- **Baconian** : Encodes text into a 5 - character binary sequence of A and B
- **Beaufort** : A polyalphabetic substitution cipher requiring a key
- **Vigenère** : A polyalphabetic cipher using a key to shift characters
- **XOR** : A bitwise cipher converting text into hexadecimal format via secret keys
- **Scytale** : A transposition cipher requiring column diameter to wrap text
- **Rot13** : A fixed substitution cipher, shifting digits by 13 places
- **Morse Code** : Simple translation layer for alphanumeric to standard dots, dashes and slashes

## Technologies / Tools Used
- **Python 3.10+** : Core Programming Language
- **Tkinter** : Standard Python GUI toolkit used for creation of GUI and windows
- **Math Module** : Built-in Python Library used for column calculations in the Scytale Cipher
- **Pyinstaller** : Used to compile the final `.exe` application

*While designing the program, it was kept in mind to utilize minimum number of external modules and libraries so that most of the code consists of pure python and understanding the code could be easy*

## Steps to Install & Run the Project
### Prerequisites: 
Python 3.10+ via the official Python installer
### Running the Source Code
1. Clone or download the repository to your local machine
2. Open terminal and navigate to project directory
3. Both CLI and GUI versions could run through ide if the dependencies are installed *(All that is listed in tools used)*
### Running the Executable
GUI version of the program can be directly opened through the `.exe` file in the folder `dist` found inside the releases folder

## Instructions for Testing
1. Launch the application, either versions work, (GUI is recommanded)
2. Select a Cipher via dropdown or the list
3. Input Data in the input box or field
4. Configure Parameters as per the cipher; `key`, `diameter`, `shift` might be required in some ciphers
5. Choose between encryption or decryption and get the output

### Testing Decryption (Reversibility):
1. Copy Result in output block after encryption
2. Click Clear button or continue running the code in CLI version
3. Paste the result in the input box / field and decrypt it
4. Verify if the original string is restored in the output box

**Test Edge Cases:** Input numbers, special characters or empty strings, all of these could be tackled by the `run_safely` wrapper and alpha-checks. Any kind of crash can be tackled through the help of try and except blocks too.

# Screenshots
<img width="1318" height="1790" alt="#1-vtpj" src="https://github.com/user-attachments/assets/0c97ce68-1761-4c1d-adad-ccbe56e23428"/>
<img width="1157" height="788" alt="#2-vtpj" src="https://github.com/user-attachments/assets/7ac81c1a-b743-4366-b7c5-c1e3bcfefa14" />
<img width="1156" height="788" alt="#3-vtpj" src="https://github.com/user-attachments/assets/3028a1b7-abd2-4b44-84ee-bfa74ed5f083" />
<img width="1161" height="785" alt="#4-vtpj" src="https://github.com/user-attachments/assets/7bd8730f-3c49-4e3c-8de4-32ad94dcc122" />
