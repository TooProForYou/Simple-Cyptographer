"""
_summary_
*GUI BY TKINTER AND LUNA*
This code contains the code for encryption and decryption support for the following Cyphers
1. Caesar
​2. A1z26
3. Atbash
4. Baconian (Unique Values)
5. Beaufort
6. Vigenere
7. Xor
8. Skytale
9. rot13
10. Morse Code

`-` Cypher Stack Support -> Just Stack it via common sense
`-` OOPS -> Object Oriented Programming is done in this code so that the code can be reusable
`-` Efficient -> Time complexity is less and space complexity is also less (usually O(n) or O(n^2))
"""

import math
import tkinter as tk
from tkinter import ttk


class Cipher:
    #Base class for all ciphers
    def read_text(self, prompt="Enter Plain Text: "):
        return input(prompt)
        
    def read_int(self, prompt="Enter Shift: "):
        return int(input(prompt))
        
    def read_bool(self, prompt="Encrypt -> True / Decrypt -> False: "):
        return input(prompt).strip().lower() == "true"
        
    def read_key(self, prompt="Enter Key: "):
        return input(prompt).upper()
        
    def read_diameter(self, prompt="Enter Diameter: "):
        return int(input(prompt))


class CaesarCipher(Cipher):
    #defining the text-box, encryption / decryption, key or diameters 
    def run(self):
        print("-------------------------CaesarCipher------------------------")
        
        text = self.read_text()
        shift = self.read_int()
        encrypt = self.read_bool()
        return process_translation("caesar", text, encrypt, shift=shift)


class A1Z26Cipher(Cipher):
    def run(self):
        print("-------------------------A1Z26 Cipher------------------------")
        
        text = self.read_text()
        encrypt = self.read_bool()
        return process_translation("a1z26", text, encrypt)


class AtbashCipher(Cipher):
    def run(self):
        print("----------------------AtBash Cipher--------------------------")
        
        text = self.read_text()
        self.read_bool()  # Keeps interface parity with original script
        return process_translation("atbash", text)


class BaconianCipher(Cipher):
    def run(self):
        print("-----------------------Baconian Cipher-------------------------")
        
        text = self.read_text()
        encrypt = self.read_bool()
        return process_translation("baconian", text, encrypt)


class BeaufortCipher(Cipher):
    def run(self):
        
        text = self.read_text()
        key = self.read_key()
        encrypt = self.read_bool()
        return process_translation("beaufort", text, encrypt, key)


class VigenereCipher(Cipher):
    def run(self):
        
        text = self.read_text()
        key = self.read_key()
        encrypt = self.read_bool()
        return process_translation("vigenere", text, encrypt, key)


class XORCipher(Cipher):
    def run(self):
        
        text = self.read_text()
        key = input("Enter Key: ")
        encrypt = self.read_bool()
        return process_translation("xor", text, encrypt, key)


class ScytaleCipher(Cipher):
    def run(self):
        
        text = self.read_text()
        diameter = self.read_diameter()
        encrypt = self.read_bool()
        return process_translation("scytale", text, encrypt, diameter=diameter)


class Rot13Cipher(Cipher):
    def run(self):
        
        text = self.read_text()
        self.read_bool()
        return process_translation("rot13", text)


class MorseCipher(Cipher):
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'
    }
    
    def run(self):
        text = self.read_text()
        encrypt = self.read_bool()
        return process_translation("morse", text, encrypt)

#Function wrappers (oops)
def caesar(): return CaesarCipher().run()
def a1z26(): return A1Z26Cipher().run()
def atbash(): return AtbashCipher().run()
def baconian(): return BaconianCipher().run()
def beaufort(): return BeaufortCipher().run()
def vigenere(): return VigenereCipher().run()
def xor(): return XORCipher().run()
def scytale(): return ScytaleCipher().run()
def rot13(): return Rot13Cipher().run()
def morse(): return MorseCipher().run()

