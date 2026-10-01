## Problem Statement
In the realm of cryptography education and hobbyist code-breaking, individuals often rely on fragmented, ad-laden, or online-only web tools to explore and manipulate historical ciphers. There is a notable lack of cohesive, privacy-respecting, and offline-capable applications that consolidate multiple classic encryption methods into a single, user-friendly interface. Furthermore, students studying computer science or introductory cryptography often struggle to find clear, accessible, and object-oriented implementations of these algorithms to study, experiment with, and execute locally.

## Scope of Project
The scope of `Simple Cryptographer` encompasses the design, development and deployment of a local python application that performs bidirectional text translations for 10 classical ciphers.
The project includes two type of versions,  where one consists of a command-line-interface design and other offers a fully functional graphical user interface.

The project is strictly limited to classic, text-based cryptographic algorithms for most of the ciphers, operating on the time complexity `O(n)`
The scope excludes modern encryption standards such as AES, RSA, SHA, Network based communication, file-level-data encryption or sharing features.
Final deliverable includes a `.exe` file ensuring frictionless deployment for end-users without requiring pre-configured Python IDE or environments

## Target Users
- **Educational Institutions** : Individuals studying cryptography, computer science or algorithm design require a reliable tool offline. This program could act as so.
- **Cipher Enthusiasts** - People who frequently need to rapidly encrypt and decrypt clues using various hystorical methods or just hide a piece of information with themselves.
- **Software Developers** - Python devs looking for reference architecture demonstrating effective transition a functional script into scalable GUI application using Tkinter and LUNA and custom widget theming.

## High-Level Features
- **Unified Cryptographic Engine:**  Bidirectional support (encryption and decryption) for 10 distinct ciphers, including Caesar, A1Z26, Atbash, Baconian, Beaufort, Vigenère, XOR, Scytale, ROT13, and Morse Code.
- **Dynamic Graphical Interface:** A responsive, custom-themed GUI that automatically adapts its input parameters—intelligently prompting for specialized inputs like "Keys", numerical "Shifts", or rod "Diameters" based strictly on the selected cipher algorithm.
- **Scalable OOP Architecture:** A modular, class-based codebase that separates UI rendering from mathematical processing, allowing developers to easily integrate future algorithms by simply inheriting from the base `Cipher` class.
- **Frictionless User Experience:** Built-in clipboard management (Copy/Paste Result functionality) and dedicated input-clearing mechanics to facilitate rapid, iterative cipher stacking (running encrypted text through multiple different ciphers sequentially).
- **Zero-Dependency Deployment:** Packaged as a standalone executable to provide immediate, out-of-the-box functionality for Windows environments without requiring users to install Python or external libraries.
