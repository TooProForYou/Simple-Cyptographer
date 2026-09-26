"""
    _summary_
    *NO GUI UP TILL NOW*
    This code contains the code for encryption and decryption support for the following Cyphers
    1. Caesar
    2. A1z26
    3. Atbash
    4. Baconian (Unique Values)
    5. Beaufort
    6. Vigenere
    7. Xor
    8. Skytale
    9. rot13
    10. Morse Code

    `-` Cypher Stack Support -> Just Stack it via common sense
    `-` Efficient -> Time complexity is less and space complexity is also less (usually O(n) or o(logn))
"""

def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def read_mode():
    while True:
        answer = input("Encrypt or decrypt? (true/false): ").strip().lower()
        if answer in ("true", "t", "yes", "y", "encrypt", "e"):
            return True
        if answer in ("false", "f", "no", "n", "decrypt", "d"):
            return False
        print("Please enter true/encrypt or false/decrypt.")


def run_safely(cipher_function):
    try:
        print(cipher_function())
    except (ValueError, ZeroDivisionError, OverflowError, IndexError) as error:
        print(f"Invalid cipher input: {error}")


choice = False
while True:
    print("-------------------------------------------------------------")
    if choice == True:
        choice = input("Type 'quit' to quit press enter to continue: ")
    if choice == "quit":
        break
    choice = True
    print("Available Ciphers:\n1 - Caesar\n2 - A1z26\n3 - Atbash\n4 - Baconian (Unique Values)\n5 - Beaufort\n6 - Vigenere\n7 - Xor\n8 - Skytale\n9 - rot13\n10 - Morse Code")
    c = read_integer("Select a Cipher (1-10): ")
    if not 1 <= c <= 10:
        print("Choose a cipher number from 1 to 10.")
        continue

    match(c):
        case 1:
            def caesar():
                print("-------------------------CaesarCipher------------------------")
                text=input("Enter Plain Text: ")
                shift = read_integer("Enter Shift: ")
                encrypt = read_mode()
                if not encrypt:
                    shift = -shift
                result = ""
                for x in text:
                    if x.isalpha():
                        #defining the charachter boundry
                        original = ord('A') if x.isupper() else ord('a')
                        #shifting the charachter within it's boundry as per the (0,25) range
                        result += chr((ord(x) - original + shift) % 26 + original)
                    else:
                        result += x
                return f"Output: {result}"
            run_safely(caesar)
        
        case 2:
            def a1z26():
                print("-------------------------A1Z26 Cipher------------------------")
                text=input("Enter Plain Text: ")
                encrypt = read_mode()
                if encrypt:
                    words = text.upper().split(" ")
                    encrypted_words = []
                    
                    for word in words:
                        converted_letters = []
                        for x in word:    
                            if x.isalpha():
                            #convert every letter into a number a->1 , b-> 2, ...., z->26
                                n = ord(x) - ord('A') + 1
                                converted_letters.append(str(n))
                            #string datatype is used since we need to join them via dashes and even seperate them after
                        if converted_letters:
                            encrypted_words.append('-'.join(converted_letters))
                    #join words with slashes for readability
                    return "/".join(encrypted_words)
                
                else:
                    words = text.split('/')
                    decrypted_words = []
                    
                    for x in words:
                        #isolate the input for conducting operations
                        numbers = x.strip().split("-")
                        converted_letters = ""
                        for i in numbers:
                            if i.isdigit():
                                #convert number into unicode and then into a charachter
                                converted_letters += chr(int(i) + ord('A') - 1)                 
                        decrypted_words.append(converted_letters)
                    return " ".join(decrypted_words)
            run_safely(a1z26)

        case 3:
            def atbash():
                print("----------------------AtBash Cipher--------------------------")
                #atbash dict is defined
                atbash_dictionary = {chr(65 + i): chr(90 - i) for i in range(26)}
                result = []
                text=input("Enter Plain Text: ")
                encrypt = read_mode()
                    
                for x in text:
                    if x.upper() in atbash_dictionary:
                        #swap contains the encoded/decoded text from the message
                        swap = atbash_dictionary[x.upper()]
                        result.append(swap if x.isupper() else swap.lower())
                    else:
                        #leave symbols, spaces, and numbers unaffected
                        result.append(x)
                return "".join(result)
            run_safely(atbash)

        case 4:
            def baconian():
                #baconian dictionary (typically A -> 0 b -> 1 is encoded in base 5)
                #05b converts it into binary, via formatting we've swapped 0 with A and 1 with B
                print("-----------------------Baconian Cipher-------------------------")
                baconian_dictionary = {chr(65 + i): format(i, '05b').replace('0', 'A').replace('1', 'B')  for i in range(26)}
                reversed_baconian_dictionary = {v: k for k, v in baconian_dictionary.items()}
                text=input("Enter Plain Text: ")
                encrypt = read_mode()
                if encrypt:
                    encoded=[]
                    for x in text.upper():
                        if x in baconian_dictionary:
                            encoded.append(baconian_dictionary[x])
                        elif x == " ":
                            encoded.append("/")
                        else:
                            raise ValueError("Baconian cipher only supports letters and spaces")
                    return " ".join(encoded)
                else:
                    piece = text.upper().split(" ")
                    decoded = []
                    
                    for i in piece:
                        if not i:
                            continue
                        if i in reversed_baconian_dictionary:
                            decoded.append(reversed_baconian_dictionary[i])
                        elif i == "/":
                            decoded.append(" ")
                        else:
                            raise ValueError("Invalid Baconian block; use five A/B characters")
                    return "".join(decoded).capitalize()
            run_safely(baconian)

        case 5:
            def beaufort():
                text=input("Enter Plain Text: ")
                key = input("Enter Key: ").upper()
                encrypt = read_mode()
                    
                result =[]
                key_index= 0
                
                for x in text:
                    if x.isalpha():
                        #Defining start value
                        start = ord('A') if x.isupper() else ord('a')
                        #Getting Current Value
                        key_char = key[key_index % len(key)]
                        k_val = ord(key_char) - ord('A')
                        #text_value
                        t_val = ord(x) - start
                        
                        #Beaufort Formula -> Cipher = (Key - Text) % 26
                        c_val = (k_val - t_val) % 26
                        
                        #Convert back to text and preserve its case
                        cipher_char = chr(c_val + ord('A'))
                        result.append(cipher_char if x.isupper() else cipher_char.lower())
                        key_index+=1
                    else:
                        result.append(x)
                return "".join(result)
            run_safely(beaufort)

        case 6:
            def vigenere():
                text=input("Enter Plain Text: ")
                key = input("Enter Key: ").upper()
                encrypt = read_mode()
                
                result = ""
                key_index = 0
                
                for x in text:
                    if x.isalpha():
                        start = ord('A') if x.isupper() else ord('a')
                        #Turn current character into a shifted character
                        key_char = key[key_index % len(key)]
                        shift = ord(key_char) - ord('A')
                        
                        if not encrypt:
                            shift = -shift
                        result += chr((ord (x) - start + shift) % 26 + start)
                        key_index += 1
                    else:
                        result += x
                return result
            run_safely(vigenere)

        case 7:
            def xor():
                text=input("Enter Plain Text: ")
                key=input("Enter Key: ")
                encrypt = read_mode()
                
                if encrypt:
                    hex_output = []
                    for i, x in enumerate(text):
                        key_char = key[i % len(key)]
                        #perform xor operation
                        xor_result = ord(x) ^ ord(key_char)
                        #hex_output
                        hex_output.append(f"{xor_result:02x}")
                    return "".join(hex_output)
                else:
                    decoded = []
                    #processing the hex string in pair of 2 characters (each pairs consumes 1 byte)
                    byte_list = [text[i:i+2] for i in range(0,len(text),2)]
                    #print(byte_list)
                    for i,hex_byte in enumerate(byte_list):
                        key_char = key[i % len(key)]
                        #convert hex into base16
                        cipher_val = int(hex_byte, 16)
                        #xor it to reverse encyption
                        original_val = cipher_val ^ ord(key_char)
                        #convert the integer back to its original character
                        decoded.append(chr(original_val))
                    return "".join(decoded)
            run_safely(xor)

        case 8:
            def scytale():
                import math
                text=input("Enter Plain Text: ")
                diameter = read_integer("Enter Diameter: ")
                encrypt = read_mode()
                
                if encrypt:
                    if diameter <= 1:
                        return text
                    #number of columns (turns of rod we need)
                    num_cols = math.ceil(len(text) / diameter)
                    #padding text
                    padded_text = text.ljust(diameter * num_cols)
                    
                    encoded = []
                    for col in range(num_cols):
                        for row in range(diameter):
                            index = row * num_cols + col
                            encoded.append(padded_text[index])
                    return "".join(encoded)
                else:
                    #we can understand this as just removing the strip on the damn rod
                    if diameter <= 1:
                        return text
                    #number of columns (turns of rod we need)
                    num_cols = math.ceil(len(text) / diameter)
                    result = [None] * len(text)
                    #wat
                    current_char = 0
                    for col in range(num_cols):
                        for row in range(diameter):
                            index = row * num_cols + col
                            if current_char < len(text):
                                result[index] = text[current_char]
                                current_char +=1
                    return "".join(result).rstrip()
            run_safely(scytale)

        case 9:
            def rot13():
                text=input("Enter Plain Text: ")
                encrypt = read_mode()
                
                #baseline alphabets
                l_alpha = "abcdefghijklmnopqrstuvwxyz"
                u_alpha = l_alpha.upper()
                #target shifting
                shift_lower = l_alpha[13:] + l_alpha[:13]
                shift_upper = shift_lower.upper()
                #translation -> key, value = alpha,shifted_alpha
                trans = str.maketrans( l_alpha + u_alpha, shift_lower + shift_upper)
                return text.translate(trans)
            run_safely(rot13)

        case 10:
            def morse():
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
                #translation table
                
                encoder_map = {key: val + ' ' for key, val in MORSE_CODE_DICT.items()}
                encoder_map[' '] = '/ ' 
                trans = str.maketrans(encoder_map)
                # 2. FIX FOR DECODER: Create a clean reversed mapping for lookups
                REVERSED_MORSE_DICT = {val: key for key, val in MORSE_CODE_DICT.items()}
                REVERSED_MORSE_DICT['/'] = ' ' # Decode the slash back into a normal space
                
                text=input("Enter Plain Text: ")
                encrypt = read_mode()
                
                if encrypt:
                    return text.upper().translate(trans).strip()
                else:
                    #requires cleaning
                    tokens = text.split(' ')
                    result = []
                    
                    for token in tokens:
                        if token in REVERSED_MORSE_DICT:
                            result.append(REVERSED_MORSE_DICT[token])
                    return ''.join(result)
            run_safely(morse)
        