#Main Logic
def process_caesar_text(text, shift, encrypt):
    #defining shift for decrypting
    if not encrypt:
        shift = -shift
    #result's placeholder
    result = []
    
    for char in text:
        if char.isalpha():
            #converting to unicode for processing charachters
            ascii_offset = ord('A') if char.isupper() else ord('a')
            #identifying the char and then take the modulo with 26 to be in range
            result.append(chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset))
        else:
            result.append(char)
    
    return "".join(result)


def process_a1z26_text(text, encrypt):
    if encrypt:
        words = text.upper().split(" ")
        encrypted_words = []
        
        for word in words:
            converted_chars = []
            for char in word:
                if char.isalpha():
                    #making the numbers translate asper - a->1 , b-> 2, c-> 3, d-> 4, ..., y-> 25, z-> 26
                    char_num = ord(char) - ord('A') + 1
                    converted_chars.append(str(char_num))
            
            if converted_chars:
                encrypted_words.append('-'.join(converted_chars))
        
        return "/".join(encrypted_words)

    #decrypting stuff
    words = text.split('/')
    decrypted_words = []
    
    for word in words:
        numbers = word.strip().split("-")
        converted_chars = []
        for num in numbers:
            if num.isdigit():
                #run it back
                converted_chars.append(chr(int(num) + ord('A') - 1))
        
        decrypted_words.append("".join(converted_chars))
    return " ".join(decrypted_words)


def process_atbash_text(text):
    #atbash dictionary consists of all charachters from a to z being equated inversely
    #asper - a->z, b->y, c->x, ... , y->b, z->a
    atbash_dictionary = {chr(65 + i): chr(90 - i) for i in range(26)}
    result = []
    
    for char in text:
        if char.upper() in atbash_dictionary:
            swapped_char = atbash_dictionary[char.upper()]
            result.append(swapped_char if char.isupper() else swapped_char.lower())
        else:
            result.append(char)
    return "".join(result)


def process_baconian_text(text, encrypt):
    #baconian cipher typically converts the text into binary encoding 
    #but 0's are replaced with A and 1's are replaced with B
    baconian_dictionary = {
        chr(65 + i): format(i, '05b').replace('0', 'A').replace('1', 'B')
        for i in range(26)
    }
    #reversing dictionary in order to decrpyt stuff
    reversed_baconian_dictionary = {v: k for k, v in baconian_dictionary.items()}

    if encrypt:
        encoded = []
        for char in text.upper():
            if char in baconian_dictionary:
                encoded.append(baconian_dictionary[char])
            elif char == " ":
                encoded.append("/")
            else:
                raise ValueError("Baconian cipher only supports letters and spaces")
        
        return " ".join(encoded)

    pieces = text.upper().split(" ")
    decoded = []
    
    for piece in pieces:
        #letting the loop skip the particular index
        if not piece:
            continue
        #reverse translation layer
        if piece in reversed_baconian_dictionary:
            decoded.append(reversed_baconian_dictionary[piece])
        #spacing
        elif piece == "/":
            decoded.append(" ")
        else:
            raise ValueError("Invalid Baconian Text; Use 5 A / B characters")
    return "".join(decoded).capitalize()


def process_beaufort_text(text, key, encrypt):
    if not text:
        return ""
    if not key:
        raise ValueError("A key is required for Beaufort Cipher to Function")

    key = key.upper()
    result = []
    key_index = 0
    
    for char in text:
        if char.isalpha():
            #calculating unicode
            start_ascii = ord('A') if char.isupper() else ord('a')
            #key characters
            key_char = key[key_index % len(key)]
            key_val = ord(key_char) - ord('A')
            #char value
            text_val = ord(char) - start_ascii
            cipher_val = (key_val - text_val) % 26
            #final cipher value
            cipher_char = chr(cipher_val + ord('A'))
            result.append(cipher_char if char.isupper() else cipher_char.lower())
            
            key_index += 1
        #leave the spaces and symbols unbothered
        else:
            result.append(char)
    
    return "".join(result)


def process_vigenere_text(text, key, encrypt):
    if not key:
        raise ValueError("A key is required for Vigenere Cipher to Function")
    
    key = key.upper()
    result = []
    key_index = 0
    
    for char in text:
        if char.isalpha():
            #calculating unicode
            start_ascii = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % len(key)]
            shift_val = ord(key_char) - ord('A')
            
            #calculating shift for decryption
            if not encrypt:
                shift_val = -shift_val
            
            result.append(chr((ord(char) - start_ascii + shift_val) % 26 + start_ascii))
            key_index += 1
        else:
            result.append(char)
    
    return "".join(result)


def process_xor_text(text, key, encrypt):
    if not key:
        raise ValueError("A key is required for XOR Cipher to Function")
    
    if encrypt:
        #converting text to hex via xor
        hex_output = []
        for i, char in enumerate(text):
            #finding key char value
            key_char = key[i % len(key)]
            #applying xor operation
            xor_result = ord(char) ^ ord(key_char)
            hex_output.append(f"{xor_result:02x}")
        return "".join(hex_output)

    decoded = []
    byte_list = [text[i:i + 2] for i in range(0, len(text), 2)]
    
    for i, hex_val in enumerate(byte_list):
        #finding key char value
        key_char = key[i % len(key)]
        #run it back
        cipher_val = int(hex_val, 16)
        #applying xor operation
        original_val = cipher_val ^ ord(key_char)
        decoded.append(chr(original_val))
    return "".join(decoded)


def process_scytale_text(text, diameter, encrypt):
    import math #for math.ceil in column calculations 
    
    if diameter <= 1:
        return text
    
    if encrypt:
        #number of columns
        num_cols = math.ceil(len(text) / diameter)
        #pad text as per the cipher's rules
        padded_text = text.ljust(diameter * num_cols)
        encoded = []
        #sm shitty loop
        for col in range(num_cols):
            for row in range(diameter):
                index = row * num_cols + col
                encoded.append(padded_text[index])
        return "".join(encoded)

    num_cols = math.ceil(len(text) / diameter)
    result = [None] * len(text)
    current_idx = 0
    #run it back
    for col in range(num_cols):
        for row in range(diameter):
            index = row * num_cols + col
            
            if current_idx < len(text):
                result[index] = text[current_idx]
                current_idx += 1
    
    return "".join(filter(None, result)).rstrip()


def process_rot13_text(text):
    #simple af cipher
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    
    #shift by 13
    shifted_lower = lower_alpha[13:] + lower_alpha[:13]
    shifted_upper = shifted_lower.upper()
    
    #translation layer
    trans_table = str.maketrans(lower_alpha + upper_alpha, shifted_lower + shifted_upper)
    return text.translate(trans_table)


def process_morse_text(text, encrypt):
    morse_dict = MorseCipher.MORSE_CODE_DICT
    #connecting morse dictionary
    if encrypt:
        mapping = {key: val + ' ' for key, val in morse_dict.items()}
        mapping[' '] = '/ '
        trans_table = str.maketrans(mapping)
        return text.upper().translate(trans_table).strip()

    reversed_morse_dict = {val: key for key, val in morse_dict.items()}
    reversed_morse_dict['/'] = ' '
    result = []
    
    for token in text.split(' '):
        if token in reversed_morse_dict:
            result.append(reversed_morse_dict[token])
    
    return ''.join(result)


def process_translation(cipher_name, text, encrypt=True, key="", shift=0, diameter=1):
    name = cipher_name.strip().lower()
    #for outputs, we've made a whole translation function for better readability

    if "caesar" in name: return process_caesar_text(text, shift, encrypt)
    if "a1z26" in name or "a1z" in name: return process_a1z26_text(text, encrypt)
    if "atbash" in name: return process_atbash_text(text)
    if "baconian" in name: return process_baconian_text(text, encrypt)
    if "beaufort" in name: return process_beaufort_text(text, key, encrypt)
    if "vigenere" in name: return process_vigenere_text(text, key, encrypt)
    if "xor" in name: return process_xor_text(text, key, encrypt)
    if "scytale" in name: return process_scytale_text(text, diameter, encrypt)
    if "rot13" in name: return process_rot13_text(text)
    if "morse" in name: return process_morse_text(text, encrypt)

    raise ValueError(f"Unable to trace the cipher: {cipher_name}")


"""
PROPER GUI VIA TKINTER AND LUNA
"""
class CipherNightGUI:

    def __init__(self, root=None):
        #says for itself
        self.root = root if root is not None else tk.Tk()
        self.root.title("Simple Cryptographer V3")
        #size of window 
        self.root.geometry("930x640")
        self.root.minsize(820, 560)
        #ui defining
        self._configure_theme()
        self._build_ui()
        #exit fullscreen
        self.root.bind("<Escape>", self._exit_fullscreen)

    def _configure_theme(self):
        #color schemes (actually used the nightly beige pallet from the atomic one dark pro theme)
        #pretty coppied ngl
        #body
        self.bg = "#08111f"
        self.panel = "#121d2e"
        self.widget = "#1c2a3e"
        #primary
        self.primary = "#7c5cff"
        self.accent = "#4dd0ff"
        #text
        self.text = "#eaf2ff"
        self.muted = "#9ab0d0"
        #extra
        self.success = "#7ef7c6"
        self.error = "#ff7d7d"
        self.root.configure(bg=self.bg)

        try:
            style = ttk.Style(self.root)
            #theme
            style.theme_use("clam")

            style.configure("TFrame", background=self.bg)
            style.configure("TLabel", background=self.bg, foreground=self.text, font=("Segoe UI", 10))
            
            style.configure("TCombobox", fieldbackground=self.widget, background=self.widget, foreground=self.text)
            style.map("TCombobox", fieldbackground=[("readonly", self.widget)], foreground=[("readonly", self.text)])

            style.configure("TButton", background=self.primary, foreground=self.text, borderwidth=0, padding=(14, 8), font=("Segoe UI", 10, "bold"))
            style.map("TButton", background=[("active", self.accent)], foreground=[("active", self.bg)])
            
            style.configure("Clear.TButton", background=self.widget, foreground=self.muted, borderwidth=0, padding=(3, 1), font=("Segoe UI", 9, "bold"))
            style.map("Clear.TButton", background=[("active", self.primary)], foreground=[("active", self.text)])
            
            style.configure("Footer.TLabel", background=self.bg, foreground="#9aa8bb", font=("Segoe UI", 9))
            style.configure("TEntry", fieldbackground=self.widget, foreground=self.text)
            style.configure("TCheckbutton", background=self.bg, foreground=self.text)
        
        except tk.TclError:
            pass

    def _build_ui(self):

        class RoundedScrollbar(tk.Canvas):
            def __init__(self, master, command):
                super().__init__(master, width=14, bg="#050505", highlightthickness=0, bd=0)
                self.command = command
                self.first = 0.0
                self.last = 1.0
                self.thumb_top = 0
                self.thumb_bottom = 0
                self.drag_offset = 0
                self.hovered = False

                self.bind("<Configure>", lambda event: self._draw())
                self.bind("<Button-1>", self._start_drag)
                self.bind("<B1-Motion>", self._drag)
                self.bind("<MouseWheel>", self._on_mousewheel)
                self.bind("<Enter>", self._on_enter)
                self.bind("<Leave>", self._on_leave)

            def set(self, first, last):
                self.first = float(first)
                self.last = float(last)
                self._draw()

            def _pill(self, left, top, right, bottom, color):
                radius = (right - left) / 2
                self.create_oval(left, top, right, top + 2 * radius, fill=color, outline=color)
                self.create_rectangle(left, top + radius, right, bottom - radius, fill=color, outline=color)
                self.create_oval(left, bottom - 2 * radius, right, bottom, fill=color, outline=color)

            def _draw(self):
                self.delete("all")
                height = self.winfo_height()
                if height <= 1:
                    return

                track_top = 4
                track_bottom = max(track_top + 1, height - 4)
                self._pill(4, track_top, 10, track_bottom, "#171717")

                track_height = track_bottom - track_top
                thumb_height = min(track_height, max(24, int((self.last - self.first) * track_height)))

                self.thumb_top = min(track_top + int(self.first * track_height), track_bottom - thumb_height)
                self.thumb_bottom = self.thumb_top + thumb_height

                color = "#777777" if self.hovered else "#505050"
                self._pill(3, self.thumb_top, 11, self.thumb_bottom, color)

            def _start_drag(self, event):
                if self.thumb_top <= event.y <= self.thumb_bottom:
                    self.drag_offset = event.y - self.thumb_top
                else:
                    self.drag_offset = (self.thumb_bottom - self.thumb_top) / 2
                self._drag(event)

            def _drag(self, event):
                track_top = 4
                track_bottom = max(track_top + 1, self.winfo_height() - 4)
                travel = track_bottom - track_top - (self.thumb_bottom - self.thumb_top)

                if travel <= 0:
                    return

                thumb_top = min(max(event.y - self.drag_offset, track_top), track_top + travel)
                scrollable_fraction = max(0.0, 1.0 - (self.last - self.first))
                fraction = (thumb_top - track_top) / travel * scrollable_fraction
                self.command("moveto", fraction)

            def _on_mousewheel(self, event):
                self.command("scroll", -1 if event.delta > 0 else 1, "units")
                return "break"

            def _on_enter(self, event):
                self.hovered = True
                self._draw()

            def _on_leave(self, event):
                self.hovered = False
                self._draw()


        main = ttk.Frame(self.root, padding=18)
        main.pack(fill="both", expand=True)

        header = ttk.Frame(main)
        header.pack(fill="x", pady=(0, 12))

        title = ttk.Label(header, text="Simple Cryptographer", font=("Segoe UI", 22, "bold"))
        title.pack(side="left", anchor="w")

        self.fullscreen_btn = ttk.Button(header, text="⛶", width=3, style="Clear.TButton", command=self._toggle_fullscreen)
        self.fullscreen_btn.pack(side="right", anchor="ne")

        toolbar = ttk.Frame(main)
        toolbar.pack(fill="x", pady=(0, 14))

        ttk.Label(toolbar, text="Cipher").pack(side="left", padx=(0, 8))

        self.cipher_var = tk.StringVar(value="Caesar Cipher")
        cipher_box = ttk.Combobox(toolbar, textvariable=self.cipher_var, values=[
            "Caesar Cipher",
            "A1Z26 Cipher",
            "Atbash Cipher",
            "Baconian Cipher",
            "Beaufort Cipher",
            "Vigenere Cipher",
            "XOR Cipher",
            "Scytale Cipher",
            "ROT13 Cipher",
            "Morse Cipher",
        ], width=18, state="readonly")

        cipher_box.pack(side="left", padx=(0, 16))
        cipher_box.bind("<<ComboboxSelected>>", self._update_parameter_fields)

        form = ttk.Frame(main)
        form.pack(fill="x", pady=(0, 10))

        self.shift_label = ttk.Label(form, text="Shift")
        self.shift_label.grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 10))

        self.shift_entry = ttk.Entry(form, width=16)
        self.shift_entry.insert(0, "3")
        self.shift_entry.grid(row=0, column=1, sticky="w", padx=(0, 18), pady=(0, 10))

        self.key_label = ttk.Label(form, text="Key")
        self.key_label.grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 10))

        self.key_entry = ttk.Entry(form, width=22)
        self.key_entry.grid(row=0, column=1, sticky="w", padx=(0, 18), pady=(0, 10))

        self.diameter_label = ttk.Label(form, text="Diameter")
        self.diameter_label.grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 10))

        self.diameter_entry = ttk.Entry(form, width=12)
        self.diameter_entry.insert(0, "3")
        self.diameter_entry.grid(row=0, column=1, sticky="w", padx=(0, 18), pady=(0, 10))

        self._update_parameter_fields()

        text_area = ttk.Frame(main)
        text_area.pack(fill="both", expand=True)

        text_area.columnconfigure(0, weight=1)

        text_area.rowconfigure(1, weight=1, uniform="text_boxes")
        text_area.rowconfigure(4, weight=1, uniform="text_boxes")

        ttk.Label(text_area, text="Input").grid(row=0, column=0, sticky="w")

        input_frame = ttk.Frame(text_area)
        input_frame.grid(row=1, column=0, sticky="nsew", pady=(6, 12))

        self.input_box = tk.Text(input_frame, height=10, bg=self.widget, fg=self.text, insertbackground=self.text, relief="flat", borderwidth=0)

        input_scrollbar = RoundedScrollbar(input_frame, self.input_box.yview)

        self.input_box.configure(yscrollcommand=input_scrollbar.set)
        self.input_box.pack(side="left", fill="both", expand=True)

        input_scrollbar.pack(side="right", fill="y")

        self.input_box.insert("1.0", "HELLO WORLD")
        self.clear_input_btn = ttk.Button(input_frame, text="×", width=2, style="Clear.TButton", command=self.clear_input)
        self.clear_input_btn.place(relx=1.0, x=-22, y=6, anchor="ne")

        btn_row = ttk.Frame(text_area)
        btn_row.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        self.encrypt_btn = ttk.Button(btn_row, text="Encrypt", command=lambda: self.transform(True))
        self.encrypt_btn.pack(side="left")

        self.decrypt_btn = ttk.Button(btn_row, text="Decrypt", command=lambda: self.transform(False))
        self.decrypt_btn.pack(side="left", padx=(10, 0))

        self.copy_btn = ttk.Button(btn_row, text="Copy Result", command=self.copy_result)
        self.copy_btn.pack(side="left", padx=(10, 0))

        self.paste_btn = ttk.Button(btn_row, text="Paste Result", command=self.paste_result)
        self.paste_btn.pack(side="left", padx=(10, 0))

        ttk.Label(text_area, text="Output").grid(row=3, column=0, sticky="w")

        output_frame = ttk.Frame(text_area)
        output_frame.grid(row=4, column=0, sticky="nsew", pady=(6, 12))

        self.output_box = tk.Text(output_frame, height=10, bg="#0d1726", fg=self.success, insertbackground=self.success, relief="flat", borderwidth=0)

        output_scrollbar = RoundedScrollbar(output_frame, self.output_box.yview)

        self.output_box.configure(yscrollcommand=output_scrollbar.set)
        self.output_box.pack(side="left", fill="both", expand=True)

        output_scrollbar.pack(side="right", fill="y")
        
        ttk.Label(text_area, text="All rights reserved, Shreyansh Mishra (26BCE10245)", style="Footer.TLabel", anchor="center").grid(row=5, column=0, sticky="ew", pady=(8, 0))


    def _toggle_fullscreen(self):
        fullscreen = not bool(self.root.attributes("-fullscreen"))
        self.root.attributes("-fullscreen", fullscreen)


    def _exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)
        return "break"


    def _update_parameter_fields(self, event=None):
        cipher = self.cipher_var.get().lower()
        
        required_fields = {
            "shift": "caesar" in cipher,
            "key": any(name in cipher for name in ("beaufort", "vigenere", "xor")),
            "diameter": "scytale" in cipher
        }

        for name, required in required_fields.items():
            label = getattr(self, f"{name}_label")
            entry = getattr(self, f"{name}_entry")
        
            if required:
                label.grid()
                entry.grid()
            else:
                label.grid_remove()
                entry.grid_remove()


    def transform(self, encrypt):
        text = self.input_box.get("1.0", "end").strip()
        cipher = self.cipher_var.get()

        try:
            shift = int(self.shift_entry.get() or 0)
        except ValueError:
            shift = 0

        try:
            diameter = int(self.diameter_entry.get() or 1)
        except ValueError:
            diameter = 1

        try:
            result = process_translation(cipher, text, encrypt, self.key_entry.get(), shift, diameter)
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", result)
        except Exception as exc:
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", f"Error: {exc}")


    def copy_result(self):
        result = self.output_box.get("1.0", "end").strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(result)
        self.root.update()


    def paste_result(self):
        try:
            clipboard_text = self.root.clipboard_get()
        except tk.TclError:
            return

        self.input_box.insert("insert", clipboard_text)


    def clear_input(self):
        self.input_box.delete("1.0", "end")

"""Runtime disguised in a function"""
def main():
    try:        
        root = tk.Tk()
        app = CipherNightGUI(root)
        root.mainloop()
    except tk.TclError:
        print("Tkinter is not available in this environment.")

if __name__ == "__main__":
    main()